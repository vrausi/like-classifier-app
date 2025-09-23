# logic.py — pure decision-tree helpers (no Streamlit, no session use)
from collections import deque, defaultdict
from typing import Dict, List, Tuple, Optional, Set

from data import TRANSITIONS

def children(qid: str):
    y = TRANSITIONS.get((qid,'yes'))
    n = TRANSITIONS.get((qid,'no'))
    return y, n

def is_question(node_id) -> bool:
    return isinstance(node_id, str) and node_id.startswith('q')

def all_questions_from(root: str='q1') -> Set[str]:
    seen = set(); out = set(); dq = deque([root])
    while dq:
        cur = dq.popleft()
        if cur in seen or not is_question(cur):
            continue
        seen.add(cur); out.add(cur)
        y,n = children(cur)
        for nxt in (y,n):
            if is_question(nxt): dq.append(nxt)
    return out

def compute_path_and_focus(answers: Dict[str,str], root: str='q1'):
    """
    Follow answers from root until first unanswered or result.
    Returns (path_questions: list in order), focus_question (may be None), inactive_questions: set
    """
    all_qs = all_questions_from(root)
    path = []
    inactive = set()
    cur = root
    while is_question(cur):
        path.append(cur)
        ans = answers.get(cur)
        y,n = children(cur)
        if ans == 'yes':
            if is_question(n):
                inactive |= all_questions_from(n)
            cur = y
        elif ans == 'no':
            if is_question(y):
                inactive |= all_questions_from(y)
            cur = n
        else:
            return path, cur, inactive
        if not is_question(cur):
            return path, None, inactive
    return path, None, inactive

def infer_result(answers: Dict[str,str], root: str='q1') -> Optional[str]:
    cur = root
    guard = 0
    while guard < 500 and is_question(cur):
        guard += 1
        ans = answers.get(cur)
        y, n = children(cur)
        if ans == 'yes':
            cur = y
        elif ans == 'no':
            cur = n
        else:
            return None
    if isinstance(cur, str) and cur.startswith('result_'):
        return cur
    if cur == 'retry':
        return 'result_retry'
    return None

def all_paths_to_results(root: str='q1'):
    """
    Return dict: {result_id: [ [(qid,'yes'|'no'), ...], ... ] }
    Traverses TRANSITIONS and collects every route from root to each result_* node.
    """
    paths = defaultdict(list)
    def _dfs(node, acc):
        if isinstance(node, str) and node.startswith('result_'):
            paths[node].append(list(acc))
            return
        if not is_question(node):
            return
        for ans in ('yes', 'no'):
            nxt = TRANSITIONS.get((node, ans))
            if not nxt or nxt == 'retry':
                continue
            acc.append((node, ans))
            _dfs(nxt, acc)
            acc.pop()
    _dfs(root, [])
    return dict(paths)

def apply_path_to_answers(pairs, answers_dict: Dict[str, str]):
    """Replace current answers with a path (list of (qid, 'yes'|'no'))."""
    answers_dict.clear()
    for qid, ans in pairs:
        answers_dict[qid] = ans

def step_back_one(answers_dict: Dict[str,str], root: str='q1'):
    """
    Undo the most recent decision:
    - If we're at a result (focus=None), remove the answer to the last question on the path.
    - If we're mid-path (focus is first unanswered), remove the previous question's answer.
    """
    path, focus, _ = compute_path_and_focus(answers_dict, root)
    if not path:
        return
    if focus is None:
        last = path[-1]
        if last in answers_dict:
            del answers_dict[last]
    else:
        try:
            idx = path.index(focus)
        except ValueError:
            idx = len(path) - 1
        if idx > 0:
            prev = path[idx - 1]
            if prev in answers_dict:
                del answers_dict[prev]

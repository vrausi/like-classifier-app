import html
from dataclasses import dataclass
from pathlib import Path

import streamlit as st

# Local imports (must be in the same folder as app.py)
from utils_render import render_html
from data import (
    TRANSITIONS, QUESTIONS, EXAMPLES, RESULTS, RESULTS_SHORT, RESULTS_HELP,
    Q_FUNC, RES_FUNC, FEATURE_LABELS_TEXT
)
from logic import (
    compute_path_and_focus, infer_result, all_paths_to_results,
    apply_path_to_answers, step_back_one
)

# ----------------------------
# Basic page setup + CSS load
# ----------------------------
st.set_page_config(page_title="Discourse-Pragmatic LIKE Classifier", layout="wide")

# Load CSS from theme.css located next to app.py (do not crash if missing)
try:
    css = Path(__file__).with_name("theme.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ----------------------------
# Title + intro
# ----------------------------
st.title("Discourse-Pragmatic LIKE Classifier")

# Provide a safe default intro (monolith usually had this variable inline)
_intro_default = (
    "Welcome to the **LIKE** classifier! Use the decision tree to identify the function of **LIKE** in context.\n"
    "Based on your answers below, the tree first helps determine whether the use is **propositional** or "
    "**discourse-pragmatic (DP)**. If DP, the tree narrows down its core function either to a **discourse marker, "
    "a clause-medial pragmatic marker, a clause-final pragmatic marker, or a quotative marker** and then to a relevant "
    "subfunction.\nBrowse the list of functions on the right to view a brief description with examples."
)
st.markdown(render_html(_intro_default, "intro-prose"), unsafe_allow_html=True)

# ----------------------------
# Width tuning (kept minimal)
# ----------------------------
@dataclass(frozen=True)
class WidthTuning:
    W_ACTIVE: float = 4.0
    W_ANSWERED: float = 2.0
    W_INACTIVE: float = 1.0
    RESULTS_SHARE: float = 5.0
    EQUALIZE_ON_RESULT: bool = True

WT = WidthTuning()
ss = st.session_state
ss.setdefault("w_active", WT.W_ACTIVE)
ss.setdefault("w_answered", WT.W_ANSWERED)
ss.setdefault("w_inactive", WT.W_INACTIVE)
ss.setdefault("results_share", WT.RESULTS_SHARE)
ss.setdefault("equalize_on_result", WT.EQUALIZE_ON_RESULT)

w_active   = ss["w_active"]
w_answered = ss["w_answered"]
w_inactive = ss["w_inactive"]
results_share = ss["results_share"]
equalize_on_result = ss["equalize_on_result"]

# ----------------------------
# View options (sidebar)
# ----------------------------
hide_examples = st.sidebar.checkbox(
    "Hide examples", value=ss.get("hide_examples", False), key="hide_examples"
)
show_inactive = st.sidebar.checkbox(
    "Show inactive cards/columns", value=ss.get("show_inactive", False), key="show_inactive"
)
single_card_mode = st.sidebar.checkbox(
    "Single-card mode (show only active + answered)", value=True
)

# ----------------------------
# Session state for answers
# ----------------------------
if "answers" not in st.session_state:
    st.session_state.answers = {}
answers = st.session_state.answers

# Precompute routing helpers
RESULT_PATHS = all_paths_to_results('q1')

def _children(qid):
    y = TRANSITIONS.get((qid, 'yes'))
    n = TRANSITIONS.get((qid, 'no'))
    return y, n

def _is_question(node_id):
    return isinstance(node_id, str) and node_id.startswith('q')

# ----------------------------
# Compute layout state
# ----------------------------
path, focus, inactive = compute_path_and_focus(answers, 'q1')
res = infer_result(answers, 'q1')

# Build depth map (BFS)
from collections import deque as _dq
depth = {}
_qd = _dq([('q1', 0)]); _seen = set()
while _qd:
    cur, d = _qd.popleft()
    if cur in _seen or not _is_question(cur):
        continue
    _seen.add(cur); depth[cur] = d
    y, n = _children(cur)
    if _is_question(y): _qd.append((y, d + 1))
    if _is_question(n): _qd.append((n, d + 1))

# Guarantee a focus on first load
if not answers:
    focus = 'q1'

max_d = max(depth.values()) if depth else 0
n_cols = max_d + 1
fidx = depth.get(focus, 0)

answered_cols = { depth[q] for q, a in answers.items() if a in ('yes', 'no') }
answered_cols.discard(fidx)

w_active_eff = (w_answered if (res and equalize_on_result) else w_active)
weights_live = [1.0] if n_cols == 1 else [
    (w_active_eff if d == fidx else (w_answered if d in answered_cols else w_inactive))
    for d in range(n_cols)
]
weights_to_use = weights_live

# ----------------------------
# Layout: Cards (left) + Results (right)
# ----------------------------
st.markdown("<div id='layout-top'>", unsafe_allow_html=True)
outer_left, left_shell, spacer, col_results, outer_right = st.columns([0.5, 3, 0.4, 1, 0.5], gap="small")

# ----- Right pane: Jump to result -----
with col_results:
    st.markdown("<div id='results-pane' class='results-pane'>", unsafe_allow_html=True)
    st.markdown("<div class='results-header'>Jump to a result</div>", unsafe_allow_html=True)
    st.markdown("<div class='results-scroll'>", unsafe_allow_html=True)

    func_groups = ['root', 'quot', 'dm', 'pmmed', 'pmfin']
    headers = {
        'root':  'PROPOSITIONAL USE',
        'quot':  'QUOTATIVE MARKER',
        'dm':    'DISCOURSE MARKER',
        'pmmed': 'CLAUSE-MEDIAL PRAGMATIC MARKER',
        'pmfin': 'CLAUSE-FINAL PRAGMATIC MARKER'
    }

    for grp in func_groups:
        group_ids = [rid for rid in RESULTS if RES_FUNC.get(rid, 'root') == grp and rid != 'result_retry']
        if not group_ids:
            continue

        st.markdown(f"**{headers.get(grp, grp.upper())}**")
        for rid in group_ids:
            caption = RESULTS_SHORT.get(rid, RESULTS.get(rid, rid))
            clicked = st.button(
                caption,
                key=f"btn_go_resultpanel_{rid}",
                use_container_width=True,
                type="secondary"
            )
            if clicked:
                routes = RESULT_PATHS.get(rid, [])
                if routes:
                    idx_key = f"route_idx_{rid}"
                    idx = st.session_state.get(idx_key, 0)
                    apply_path_to_answers(routes[idx], st.session_state.answers)
                    st.session_state[idx_key] = (idx + 1) % len(routes)
                    st.rerun()
# ... inside the right-pane loop, right after the inner for rid in group_ids:
# (group_ids is already defined above)

# Show the hint ONLY under PROPOSITIONAL USE and DISCOURSE MARKER
        if grp == "root":
            if len(RESULT_PATHS.get("result_prop", [])) > 1:
                st.caption("2 paths — click again to view the other route")
        elif grp == "dm":
            if any(len(RESULT_PATHS.get(rid, [])) > 1 for rid in group_ids):
                st.caption("2 paths — click again to view the other route")
# (no caption for other groups)

        # ----- Left pane: toolbar, result pill, cards -----
with left_shell:
    # Toolbar
    st.markdown("<div class='btn-size-marker'></div>", unsafe_allow_html=True)
    b1, b2 = st.columns([1,1])
    with b1:
        if st.button("Back", key="btn_back", use_container_width=True, type="secondary"):
            step_back_one(st.session_state.answers, 'q1')
            st.rerun()
    with b2:
        if st.button("Clear all selections", key="btn_clear_all_top",
                     use_container_width=True, type="secondary"):
            st.session_state.answers = {}
            st.rerun()

    # Result pill + description
    res = infer_result(answers, 'q1')
    if res:
        label = RESULTS.get(res, str(res))
        st.markdown(f"<div class='res-badge'>{html.escape(label)}</div>", unsafe_allow_html=True)
        desc = RESULTS_HELP.get(res) or RESULTS_HELP.get(label)
        if desc:
            st.markdown(render_html(desc, "res-desc"), unsafe_allow_html=True)

    # Cards grid
    cols = st.columns(weights_to_use)
    render_order = sorted(depth.keys(), key=lambda q: (depth[q], q))

    for qid in render_order:
        d = depth[qid]

        # Single-card mode: show only active + answered
        if single_card_mode:
            _ans = answers.get(qid)
            is_answered = _ans in ('yes', 'no')
            is_active = (focus is not None and qid == focus)
            if not (is_active or is_answered):
                continue

        # status: inactive / path / focus / neutral
        if qid in inactive:
            status = 'inactive'
        elif qid in path:
            status = 'path'
        elif focus == qid:
            status = 'focus'
        else:
            status = 'neutral'

        # Hide inactive if toggle off
        if not show_inactive and status == 'inactive':
            continue

        current = answers.get(qid)        # 'yes' | 'no' | None
        answered = current in ('yes', 'no')
        dim_cls = "col-dim" if (focus is not None and d != fidx) else "col-focus"
        ans_cls = f"ans-{current}" if (status == 'path' and answered) else ""

        with cols[d]:
            st.markdown(
                f"<div class='cm-card {status} func-root {dim_cls} {ans_cls}'>",
                unsafe_allow_html=True
            )

            # Feature label chip (only when answered)
            _label = FEATURE_LABELS_TEXT.get((qid, current))
            if _label:
                _variant = "yes" if current == "yes" else "no"
                st.markdown(
                    f"<div class='cm-labelbar {_variant}'>{html.escape(_label)}</div>",
                    unsafe_allow_html=True
                )

            # Body (only when not answered)
            if not answered:
                st.markdown(render_html(QUESTIONS[qid], "cm-q"), unsafe_allow_html=True)

                if not hide_examples:
                    ex_text = EXAMPLES.get(qid, "")
                    if ex_text:
                        st.markdown(render_html(ex_text, "cm-ex"), unsafe_allow_html=True)

                disabled = (qid != focus)
                st.markdown("<div class='choice-row'>", unsafe_allow_html=True)
                col_yes, col_no = st.columns([1, 1])
                with col_yes:
                    yes_clicked = st.button(
                        "Yes",
                        key=f"btn_yes_{qid}",
                        use_container_width=True,
                        disabled=disabled,
                        type=("primary" if current == 'yes' else "secondary"),
                    )
                with col_no:
                    no_clicked = st.button(
                        "No",
                        key=f"btn_no_{qid}",
                        use_container_width=True,
                        disabled=disabled,
                        type=("primary" if current == 'no' else "secondary"),
                    )
                st.markdown("</div>", unsafe_allow_html=True)

                if not disabled:  # qid == focus
                    if yes_clicked:
                        answers[qid] = 'yes'
                        st.rerun()
                    if no_clicked:
                        answers[qid] = 'no'
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Footer — optional (no crash if missing in user's theme)
# ----------------------------
# Open footer wrapper (HTML)
st.markdown("<div id='app-footer' class='static'><div class='footer-inner'>", unsafe_allow_html=True)

# Content (pure Markdown → safe, clickable links, APA styled)
st.markdown(
"""
**Disclaimer**

- The example sentences are used for research/teaching purposes.
- Examples of propositional uses of **like** are sourced from the Oxford English Dictionary (OED), unless stated otherwise.
- Other examples are sourced from the demographically sampled component of the Spoken BNC1994 and the Spoken BNC2014 (available at https://cqpweb.lancs.ac.uk). The two corpora are easily distinguishable based on their speaker coding patterns — original spoken BNC1994 uses PSxx or KxxPSUNK, while the Spoken BNC2014 uses Sxxxx. Examples were edited for clarity and brevity, including ellipses; wording unchanged.
- The classification scheme, labels, and descriptions of functions come from Raušová (2023) and sources cited therein.

**Sources**

1. BNC Consortium. (2007). *The British National Corpus, XML Edition*. Oxford Text Archive. https://hdl.handle.net/20.500.12024/2554  
2. Love, R., Dembry, C., Hardie, A., Brezina, V., & McEnery, T. (2017). The Spoken BNC2014: Designing and building a spoken corpus of everyday conversations. *International Journal of Corpus Linguistics, 22*(3), 319–344. https://doi.org/10.1075/ijcl.22.3.02lov  
3. Oxford University Press. (n.d.). Like, adj., adv., conj., prep. In *Oxford English Dictionary*. (Retrieved September 16, 2025). https://doi.org/10.1093/OED/1074775262  
4. Raušová, V. (2023). *Discourse-pragmatic functions of like in spoken discourse* [Unpublished doctoral dissertation]. Faculty of Arts, Charles University. http://hdl.handle.net/20.500.11956/188271
""",
unsafe_allow_html=False
)

# Close footer wrapper (HTML)
st.markdown("</div></div>", unsafe_allow_html=True)

# Auto-generated from the monolith

TRANSITIONS = {
    ('q1','no'): 'q11', ('q1','yes'): 'q12',
    ('q11','yes'): 'q11a', ('q11','no'): 'q111',
    ('q11a','yes'): 'result_q11a_yes', ('q11a','no'): 'q11b',
    ('q11b','yes'): 'result_q11b_yes', ('q11b','no'): 'retry',
    ('q111','no'): 'result_prop', ('q111','yes'): 'q1111',
    ('q1111','no'): 'result_prop', ('q1111','yes'): 'q1111a',
    ('q1111a','yes'): 'q1111aa', ('q1111a','no'): 'q1111b',
    ('q1111aa','yes'):'result_elab',('q1111aa', 'no'): 'q1111ab',
    ('q1111ab','yes'):'result_clar',('q1111ab', 'no'): 'q1111ac',
    ('q1111ac','yes'):'result_exemp',('q1111ac','no'):'retry',
    ('q1111b','yes'): 'result_topic', ('q1111b','no'): 'q1111c',
    ('q1111c','yes'): 'q1111ca', ('q1111c','no'): 'retry',
    ('q1111ca','yes'): 'result_false', ('q1111ca','no'): 'q1111cb',
    ('q1111cb','yes'): 'result_repair', ('q1111cb','no'): 'q1111cc',
    ('q1111cc','yes'): 'result_repeat', ('q1111cc','no'): 'q1111cd',
    ('q1111cd','yes'): 'result_pause', ('q1111cd','no'): 'retry',

    ('q12','yes'): 'q12a', ('q12','no'): 'q121',
    ('q12a','yes'): 'result_q12a_yes', ('q12a','no'): 'q12b',
    ('q12b','yes'): 'result_q12b_yes', ('q12b','no'): 'retry',

    ('q121','yes'): 'q121a', ('q121','no'): 'q122',
    ('q121a','yes'): 'q121aa', ('q121a','no'): 'q121b',
    ('q121aa','yes'): 'result_elab', ('q121aa','no'): 'q121ab',
    ('q121ab','yes'): 'result_clar', ('q121ab','no'): 'q121ac',
    ('q121ac','yes'): 'result_exemp', ('q121ac','no'): 'retry',
    ('q121b','yes'): 'result_topic', ('q121b','no'): 'q121c',
    ('q121c','yes'): 'q121ca', ('q121c','no'): 'retry',
    ('q121ca','yes'): 'result_false', ('q121ca','no'): 'q121cb',
    ('q121cb','yes'): 'result_repair', ('q121cb','no'): 'q121cc',
    ('q121cc','yes'): 'result_repeat', ('q121cc','no'): 'q121cd',
    ('q121cd','yes'): 'result_pause', ('q121cd','no'): 'retry',

    ('q122','yes'): 'q122a', ('q122','no'): 'q123',
    ('q122a','yes'): 'result_loosen', ('q122a','no'): 'q122b',
    ('q122b','yes'): 'result_enrich', ('q122b','no'): 'q122c',
    ('q122c','yes'): 'result_focus', ('q122c','no'): 'retry',

    ('q123','yes'): 'q123a', ('q123','no'): 'retry',
    ('q123a','yes'): 'result_clear', ('q123a','no'): 'q123b',
    ('q123b','yes'): 'result_emph', ('q123b','no'): 'q123c',
    ('q123c','yes'): 'result_non_equiv_cf', ('q123c','no'): 'q123d',
    ('q123d','yes'): 'result_check', ('q123d','no'): 'q123e',
    ('q123e','yes'): 'result_respond', ('q123e','no'): 'retry'
}


QUESTIONS = {
    'q1': "Is LIKE omissible without affecting the propositional content or the grammatical well-formedness of the host clause?",
    'q11': "Is LIKE part of a quotative frame\n(_be + LIKE, IT'S LIKE_) and followed by quoted / reenacted / interpretively rendered material?",
    'q11a': "Does the material represent **ACTUAL SPEECH** that was actually produced or would have been produced in a hypothetical situation?",
    'q11b': "Does the material represent reports of **THOUGHTS, FEELINGS, and ATTITUDES**, usually not followed by other turns?",
    'q111': "Is LIKE part of an _IT'S LIKE_ construction?",
    'q1111': "Is the entire _IT'S LIKE_ construction omissible without affecting the propositional content or the grammatical well-formedness of the host clause?",
    'q1111a': "Does _IT'S LIKE_ occur clause initially, linking two adjacent segments of discourse\n(S1 IT'S LIKE S2)?",
    'q1111aa': "Does the material in S2 provide additional information to S1?\n\nCan it be paraphrased as\n_I should add…_'?",
    'q1111ab': "Does the material in S2 rephrase/clarify what is in S1?\n\nCan it be paraphrased as\n'_I should clarify/explain…'_?",
    'q1111ac': "Does the material in S2 exemplify what is in S1?\n\nCan it be paraphrased as\n'_for example_'?",
    'q1111b': "Does IT'S LIKE occur at a location of a topic shift (T1→T2)?\n\nCan it be paraphrased as '_by the way_', '_like I said before_', or '_anyway_'?",
    'q1111c': "Does IT'S LIKE occur clause externally marking a disfluency\n(false start, self-repair, repetition) or filling a pause?",
    'q1111ca': "Does the RM segment differ completely from the RR segment? (false start)",
    'q1111cb': "Does the RM segment correspond to RR with only a minor correction? (self-repair)",
    'q1111cc': "Is the RM segment fully repeated in the RR segment? (repetition)",
    'q1111cd': "Is _IT'S LIKE_ best analysed as a pause filler?\n\n Can it be paraphrased as '_let me think..._'?",
    'q12': "Is LIKE part of a quotative frame together with verbs of saying/thinking (e.g. _say, think, go_...)?",
    'q12a': "Does the material represent **ACTUAL SPEECH** that was actually produced or would have been produced in a hypothetical situation?",
    'q12b': "Does the material represent reports of **THOUGHTS, FEELINGS, and ATTITUDES**, usually not followed by other turns?",
    'q121': "Does LIKE appear clause-initially or outside of clause structure\n(e.g. linking segments of discourse, filling a pause)?",
    'q121a': "Does LIKE occur clause-initially, linking two adjacent segments of discourse\n(S1 LIKE S2)?",
    'q121aa': "Does S2 provide additional information to S1?\n\nCan it be best paraphrased as\n'_I should add…_'?",
    'q121ab': "Does S2 rephrase/clarify S1?\n\nCan it be best paraphrased as\n'_I should clarify…_'?",
    'q121ac': "Does S2 exemplify S1?\n\nCan it be best paraphrased as\n'_for example_'?",
    'q121b': "Does LIKE occur at a location of a topic shift (T1→T2)?\n\nCan it be paraphrased as '_by the way_', '_like I said before_', or '_anyway_'?",
    'q121c': "Does LIKE occur clause externally marking a disfluency\n(false start, self-repair, repetition)\nor filling a pause?",
    'q121ca': "Does the RM segment differ completely from the RR segment (**false start**)?",
    'q121cb': "Does the RM segment correspond to the RR segment only with a minor correction (**self-repair**)?",
    'q121cc': "Is the RM segment fully repeated in the RR segment? (**repetition**)?",
    'q121cd': "Is LIKE best analysed as a pause filler?\n\n Can it be paraphrased as\n'_let me think..._'?",
    'q122': "Does LIKE appear in clause-medial or phrase-internal position?",
    'q122a': "Is LIKE followed by a figuratively used expression requiring non-literal interpretation?\n or \nIs there a potential non-equivalence between what was said and what was meant, suggesting limited epistemic commitment?",
    'q122b': "Does the material following LIKE represent underspecified, vague expression or a conceptual placeholder?",
    'q122c': "Can the phrase following LIKE be interpreted as the most important information in the utterance?\n\nCan we use it-cleft or a pseudocleft to highlight the same piece of information?\n\n Alternatively, does it precede intensifiers/quantifiers?",
    'q123': "Does LIKE appear in clause-final position?",
    'q123a': "Can it be paraphrased as '_(just/so) to be clear_' or '_don't get me wrong_'?",
    'q123b': "Can LIKE be interpreted as emphasizing the illocutionary force of the preceding utterance?\nCan it be rephrased and replaced by 'really'?",
    'q123c': "Is LIKE preceded by figurative language or vague / underspecified expressions?\n\nIs there a potential non-equivalence between what was said and what was meant, suggesting limited epistemic commitment?",
    'q123d': "Can LIKE be paraphrased as '_if you know what I mean_', not expecting an explicit response?",
    'q123e': "Can LIKE be replaced by a standard reversed polarity question tag, a tag such as 'or?' to request an explicit response?"
}


EXAMPLES = {
    'q1': "PS147: _The little boy looks **LIKE** his mummy. → *The little boy looks his mummy._\n→ NOT OMISSIBLE.\n\nS0421: _It rose in popularity in **LIKE** the western world.\n✓ It rose in popularity in the western world._\n→ OMISSIBLE.",
    'q11': "S0509:_ …I got the white chocolate lollipop at the end and **she was LIKE** oh something for yourself is it? and **I was LIKE** no that's for my aunt too…_\n\nS0387: _he just said to us have you voted? And I was like I haven’t voted but did any of you vote? **IT'S LIKE** nah...\n\nS0439:... I ate it and then I binned I did bin some of it cos **I was LIKE** I can’t eat this whole thing […] then **I was LIKE** I just couldn’t decide whether it was raw or gooey…_",
    'q11a': "S0387: _He just said to us have you voted? And **I was LIKE** I haven’t voted but did any of you vote?_\n\nS0632: _...it’s shooting yourself in the foot when **people are LIKE** oh can you take on this project? **you’ll be LIKE** oh yeah yeah I haven’t you know I’ve got time to do it..._",
    'q11b': "S0041: _Were sat in the car together and she was close proximity and **I was LIKE** oo oo this is gonna be weird..._",
    'q111': "PS527: _When we went out with Robert I had a Phall which is erm **IT'S LIKE** you get all, all those different di, dishes..._",
    'q1111': "S0337: _What was I saying? **IT'S LIKE** what was I talking about?_\n→ OMISSIBLE\n\n_S0588: …it 's amazingly easy to drink **it 's LIKE** a milkshake…_\n→ NOT-OMISSIBLE",
    'q1111a': "S0644:_ If you can't look at someone there is a reason why you can't (S1) **LIKE** / **IT'S LIKE** (S2) body language has been studied to show that it happens for a reason._", 
    'q1111aa': "S0644: _If you can't look at someone there is a reason why you can't (S1) **LIKE** / **IT'S LIKE** (S2) body language has been studied to show that it happens for a reason._",
    'q1111ab': "PS0KN: _The house he’s got now is massive cos there's the living room (S1), **LIKE** / **IT'S LIKE** (S2) he's got two living rooms..._",
    'q1111ac': "S0300: _It's just the fact that our heads can't take too much (S1) **LIKE** / **IT'S LIKE** (S2) if I go into a pub or into a shop and you can just hear all these voices and music playing and my head just feels like it's gonna explode._",
    'q1111b': "S0416: _I’ll show you the first well I’ll tell the first five minutes (T1) **LIKE** / **IT'S LIKE** (T2) there's like this little –UNCLEARWORD and he's like a pupp- he's he's not like erm muppets puppets but like a puppet..._",
    'q1111c': "The disfluencies in this category are distinguished based on the correspondence of the material found in the segment to be deleted/repeated (RM) and the segment containing the correction/repetition (RR).\n\n**LIKE** or **IT'S LIKE** occur between these segments and often with other DMs.",
    'q1111ca': "PS03S: _...I mean now, er none of the shop keepers are sa, **LIKE** they were very helpful in our day weren't they?_\n\n → \n\n_I mean now, er (RM = none of the shop keepers are sa), **LIKE** (RR = hey were very helpful in our day weren't they?)_\n\nThe same function can be fulfilled by the construction **IT'S LIKE**.",
    'q1111cb': "S0520:_ ... we've all changed the way that we work you know some **LIKE** all of us have our things...\n\n → \n\n...we've all changed the way that we work you know(RM = some) **LIKE**(RR = all) of us have our things..._\n\nThe same function can be fulfilled by the construction **IT'S LIKE**.",
    'q1111cc': "S0416:_ Who's **LIKE** oh er who's got all the answers all the time?\n\n → \n\n_(RM = Who's) **LIKE** oh er (RR = who's ) got all the answers all the time?_\n\nThe same function can be fulfilled by the construction **IT'S LIKE**.",
    'q1111cd': "PS51F:_ Right. Erm well **LIKE** I usually take the train about ... twenty past eight._\nThe same function can be fulfilled by the construction **IT'S LIKE**.",
    'q12': "S0619: _I was like oh are you still with your girlfriend ? **he goes LIKE** oh no we broke up er a couple of weeks ago...\n\nS0008:...and I explained to him **I said LIKE** if you do that you 'll have to start drawing (.) down your savings..._",
    'q12a': "PS6RW: _…we drove past there one time and there was a woman standing outside, she **said LIKE**, oh what do you want, I was like, oh well, we've come to see the house..._",
    'q12b': "S0037:_ I looked at it this morning and **I thought LIKE** oh I should 've thinned that soup out earlier..._",
    'q121': "S0529:_ I don't know what to get her either (S1) **LIKE** (S2) I'm just so bad at present giving..._",
    'q121a': "LIKE joins two segments where S2 either elaborates, clarifies or exemplifies S1:\n\n_S0619: >>no I know I'm only kidding (S1) **LIKE** (S2) I know it's not my fault..._",
    'q121aa': "S0644: _If you can't look at someone there is a reason why you can't (S1) **LIKE** (S2) body language has been studied to show that it happens for a reason._",
    'q121ab': "S0644: _You know they do plagiarism now? (S1) **LIKE** (S2) they can scan your work to see if it’s plagiarised._",
    'q121ac': "PS0EB: _She’s not very good at English (S1), **LIKE** (S2) when they were doing Animal Farm, I had to explain that it was a parody of the Russian revolution._",
    'q121b': "S0530: _I'm wondering whether my eyesight's gonna go (T1) **LIKE** (T2) do we even does anyone here wear glasses?_",
    'q121c': "The disfluencies in this category are distinguished based on the correspondence of the material found in the segment to be deleted/repeated (RM) and the segment containing the correction/repetition (RR), **LIKE** occurs between these segments and often with other DMs.",
    'q121ca': "PS03S:_ ...I mean now, er none of the shop keepers are sa, **LIKE** they were very helpful in our day weren't they?_\n\n_I mean now, er (RM = none of the shop keepers are sa), **LIKE** (RR = hey were very helpful in our day weren't they?)_",
    'q121cb': "S0520:_ ... we've all changed the way that we work you know some **LIKE** all of us have our things...\n\n → \n\n...we've all changed the way that we work you know(RM = some) **LIKE** / **IT'S LIKE** (RR = all) of us have our things..._",
    'q121cc': "S0416:_ Who's **LIKE** oh er who's got all the answers all the time?\n\n → \n\n(RM = Who's) **LIKE** oh er (RR = who's) got all the answers all the time?_",
    'q121cd': "PS51F:_ Right. Erm well **LIKE** I usually take the train about ... twenty past eight._",
    'q122': "PS1GF: _The first sort of thing they ever had was just **LIKE** a little screen it just went blip and that’s it...\n\nS0587: Everything’s **LIKE** so expensive...\n\nPS04U: Just go into **LIKE** Safeways or somewhere.\n\nS0374: Have you got **LIKE** a menu thing?_",
    'q122a': "S0336: _...I’m **LIKE** baking hot by this point...\n\nPS0BK: My cleaner used to come in and just sort of **LIKE** clean around me and chat a bit. Dave’s cleaner in High Hall used to do loads of stuff for him._",
    'q122b': "PS6RB: _...Mark’s just got **LIKE** two speaker things._",
    'q122c': "S0325: _He didn’t get it cut much **LIKE** at the front.\n\nS0555: it's so weird cos he's **LIKE** very fundamentalist Christian..._",
    'q123': "PS03Y: _I dunno I’ve not checked **LIKE**. Terry said she was doing the stock so I left it to her.\n\nPS1EU: ...I said yes alright then, which was the Saturday **LIKE**.\n\n PS18E: Where's Paddy Ashdown from **LIKE**?\n\nPS0GM: What do you call it, them twilly things **LIKE**?_",
    'q123a': "PS03Y: _Supposed to be four hundred in the Ranch House last night. On the ground **LIKE**_.",
    'q123b': "PS0TU: _See it’s twelve fifty a go **LIKE**! → I REALLY cannot believe it that it is twelve fifty a go!\n\nKP3PS000: Well thick in what way **LIKE**? → I REALLY want to know what do you mean by 'thick'._",
    'q123c': "PS1JP: _Yeah. But I mean it's not just that, she's killing herself for the job **LIKE**!_",
    'q123d': "PS1ES: _Well it all adds up don’t it **LIKE**? You're [sic] heating costs is less. If you had a smaller place.\nPS1EN: Yeah._\n\n→ explicit response not expected, but may appear.",
    'q123e': "PS1HP: Has he got any bigger like cos he was small **LIKE**? PS1HH: No well he’s not...\n\nPS1FC: _Did she have her tea before she went out **LIKE**? Did she have summat to eat? PS1FE: No. No._\n\n→ explicit response requested.",
}


RESULTS = {
    'result_prop': 'PROPOSITIONAL USE (verb, noun, adjective, adverb...)',
    'result_q11a_yes': 'QUOTATIVE MARKER: introducing actual speech',
    'result_q11b_yes': 'QUOTATIVE MARKER: introducing thoughts, inner monologues and attitudes',
    'result_elab': 'DISCOURSE MARKER: discourse link – elaboration',
    'result_clar': 'DISCOURSE MARKER: discourse link – clarification',
    'result_exemp': 'DISCOURSE MARKER: discourse link – exemplification',
    'result_topic': 'DISCOURSE MARKER: topic orientation marker',
    'result_false': 'DISCOURSE MARKER: disfluency marker – false start',
    'result_repair': 'DISCOURSE MARKER: disfluency marker – self-repair',
    'result_repeat': 'DISCOURSE MARKER: disfluency marker – repetition',
    'result_pause': 'DISCOURSE MARKER: disfluency marker – pause filler',
    'result_q12a_yes': 'QUOTATIVE MARKER: introducing actual speech',
    'result_q12b_yes': 'QUOTATIVE MARKER: introducing thoughts, inner monologues and attitudes',
    'result_loosen': 'CLAUSE-MEDIAL PRAGMATIC MARKER: marker of non-equivalence requiring loosening of meaning',
    'result_enrich': 'CLAUSE-MEDIAL PRAGMATIC MARKER: marker of non-equivalence requiring enrichment of meaning',
    'result_focus': 'CLAUSE-MEDIAL PRAGMATIC MARKER: focus marker',
    'result_clear': 'CLAUSE-FINAL PRAGMATIC MARKER: focus marker – clearing up misunderstandings',
    'result_emph': 'CLAUSE-FINAL PRAGMATIC MARKER: focus marker – providing emphasis',
    'result_non_equiv_cf': 'CLAUSE-FINAL PRAGMATIC MARKER: marker of non-equivalence',
    'result_check': 'CLAUSE-FINAL PRAGMATIC MARKER: invariant tag – checking understanding with the hearer',
    'result_respond': 'CLAUSE-FINAL PRAGMATIC MARKER: invariant tag – requesting confirmation from the hearer',
    'result_retry': 'No result — go back or start again.',
}


RESULTS_SHORT = {
    # PROPOSITIONAL USE
    'result_prop': 'Verb, preposition, adjective, noun, comparative complementizer...',

    # QUOTATIVE MARKER
    'result_q11a_yes': '(be) + LIKE:\nactual speech',
    'result_q11b_yes': '(be) + LIKE:\nthoughts & attitudes',
    'result_q12a_yes': 'Verbs of saying\n+\nLIKE',
    'result_q12b_yes': 'Verbs of thinking\n+\nLIKE',

    # DISCOURSE MARKER
    'result_elab':  'Discourse link: elaboration',
    'result_clar':  'Discourse link: clarification',
    'result_exemp': 'Discourse link: exemplification',
    'result_topic': 'Topic orientation marker',
    'result_false': 'Disfluency marker: false start',
    'result_repair':'Disfluency marker: repair',
    'result_repeat':'Disfluency marker: repetition',
    'result_pause': 'Disfluency marker: pause filler',

    # CLAUSE-MEDIAL PRAGMATIC MARKER
    'result_loosen': 'Marker of non-equivalence: requiring loosening',
    'result_enrich': 'Marker of non-equivalence: requiring enrichment',
    'result_focus': 'Focus marker',

    # CLAUSE-FINAL PRAGMATIC MARKER
    'result_clear':        'Focus marker:  clearing up misunderstandings',
    'result_emph':         'Focus marker: providing emphasis',
    'result_non_equiv_cf': 'Marker of non-equivalence',
    'result_check':        'Invariant tag: checking understanding',
    'result_respond':      'Invariant tag: requesting confirmation',
}


RESULTS_HELP = {
    'result_prop': "**LIKE** is a content word (verb, preposition, noun, adjective, adverb, conjunction, comparative complementizer…).\nRemoving it affects the syntactic structure and grammaticality of the host clause.\n\n**Examples:**\n\n_Be sure to **like** us on Facebook for regular updates.\nHe, **like** the rest of the department, is in Bar Zero getting disgustingly drunk...\nPoliticians are **like** babies' nappies—they should be changed often, for the same reason.\n‘Well,’ the colonel said, ‘it sounds **like** a promising idea.’\nS0421: Oh,  it's hot in here it 's **like** a sauna._ (Spoken BNC2014)\n",

    'result_q11a_yes': "**LIKE** is used as a quotative, prototypically in a construction _be + LIKE_, although it may occur independently.\nIt marks the following material as representing reported speech that was actually uttered, would have been actually uttered in a hypothetical situation, or reconstructed from written sources.\nActual speech interpretation is often supported by the presence of adjacency pairs, explicit attribution by the speaker, or contextual hints such as direct address and comments on interlocutor's reaction.\n\n**Examples:**\n\n_S0439: **I was LIKE** what's wrong –ANONnameF? she goes I don't know what to pack and I was like well have you er c-ategorised your clothes?\n\nS0542: I said to –ANONnameF **I was LIKE** –ANONnameM is not gonna be happy.\n\nS0638: and **I'm LIKE** oh there’s a funny bit now –ANONnameF you can stop crying stop and you did cheer up a bit you just finally settled down and then they did the scene where he comes back a ghost.\n\n S0632: ...it’s shooting yourself in the foot when **people are LIKE** oh can you take on this project? **you’ll be LIKE** oh yeah yeah I haven’t you know I’ve got time to do it..._",
    'result_q11b_yes': "**LIKE** is used as a quotative: prototypically in a construction _be + LIKE_, although it may occur independently.\nIt marks the following material as representing reported thoughts, inner monologues, and attitudes. These are renditions of what the speaker recalls thinking, what they or others felt at a given time, or generalized expressions of sentiments and attitudes.\nCues supporting this line of interpretation involve absence of adjacency pairs, direct address, or other interactional cues. Alternatively, speakers might explicitly indicate that the quoted material was not actually uttered.\n\n**Examples:**\n\n_S0041: and then I felt a bit bad (.) and we were sat in the car together (.) and she was close proximity (.) and **I was LIKE** oo oo this is gonna be weird...\n\nS0140: it’s it’s I think it’s actually quite funny but **everyone else is LIKE** oh it’s rubbish but it is quite funny...\n\nS0619: oh no I've never h- I've never held a child in my arms **it’s LIKE** shit what do I do now? you know\n\nS0439:... I ate it and then I binned I did bin some of it cos **I was LIKE** I can’t eat this whole thing […] then **I was LIKE** I just couldn’t decide whether it was raw or gooey…_",
    'result_q12a_yes': "**LIKE** occurs  in quotative constructions with verbs of saying (e.g. say, go, yell...). \nIt marks the following material as representing reported speech that was aczually uttered, would have been actually uttered in a hypothetical situation, or reconstructed from written sources.\nActual speech interpretation is often supported by the presence of adjacency pairs, explicit attribution by the speaker, or contextual hints such as direct address and comments on interlocutor's reaction.\n\n**Examples:**\n\n_PS6RW: […] and like we drove past there one time and there was a woman standing outside, **she said LIKE**, oh what do you want, I was like, oh well, we've come to see the house […]\n\nS0619: I was like oh are you still with your girlfriend ? **he goes LIKE** oh no we broke up er a couple of weeks ago...\n\nS0008:...and I explained to him **I said LIKE** if you do that you 'll have to start drawing (.) down your savings..._",
    'result_q12b_yes': "**LIKE** occurs in quotative constructions with verbs of thinking (e.g. think...).\nIt marks the following material as representing reported thoughts, inner monologues, and attitudes.\n\n**Examples:**\n\n_S0037: […] I looked at it this morning and **I thought LIKE** oh I should 've thinned that soup out earlier in the week_",

    'result_elab':  "**LIKE** occurs clause initially (always at the beginning of S2) and functions as a discourse link between two discourse segments (S1 LIKE+S2).\nIn this case, the relationship between the two segments is **elaboration**, so S2 adds additional information to what was given in S1, e.g. further details, reasons, or evidence.\n**LIKE** can be paraphrased as 'I should add... / let me add...' in this case.\nThe same function can be fulfilled by the construction **IT'S LIKE**.\n\n**Examples:**\n\n_S0644: ++If you can't look at someone there is a reason why you can't++ (S1) **LIKE** (S2) ++body language has been studied to show that it happens for a reason.++\n\n\nPS0LK: I fancy one of these spirally type perms.\nPS0LR: Yeah. How do you do that?\nPS0LK: ++It's just the way they roll the curler on so I've been told but erm whether it's simple as that or not I don't know++ (S1). Mm. You know, **LIKE** (S2) ++they'd have to put a bit of a twist in it I suppose. So it sort of comes out sort of ringlets rather than a curl.++_",
    'result_clar':  "**LIKE** occurs clause initially (always at the beginning of S2) and functions as a discourse link between two discourse segments (S1 LIKE+S2).\nIn this case the relationship between the two segments is **clarification**, so S2 clarifies/explains what was said in S1.\n**LIKE** can be paraphrased as 'to clarify (what I mean by that)' / 'in other words' in this case.\nThe same function can be fulfilled by the construction **IT'S LIKE**.\n\n**Examples:**\n\n_S0644: so but and the reason I got that partly is cos ++you know they do plagiarism now++ (S1)? **LIKE** (S2) ++they can scan your work to see if it’s plagiarised++ mine was forty percent plagiarised which again was the maximum..._\n\nS0439:...Hayden Christensen's quite hot but he can't act his way out of bloody paper bag [...] ++he's worse than Pinocchio like on Rohypnol++ (S1) **LIKE** (S2) ++he's that bad...++",
    'result_exemp': "**LIKE** occurs clause initially (always at the beginning of S2) and functions as a discourse link between two discourse segments (S1 LIKE+S2).\nIn this case, the relationship between the two segments is **exemplification**, so S2 exemplifies S1.\n**LIKE** can be paraphrased as 'for example' or 'to add an example' in this case.\nThe same function can be fulfilled by the construction **IT'S LIKE**.\n\n**Examples:**\n\n_PS0EB: You remind me of bit, eh, you're like a bit what Joanne's like, except ++Joanne's better at maths but she’s not very good at English++ (S1), **LIKE** (S2) ++when they were doing Animal Farm, I had to explain that it was a parody of the Russian revolution and everything and she just sat there with her mouth open.++\n\n\nPS0LK: What's his argument now? \nPS0LM: ++I treated her rotten whilst I was studying++ (S1) **LIKE** (S2) ++I wouldn't take time off studying to go and see her or phone her..._++",
    'result_topic': "**LIKE** occurs at a location of a topic shift (e.g. T1 → T2), with 'topic' being understood as the subject of the discourse; what is being talked about.\n**LIKE** can, for example, signal return to a previous topic, a digression from the current topic, or an introduction of a new topic. It can be paraphrased as 'anyway', 'by the way or 'like I said before.'\n\n**Examples:**\n\n_S0530: I’m wondering whether my eyesight’s gonna go **LIKE** do we even does anyone here wear glasses?_",
    'result_false':  "**LIKE** occurs clause externally and functions as a marker of various disfluencies distinguished on the basis of their structure, which involves the segment to be deleted/repeated (reparandum - RM), the gap (interregnum - IM), and the segment containing the correction/repetition (repair - RR).\n\n In the case of a false start, there is no correspondence between RM and RR and **LIKE** occurs in the IM.\nThe speaker abandons their originally contributed material and starts anew. The same function can be fulfilled by the construction **IT'S LIKE**.\n\n**Examples:**\n\n_PS03S: Well it getting difference now here with most things, I mean now, er (RM = none of the shop keepers are sa), **LIKE** (RR = they were very helpful in our day weren't they?)\n\nS0328:[…] they're just stush as fuck (RM = they're so) er er **LIKE** erm sort of (RR = it’s always like late at night...)_",
    'result_repair': "**LIKE** occurs clause externally and functions as a marker of various disfluencies distinguished on the basis of their structure, which involves the segment to be deleted/repeated (reparandum - RM), the gap (interregnum - IM), and the segment containing the correction/repetition (repair - RR).\n\n In the case of a self-repair, there is some correspondence between RM and RR and the repair is either an insertion or a substitution of one element in an otherwise coherent structure. **LIKE** occurs in the IM and the same function can be fulfilled by the construction **IT'S LIKE**.\n\n**Examples:**\n\n_S0520: […] we've all changed the way that we work you know (RM = some some) **LIKE** (RR= all) of us have our things like –ANONnameF can be too bossy..._",
    'result_repeat': "**LIKE** occurs clause externally and functions as a marker of various disfluencies distinguished on the basis of their structure, which involves the segment to be deleted/repeated (reparandum - RM), the gap (interregnum - IM), and the segment containing the correction/repetition (repair - RR).\n\n In the case of a repetition, the RM and the RR segments are (nearly) identical. No correction takes place. **LIKE** occurs in the IM and may be accompanied by other DMs, filled pauses, etc. Serves primarily an evincive function and can be paraphrased as 'let me think.' The same function can be fulfilled by the construction **IT'S LIKE**.\n\n**Examples:**\n\n_PS08Y: I hate that programme because (RM = I) **LIKE** (RR = I) tend to come and listen to the content of what they're saying\n\nS0037:yeah (RM = I know (.) but they go in) **LIKE** (RR = I I know but they go in) like quarter (.)  like three and three and three quarters\n\nS0417: mm who just looks like they're good in the class? (RM = who's) **LIKE** oh er (RR = who's) got all the answers all the time?_",
    'result_pause':  "**LIKE** occurs clause externally and functions as a marker of various disfluencies distinguished on the basis of their structure, which involves the segment to be deleted/repeated (reparandum - RM), the gap (interregnum - IM), and the segment containing the correction/repetition (repair - RR).\n\n When filling a potential pause, there is no RR or RM segment, only the gap represented by the IM segment is filled.\n**LIKE** is often accompanied by unfilled and filled pauses, other DMs, interjections, or phrases suggesting planning difficulties and hesitation. \nIt serves as an evincive signal, suggesting the speaker is engaged in thinking/encountering planning difficulties but wishes to retain the floor.\nThe same function can be fulfilled by the construction **IT'S LIKE**.\n\n**Examples:**\n\n_S0417: >>but it's amazing isn't it ? ++I mean **LIKE** erm++ babies born a few months earlier are even surviving now...\n\nS0373: cos he was moving back to England (.) and he lived out there (.) erm although Switzerland is ++**LIKE** erm (.) like++ a tax haven or whatever it is..._",

    'result_loosen': "**LIKE** occurs clause internally and functions as a marker of non-equivalence between what was said and what was meant.\nIn this case **LIKE** typically precedes figurative language (hyperboles, metaphors...) suggesting that interpretation of these expressions requires conceptual loosening.\nIt can also involve non-literal interpretation based on looser commitment of the speaker regarding taboo expressions, expletives, or material that is, in a given context, otherwise inappropriate or inaccurate.\n\n**Examples:**\n\n_S0336: […] we had to be seated by half past two so I got there at like twenty-five to everybody was already seated I’m **LIKE** baking hot by this point...\n\nPS07F: I’ve never heard of him! Michael Bolton?\nPS07H: He’s **LIKE** a rock ballad si I dunno [unclear]. White. Good!\n\nPS51S: Well just say just say no, cos I mean she can't **LIKE** fucking rule your life._",
    'result_enrich': "**LIKE** occurs clause internally and functions as a marker of non-equivalence between what was said and what was meant.\nIn this case **LIKE** typically precedes vague language, conceptual placeholders or otherwise underspecified expressions that require pragmatic enrichment. \n\n**Examples:**\n\n_PS04U: yes and they wear a sort of **LIKE** a back thing on the back, is that Chinese?\nPS04Y: Oh yes, that’s, that’s Japanese.\n\nPS0BK: and that er he was er cos er last week there was supposed to be one of these big **LIKE** rave things on and it was cancelled at the last minute._",
    'result_focus':  "**LIKE** occurs clause internally and functions as a marker of focus, highlighting material that the speaker considers salient for interpretation of their utterances.\n**LIKE** can highlight information that is both new and familiar/given. It can also mark intensification or exemplification at the level of phrases.\n\n**Examples:**\n\n_S0254: […] cos I was never have got up bef- before seven\nS0253: and sometimes like my parents would drive […]\nS0254: >>yeah no I think I 'm talking about **LIKE** (.) high schools.\n\nPS6RG: That ro[ad], what's it called? It's got **LIKE** the back of the supermarket, back of the er Marks and Spencers.\n\nINTENSIFICATION\nS0529: >>although our cinema's **LIKE** really tiny it’s so annoying...\n\nEXEMPLIFICATION\nS0380: they have to use like ingredients which are like kind of expensive like they just throw **LIKE** truffle oil on everything and shit_",

    'result_clear':        "**LIKE** occurs clause finally, highlighting the preceding information, marking it as important, often to prevent misunderstanding or misinterpretation of what was said.\n**LIKE** can be paraphrased as 'just/so to be clear' or 'don't get me wrong.'\n\n**Examples:**\n\n_PS03Y:Supposed to be four hundred in the Ranch House last night. On the ground **LIKE**.\n\nPS01A: Communist countries. Everything's owned by the by the government and er, I know it’s not a right good thing, **LIKE** , but if it could work properly, it would be a damn good thing._",
    'result_emph':         "**LIKE** occurs clause finally, emphasizing the illocutionary force or the accompanying attitude conveyed by the preceding material.\n It can be reformulated so that the emphasis is expressed by 'really.'\n\n**Examples:**\n\n_Where's Paddy Ashdown from **LIKE**?\n→ 'I really want to know where is Paddy Ashdown from.'\n\n\nPS1EU: But I still had to pay the new increase **LIKE**!\n→ 'I really cannot believe that I still had to pay the new increase!'_",
    'result_non_equiv_cf': "**LIKE** occurs clause finally qualifying the preceding material, indicating a potential non-equivalence between what was said and what was meant. These uses involve either conceptual/commitment loosening or pragmatic enrichment.\n**LIKE** can be paraphrased as 'so to speak.'\nSee the respective categories of the clause-medial pragmatic marker **LIKE**. \n\n**Examples:**\n\n_PS1C1: You can't compromise your feelings just because of the money.\nPS1JP: Yeah. But I mean it's not just that, she's killing herself for the job **LIKE**!_",
    'result_check':        "**LIKE** occurs clause finally and functions as an invariant tag. In this function the speaker uses **LIKE** to check understanding with the hearer and **LIKE** can be paraphrased as 'if you know what I mean.' Explicit response is not required but the hearer may opt to supply a backchannel or some missing information.\n\n**Examples:**\n\n_PS03W: I wonder how much it would cost the town, **LIKE**? I know it sounds silly, but I say, the silly things like that are the ones that sometimes are the ones that are took seriously.\n\nPS1ES: Well it's it all adds up don't it **LIKE**? You're [sic] heating costs is less. If you had a smaller place._",
    'result_respond':      "**LIKE** occurs clause finally and functions as an invariant tag. In this function the speaker uses **LIKE** to request confirmation of what is being proposed.\nExplicit response is required.\n**LIKE** can be paraphrased as a regular opposite-polarity question tag, the conjunction 'or' or their combination.\n\n**Examples:**\n\n_S0662: >>well it's a space that she's got to work in (.) that she n- she's d- she's there now anyway **LIKE**? → (isn't she?)\nS0661: yeah she went she's been there for a few weeks now..._",
    'result_retry':        "**No result from this path.**\n\n"        "Your answers ruled out all options in this branch, so the tree can’t assign a function to the instance of **LIKE** you are trying to classify. \nUse the **Back** button to revisit the previous questions and consider other options in within this branch, or repeat the process from the start using the **Clear all selections** button.\n\n"
                           "_Note_: If the use is genuinely unclassifiable, mark the closest match and note the uncertainty."
}

Q_FUNC = {
    'q1':'root',

    # QUOTATIVE branch
    'q11':'quot','q11a':'quot','q11b':'quot',
    'q12':'quot','q12a':'quot','q12b':'quot',

    # DM branch after q11
    'q111':'dm','q1111':'dm','q1111a':'dm','q1111aa':'dm','q1111ab':'dm','q1111ac':'dm',
    'q1111b':'dm','q1111c':'dm','q1111ca':'dm','q1111cb':'dm','q1111cc':'dm','q1111cd':'dm',

    # DM branch after q12
    'q121':'dm','q121a':'dm','q121aa':'dm','q121ab':'dm','q121ac':'dm',
    'q121b':'dm','q121c':'dm','q121ca':'dm','q121cb':'dm','q121cc':'dm','q121cd':'dm',

    # PMM
    'q122':'pmmed','q122a':'pmmed','q122b':'pmmed','q122c':'pmmed',

    # PMF
    'q123':'pmfin','q123a':'pmfin','q123b':'pmfin','q123c':'pmfin','q123d':'pmfin','q123e':'pmfin',
}

RES_FUNC = {
    'result_prop':'root',

    # QUOTATIVE (speech vs thoughts)
    'result_q11a_yes':'quot','result_q11b_yes':'quot',
    'result_q12a_yes':'quot','result_q12b_yes':'quot',

    # DM
    'result_elab':'dm','result_clar':'dm','result_exemp':'dm','result_topic':'dm',
    'result_false':'dm','result_repair':'dm','result_repeat':'dm','result_pause':'dm',

    # PMM
    'result_loosen':'pmmed','result_enrich':'pmmed','result_focus':'pmmed',

    # PMF
    'result_clear':'pmfin','result_emph':'pmfin','result_non_equiv_cf':'pmfin',
    'result_check':'pmfin','result_respond':'pmfin',
}

FEATURE_LABELS_TEXT = {
    ('q1', 'no'): 'Not omissible',
    ('q1', 'yes'): 'Omissible',

    ('q11', 'no'): 'Not in quotative frame',
    ('q11', 'yes'): "Part of quotative frame (be/IT'S LIKE)",

    ('q11a', 'no'): 'Not introducing actual speech',
    ('q11a', 'yes'): 'Introduces actual speech',

    ('q11b', 'no'): 'Not introducing thoughts/attitudes',
    ('q11b', 'yes'): 'Introduces thoughts/inner monologues/attitudes',

    ('q111', 'no'): "Not in IT'S LIKE construction",
    ('q111', 'yes'): "Occurs in IT'S LIKE construction",

    ('q1111', 'no'): "IT'S LIKE not omissible (propositional)",
    ('q1111', 'yes'): "IT'S LIKE omissible (DM path)",

    ('q1111a', 'no'): 'Not clause-initial/extraclausal',
    ('q1111a', 'yes'): "Clause-initial/extraclausal (S1 IT'S LIKE S2)",

    ('q1111aa', 'no'): 'Not elaboration',
    ('q1111aa', 'yes'): 'Discourse link: S2 elaborates on S1',

    ('q1111ab', 'no'): 'Not clarification',
    ('q1111ab', 'yes'): 'Discourse link: S2 clarifies S1',

    ('q1111ac', 'no'): 'Not exemplification',
    ('q1111ac', 'yes'): 'Discourse link: S2 exemplifies S1',

    ('q1111b', 'no'): 'Not a topic-orientation marker',
    ('q1111b', 'yes'): 'Topic-orientation marker',

    ('q1111c', 'no'): 'Not marking disfluencies/pauses',
    ('q1111c', 'yes'): 'Marks disfluencies/pauses',

    ('q1111ca', 'no'): 'Not marking a false start',
    ('q1111ca', 'yes'): 'Marks a false start',

    ('q1111cb', 'no'): 'Not marking a self-repair',
    ('q1111cb', 'yes'): 'Marks a self-repair',

    ('q1111cc', 'no'): 'Not marking a repetition',
    ('q1111cc', 'yes'): 'Marks a repetition',

    ('q1111cd', 'no'): 'Not a pause filler',
    ('q1111cd', 'yes'): 'Fills a pause',

    ('q12', 'no'): 'Not in a quotative construction with verbs of saying/thinking',
    ('q12', 'yes'): 'Quotative with verbs of saying/thinking',

    ('q12a', 'no'): 'Not introducing actual speech',
    ('q12a', 'yes'): 'Introduces actual speech',

    ('q12b', 'no'): 'Not introducing thoughts/attitudes',
    ('q12b', 'yes'): 'Introduces thoughts/inner monologue/attitudes',

    ('q121', 'no'): 'Not clause-initial / extra-clausal',
    ('q121', 'yes'): 'Clause-initial / extra-clausal position',

    ('q121a', 'no'): 'Not linking adjacent segments',
    ('q121a', 'yes'): 'Discourse link (S1—LIKE—S2)',

    ('q121aa', 'no'): 'Not elaboration',
    ('q121aa', 'yes'): 'Discourse link: S2 elaborates on S1',

    ('q121ab', 'no'): 'Not clarification',
    ('q121ab', 'yes'): 'Discourse link: S2 clarifies S1',

    ('q121ac', 'no'): 'Not exemplification',
    ('q121ac', 'yes'): 'Discourse link: S2 exemplifies S1',

    ('q121b', 'no'): 'Not a topic-orientation marker',
    ('q121b', 'yes'): 'Topic-orientation marker (shift/return)',

    ('q121c', 'no'): 'Not marking disfluencies/pauses',
    ('q121c', 'yes'): 'Marks disfluencies/pauses',

    ('q121ca', 'no'): 'Not marking a false start',
    ('q121ca', 'yes'): 'Marks a false start',

    ('q121cb', 'no'): 'Not marking a self-repair',
    ('q121cb', 'yes'): 'Marks a self-repair',

    ('q121cc', 'no'): 'Not marking a repetition',
    ('q121cc', 'yes'): 'Marks a repetition',

    ('q121cd', 'no'): 'Not a pause filler',
    ('q121cd', 'yes'): 'Fills a pause',

    ('q122', 'no'): 'Not clause-medial / phrase-internal',
    ('q122', 'yes'): 'Clause-medial / phrase-internal position',

    ('q122a', 'no'): 'Not marking non-equivalence. Looser interpretation not intended.',
    ('q122a', 'yes'): 'Marks non-equivalence → looser interpretation intended',

    ('q122b', 'no'): 'Not marking non-equivalence. Pragmatic enrichment not intended.',
    ('q122b', 'yes'): 'Marks non-equivalence → pragmatic enrichment intended',

    ('q122c', 'no'): 'Not marking focus',
    ('q122c', 'yes'): 'Marks focus (new/important/intensified information)',

    ('q123', 'no'): 'Not clause-final',
    ('q123', 'yes'): 'Clause-final position',

    ('q123a', 'no'): 'Not used to clear up misunderstandings.',
    ('q123a', 'yes'): 'Marks focus (clearing up misunderstandings)',

    ('q123b', 'no'): 'Not used to mark emphasis.',
    ('q123b', 'yes'): 'Marks focus. Marks emphasis.',

    ('q123c', 'no'): 'Not marking non-equivalence. Looser interpretation/pragmatic enrichment not intended.',
    ('q123c', 'yes'): 'Marks non-equivalence. Looser interpretation/pragmatic enrichment intended.',

    ('q123d', 'no'): 'Not an invariant tag serving to check understanding.',
    ('q123d', 'yes'): 'Invariant tag: checking understanding',

    ('q123e', 'no'): 'Not an invariant tag serving to request confirmation.',
    ('q123e', 'yes'): 'Invariant tag: requesting confirmation',
}


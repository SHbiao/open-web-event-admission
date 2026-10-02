# Web Text Admission Annotation Guide

Judge only the displayed body, UTC time, and reply/quote/media flags. Do not open links, parent posts, images, or videos. Do not browse or use external facts.

Choose exactly one action:

- **ADMISSIBLE**: the displayed text is sufficient to organize at least one qualified real-world event target.
- **REJECT**: the displayed text does not meet that admission requirement. It may lack an event target, use events only as background, or omit context essential to identifying an organizational target.

`REJECT` is an operational no-admission action, not a claim that nothing happened.

## Clause codes

- `A1`: A real-world occurrence, action, change, result, institutional act, or explicit event reference is primary information.
- `A2`: A comment, reply, historical event, small event, or personal experience still supplies a sufficiently identifiable event target.
- `R1`: The text is mainly an abstract opinion, general property, generic recommendation, wordplay, or fictional discussion without a qualifying real-world event target.
- `R2`: An event appears only as background, comparison, or example rather than an organizational target.
- `R3`: Missing referents, context, or unseen media prevent the displayed text from supporting a target.

Do not reject merely because date, location, participants, or a knowledge-base page are incomplete. An explicit decision, statement, plan, or ongoing action may be admissible. A wish, hypothetical, or conditional discussion does not by itself establish that an action occurred.

Return one concise evidence statement, not hidden reasoning or chain-of-thought. For `ADMISSIBLE`, quote the shortest exact span supporting the target. For `REJECT`, the evidence span may be empty when no qualifying span exists.

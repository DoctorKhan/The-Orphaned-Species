# Volume IV — *The Court of Threads* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 10
- **Total flag instances:** 28

| Flag | Chapters |
|---|---|
| SHORT-PARA-RUN | 10 |
| TELL-NOT-SHOW | 9 |
| STACKED-EM-DASHES | 3 |
| ABSTRACT-DENSE | 1 |
| IDENTICAL-PARA-OPENING | 1 |
| OPEN-LIGHT-ON-BODY | 1 |
| ECHO-CLOSER | 1 |
| NOT-X-BUT-Y | 1 |
| ABSTRACT-OVER-BODY | 1 |

## Chapter-level detail

### ## Chapter One—The Doors
- **Word count:** 7305
- **Sentence count:** 791
- **Flags:**
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (12 hits)
  - ABSTRACT-DENSE (44 abstract terms, 187 body terms)
  - SHORT-PARA-RUN (33 run(s) of 3+ short paragraphs)
  - IDENTICAL-PARA-OPENING (2 run(s) of 3+ same-shape openings)

### ## Chapter Two—Present Consent
- **Word count:** 1511
- **Sentence count:** 238
- **Flags:**
  - SHORT-PARA-RUN (8 run(s) of 3+ short paragraphs)

### ## Chapter Three—Three Rooms
- **Word count:** 2360
- **Sentence count:** 283
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (6 hits)
  - OPEN-LIGHT-ON-BODY
  - SHORT-PARA-RUN (12 run(s) of 3+ short paragraphs)

### ## Chapter Four—What We Build
- **Word count:** 2951
- **Sentence count:** 361
- **Flags:**
  - TELL-NOT-SHOW (6 hits)
  - SHORT-PARA-RUN (11 run(s) of 3+ short paragraphs)

### ## Chapter Five—The Rumor
- **Word count:** 2077
- **Sentence count:** 289
- **Flags:**
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (6 hits)
  - SHORT-PARA-RUN (8 run(s) of 3+ short paragraphs)

### ## Chapter Six—The Statement
- **Word count:** 2322
- **Sentence count:** 307
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - TELL-NOT-SHOW (3 hits)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 1 body)
  - SHORT-PARA-RUN (14 run(s) of 3+ short paragraphs)

### ## Chapter Seven—The Two Houses
- **Word count:** 3384
- **Sentence count:** 377
- **Flags:**
  - TELL-NOT-SHOW (9 hits)
  - SHORT-PARA-RUN (18 run(s) of 3+ short paragraphs)

### ## Chapter Eight—The Succession Debate
- **Word count:** 2800
- **Sentence count:** 336
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (4 hits)
  - SHORT-PARA-RUN (14 run(s) of 3+ short paragraphs)

### ## Chapter Nine—The Room Prepared
- **Word count:** 1703
- **Sentence count:** 231
- **Flags:**
  - TELL-NOT-SHOW (2 hits)
  - SHORT-PARA-RUN (6 run(s) of 3+ short paragraphs)

### ## Chapter Ten—Before the First Breath
- **Word count:** 4211
- **Sentence count:** 500
- **Flags:**
  - TELL-NOT-SHOW (5 hits)
  - SHORT-PARA-RUN (22 run(s) of 3+ short paragraphs)

## Open items

1. These are heuristic flags, not verdicts. Review flagged passages individually.
2. `ABSTRACT-OVER-BODY` uses a sliding window; tune the window size if false-positive rate is high.
3. `STALE-FRAMING` is pattern-based; expand `STALE_FRAMING` after each lock change.
4. `ABSTRACT-OPEN` / `OPEN-LIGHT-ON-BODY` check the first paragraph only.
5. `SHORT-PARA-RUN` / `LONG-PARAGRAPH` / `IDENTICAL-PARA-OPENING` are rhythm flags, not prose verdicts. Review in context.
6. Paragraph metrics are collected per-chapter; short/long paragraph counts can be inflated by dialogue, metadata, or intentional rhythm.
7. `TIDY-COMPARISON` flags symmetrical simile syntax; review for interchangeability, not every instance is wrong.

## Methodology

Pattern checks applied:
- `NOT-X-BUT-Y`: default contrastive shape
- `TIDY-COMPARISON`: symmetrical simile/comparison syntax
- `STACKED-EM-DASHES`: 2+ em dashes in one sentence
- `COLON-HEAVY`: 2+ colons in one sentence
- `ECHO-CLOSER`: final-sentence thematic restatement
- `TELL-NOT-SHOW`: interpretive-telling words
- `ABSTRACT-DENSE`: high abstract-noun count
- `ABSTRACT-OVER-BODY`: abstract terms outweigh body terms in a local window
- `ABSTRACT-OPEN` / `OPEN-LIGHT-ON-BODY`: chapter open without physical body
- `STALE-FRAMING`: superseded canonical phrasing
- `SHORT-PARA-RUN`: 3+ consecutive paragraphs under 25 words
- `LONG-PARAGRAPH`: paragraph over 250 words
- `IDENTICAL-PARA-OPENING`: 3+ consecutive paragraphs opening with same word shape
- `ABSTRACT-OPEN-PARA`: paragraph opening with abstract thematic language

Source: `14_literary_speculative_thriller_style_guide.md` § *Generic-cadence / AI-pattern checklist* and § *Human-prose lock*; `AGENTS.md` prose discipline.
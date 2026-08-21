# Volume III — *The Compact* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 10
- **Total flag instances:** 39

| Flag | Chapters |
|---|---|
| TELL-NOT-SHOW | 10 |
| SHORT-PARA-RUN | 10 |
| NOT-X-BUT-Y | 6 |
| ABSTRACT-DENSE | 5 |
| STACKED-EM-DASHES | 3 |
| ECHO-CLOSER | 3 |
| ABSTRACT-OVER-BODY | 1 |
| IDENTICAL-PARA-OPENING | 1 |

## Chapter-level detail

### ## Chapter One—The Boat at Morning
- **Word count:** 3498
- **Sentence count:** 509
- **Flags:**
  - NOT-X-BUT-Y (3 hits)
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (9 hits)
  - ABSTRACT-DENSE (22 abstract terms, 107 body terms)
  - SHORT-PARA-RUN (27 run(s) of 3+ short paragraphs)

### ## Chapter Two—Terms of Welcome
- **Word count:** 3938
- **Sentence count:** 496
- **Flags:**
  - TELL-NOT-SHOW (5 hits)
  - SHORT-PARA-RUN (22 run(s) of 3+ short paragraphs)

### ## Chapter Three—Three Requests
- **Word count:** 2175
- **Sentence count:** 281
- **Flags:**
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (2 hits)
  - SHORT-PARA-RUN (13 run(s) of 3+ short paragraphs)

### ## Chapter Four—Lang's Folder
- **Word count:** 4446
- **Sentence count:** 519
- **Flags:**
  - NOT-X-BUT-Y (3 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-DENSE (21 abstract terms, 95 body terms)
  - SHORT-PARA-RUN (27 run(s) of 3+ short paragraphs)

### ## Chapter Five—The Names They Carry
- **Word count:** 3800
- **Sentence count:** 458
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (5 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (12 hits)
  - ABSTRACT-DENSE (26 abstract terms, 84 body terms)
  - SHORT-PARA-RUN (30 run(s) of 3+ short paragraphs)

### ## Chapter Six—The Compact
- **Word count:** 3779
- **Sentence count:** 449
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - TELL-NOT-SHOW (7 hits)
  - ABSTRACT-DENSE (31 abstract terms, 69 body terms)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 0 body)
  - SHORT-PARA-RUN (27 run(s) of 3+ short paragraphs)

### ## Chapter Seven—A Crown With an End
- **Word count:** 2946
- **Sentence count:** 353
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (3 hits)
  - SHORT-PARA-RUN (19 run(s) of 3+ short paragraphs)
  - IDENTICAL-PARA-OPENING (1 run(s) of 3+ same-shape openings)

### ## Chapter Eight—The Cost of Consent
- **Word count:** 3826
- **Sentence count:** 496
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - TELL-NOT-SHOW (5 hits)
  - SHORT-PARA-RUN (16 run(s) of 3+ short paragraphs)

### ## Chapter Nine—The Packet
- **Word count:** 3500
- **Sentence count:** 456
- **Flags:**
  - TELL-NOT-SHOW (1 hits)
  - ABSTRACT-DENSE (22 abstract terms, 86 body terms)
  - SHORT-PARA-RUN (18 run(s) of 3+ short paragraphs)

### ## Chapter Ten—The Handover
- **Word count:** 1997
- **Sentence count:** 237
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (3 hits)
  - SHORT-PARA-RUN (12 run(s) of 3+ short paragraphs)

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
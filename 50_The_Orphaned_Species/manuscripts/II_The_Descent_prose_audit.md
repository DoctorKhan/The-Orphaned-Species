# Volume II — *The Descent* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 10
- **Total flag instances:** 24

| Flag | Chapters |
|---|---|
| SHORT-PARA-RUN | 10 |
| NOT-X-BUT-Y | 6 |
| STACKED-EM-DASHES | 4 |
| ABSTRACT-DENSE | 3 |
| ABSTRACT-OVER-BODY | 1 |

## Chapter-level detail

### ## Chapter One—What Came Home
- **Word count:** 3088
- **Sentence count:** 354
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - SHORT-PARA-RUN (23 run(s) of 3+ short paragraphs)

### ## Chapter Two—The Cold Container
- **Word count:** 3998
- **Sentence count:** 479
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - ABSTRACT-DENSE (31 abstract terms, 120 body terms)
  - SHORT-PARA-RUN (25 run(s) of 3+ short paragraphs)

### ## Chapter Three—The Buried Instrument
- **Word count:** 4647
- **Sentence count:** 610
- **Flags:**
  - NOT-X-BUT-Y (3 hits)
  - SHORT-PARA-RUN (33 run(s) of 3+ short paragraphs)

### ## Chapter Four—The Healer's Terms
- **Word count:** 3203
- **Sentence count:** 561
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - SHORT-PARA-RUN (20 run(s) of 3+ short paragraphs)

### ## Chapter Five—The Holding Site
- **Word count:** 4197
- **Sentence count:** 557
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (1 hits)
  - SHORT-PARA-RUN (27 run(s) of 3+ short paragraphs)

### ## Chapter Six—The Changing Map
- **Word count:** 3702
- **Sentence count:** 532
- **Flags:**
  - SHORT-PARA-RUN (18 run(s) of 3+ short paragraphs)

### ## Chapter Seven—The Riddling Ground
- **Word count:** 4759
- **Sentence count:** 609
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (4 hits)
  - ABSTRACT-DENSE (24 abstract terms, 183 body terms)
  - SHORT-PARA-RUN (30 run(s) of 3+ short paragraphs)

### ## Chapter Eight—The Corridor Signal
- **Word count:** 2270
- **Sentence count:** 299
- **Flags:**
  - STACKED-EM-DASHES (3 hits)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 1 body)
  - SHORT-PARA-RUN (12 run(s) of 3+ short paragraphs)

### ## Chapter Nine—The Staff Entrance
- **Word count:** 3294
- **Sentence count:** 436
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - ABSTRACT-DENSE (22 abstract terms, 116 body terms)
  - SHORT-PARA-RUN (19 run(s) of 3+ short paragraphs)

### ## Chapter Ten—Release
- **Word count:** 4364
- **Sentence count:** 696
- **Flags:**
  - SHORT-PARA-RUN (29 run(s) of 3+ short paragraphs)

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
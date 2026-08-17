# Volume II — *The Descent* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 10
- **Total flag instances:** 25

| Flag | Chapters |
|---|---|
| TELL-NOT-SHOW | 10 |
| NOT-X-BUT-Y | 7 |
| STACKED-EM-DASHES | 4 |
| ABSTRACT-DENSE | 3 |
| ABSTRACT-OVER-BODY | 1 |

## Chapter-level detail

### ## Chapter One—What Came Home
- **Word count:** 3089
- **Sentence count:** 354
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - TELL-NOT-SHOW (6 hits)

### ## Chapter Two—The Cold Container
- **Word count:** 4021
- **Sentence count:** 481
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - TELL-NOT-SHOW (9 hits)
  - ABSTRACT-DENSE (31 abstract terms, 120 body terms)

### ## Chapter Three—The Buried Instrument
- **Word count:** 4654
- **Sentence count:** 610
- **Flags:**
  - NOT-X-BUT-Y (3 hits)
  - TELL-NOT-SHOW (11 hits)

### ## Chapter Four—The Healer's Terms
- **Word count:** 3203
- **Sentence count:** 561
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (6 hits)

### ## Chapter Five—The Holding Site
- **Word count:** 4183
- **Sentence count:** 556
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (6 hits)

### ## Chapter Six—The Changing Map
- **Word count:** 3702
- **Sentence count:** 532
- **Flags:**
  - TELL-NOT-SHOW (3 hits)

### ## Chapter Seven—The Riddling Ground
- **Word count:** 4737
- **Sentence count:** 608
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (11 hits)
  - ABSTRACT-DENSE (23 abstract terms, 183 body terms)

### ## Chapter Eight—The Corridor Signal
- **Word count:** 2284
- **Sentence count:** 299
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (3 hits)
  - TELL-NOT-SHOW (8 hits)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 1 body)

### ## Chapter Nine—The Staff Entrance
- **Word count:** 3294
- **Sentence count:** 436
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - TELL-NOT-SHOW (4 hits)
  - ABSTRACT-DENSE (22 abstract terms, 116 body terms)

### ## Chapter Ten—Release
- **Word count:** 4364
- **Sentence count:** 696
- **Flags:**
  - TELL-NOT-SHOW (5 hits)

## Open items

1. These are heuristic flags, not verdicts. Review flagged passages individually.
2. `ABSTRACT-OVER-BODY` uses a sliding window; tune the window size if false-positive rate is high.
3. `STALE-FRAMING` is pattern-based; expand `STALE_FRAMING` after each lock change.
4. `ABSTRACT-OPEN` / `OPEN-LIGHT-ON-BODY` check the first paragraph only.

## Methodology

Pattern checks applied:
- `NOT-X-BUT-Y`: default contrastive shape
- `STACKED-EM-DASHES`: 2+ em dashes in one sentence
- `COLON-HEAVY`: 2+ colons in one sentence
- `ECHO-CLOSER`: final-sentence thematic restatement
- `TELL-NOT-SHOW`: interpretive-telling words
- `ABSTRACT-DENSE`: high abstract-noun count
- `ABSTRACT-OVER-BODY`: abstract terms outweigh body terms in a local window
- `ABSTRACT-OPEN` / `OPEN-LIGHT-ON-BODY`: chapter open without physical body
- `STALE-FRAMING`: superseded canonical phrasing

Source: `14_literary_speculative_thriller_style_guide.md` § *Generic-cadence / AI-pattern checklist* and § *Human-prose lock*; `AGENTS.md` prose discipline.
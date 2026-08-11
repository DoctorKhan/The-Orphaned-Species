# Volume II — *The Descent* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 10
- **Total flag instances:** 42

| Flag | Chapters |
|---|---|
| STACKED-EM-DASHES | 10 |
| TELL-NOT-SHOW | 10 |
| ABSTRACT-OVER-BODY | 10 |
| NOT-X-BUT-Y | 8 |
| ABSTRACT-DENSE | 4 |

## Chapter-level detail

### ## Chapter One—What Came Home
- **Word count:** 3344
- **Sentence count:** 391
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (3 hits)
  - TELL-NOT-SHOW (7 hits)
  - ABSTRACT-OVER-BODY (windowed 12 abstract vs 2 body)

### ## Chapter Two—The Folly
- **Word count:** 3939
- **Sentence count:** 476
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (10 hits)
  - ABSTRACT-DENSE (32 abstract terms, 112 body terms)
  - ABSTRACT-OVER-BODY (windowed 32 abstract vs 0 body)

### ## Chapter Three—The Buried Instrument
- **Word count:** 3396
- **Sentence count:** 453
- **Flags:**
  - NOT-X-BUT-Y (4 hits)
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (9 hits)
  - ABSTRACT-OVER-BODY (windowed 14 abstract vs 0 body)

### ## Chapter Four—The Healer's Terms
- **Word count:** 4302
- **Sentence count:** 616
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (7 hits)
  - TELL-NOT-SHOW (10 hits)
  - ABSTRACT-DENSE (23 abstract terms, 150 body terms)
  - ABSTRACT-OVER-BODY (windowed 23 abstract vs 0 body)

### ## Chapter Five—What They Took
- **Word count:** 4013
- **Sentence count:** 538
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (7 hits)
  - ABSTRACT-OVER-BODY (windowed 14 abstract vs 0 body)

### ## Chapter Six—The Changing Map
- **Word count:** 3397
- **Sentence count:** 497
- **Flags:**
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (4 hits)
  - ABSTRACT-OVER-BODY (windowed 13 abstract vs 1 body)

### ## Chapter Seven—The Riddling Ground
- **Word count:** 4132
- **Sentence count:** 538
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (8 hits)
  - TELL-NOT-SHOW (11 hits)
  - ABSTRACT-DENSE (21 abstract terms, 157 body terms)
  - ABSTRACT-OVER-BODY (windowed 21 abstract vs 2 body)

### ## Chapter Eight—The Corridor Signal
- **Word count:** 2339
- **Sentence count:** 310
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (6 hits)
  - TELL-NOT-SHOW (10 hits)
  - ABSTRACT-DENSE (21 abstract terms, 65 body terms)
  - ABSTRACT-OVER-BODY (windowed 21 abstract vs 1 body)

### ## Chapter Nine—The Transmission Station
- **Word count:** 3041
- **Sentence count:** 433
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (3 hits)
  - ABSTRACT-OVER-BODY (windowed 18 abstract vs 0 body)

### ## Chapter Ten—Release
- **Word count:** 4327
- **Sentence count:** 717
- **Flags:**
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-OVER-BODY (windowed 20 abstract vs 0 body)

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
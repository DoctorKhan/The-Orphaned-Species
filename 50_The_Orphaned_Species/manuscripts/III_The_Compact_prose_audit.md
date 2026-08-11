# Volume III — *The Compact* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 10
- **Total flag instances:** 44

| Flag | Chapters |
|---|---|
| STACKED-EM-DASHES | 10 |
| TELL-NOT-SHOW | 10 |
| ABSTRACT-OVER-BODY | 10 |
| NOT-X-BUT-Y | 6 |
| ABSTRACT-DENSE | 5 |
| ECHO-CLOSER | 3 |

## Chapter-level detail

### ## Chapter One—The Boat at Morning
- **Word count:** 3370
- **Sentence count:** 488
- **Flags:**
  - NOT-X-BUT-Y (3 hits)
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (8 hits)
  - ABSTRACT-DENSE (22 abstract terms, 102 body terms)
  - ABSTRACT-OVER-BODY (windowed 22 abstract vs 1 body)

### ## Chapter Two—Terms of Welcome
- **Word count:** 3817
- **Sentence count:** 480
- **Flags:**
  - STACKED-EM-DASHES (3 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-DENSE (21 abstract terms, 70 body terms)
  - ABSTRACT-OVER-BODY (windowed 21 abstract vs 0 body)

### ## Chapter Three—The Person Freedom Failed
- **Word count:** 2190
- **Sentence count:** 283
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (2 hits)
  - ABSTRACT-OVER-BODY (windowed 11 abstract vs 1 body)

### ## Chapter Four—The Standard
- **Word count:** 3651
- **Sentence count:** 417
- **Flags:**
  - NOT-X-BUT-Y (3 hits)
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-OVER-BODY (windowed 20 abstract vs 1 body)

### ## Chapter Five—The Names They Carry
- **Word count:** 3583
- **Sentence count:** 432
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (7 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (12 hits)
  - ABSTRACT-DENSE (25 abstract terms, 78 body terms)
  - ABSTRACT-OVER-BODY (windowed 25 abstract vs 1 body)

### ## Chapter Six—The Compact
- **Word count:** 3135
- **Sentence count:** 348
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (10 hits)
  - ABSTRACT-DENSE (28 abstract terms, 46 body terms)
  - ABSTRACT-OVER-BODY (windowed 28 abstract vs 0 body)

### ## Chapter Seven—A Crown With an End
- **Word count:** 2892
- **Sentence count:** 348
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (1 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (2 hits)
  - ABSTRACT-OVER-BODY (windowed 17 abstract vs 0 body)

### ## Chapter Eight—The Cost of Consent
- **Word count:** 3205
- **Sentence count:** 431
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (4 hits)
  - ABSTRACT-OVER-BODY (windowed 16 abstract vs 0 body)

### ## Chapter Nine—The Hearing Begins
- **Word count:** 3021
- **Sentence count:** 398
- **Flags:**
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (2 hits)
  - ABSTRACT-DENSE (22 abstract terms, 64 body terms)
  - ABSTRACT-OVER-BODY (windowed 22 abstract vs 0 body)

### ## Chapter Ten—The Handover
- **Word count:** 1619
- **Sentence count:** 160
- **Flags:**
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (4 hits)
  - ABSTRACT-OVER-BODY (windowed 10 abstract vs 1 body)

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
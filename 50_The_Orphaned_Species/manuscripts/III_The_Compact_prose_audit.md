# Volume III — *The Compact* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 10
- **Total flag instances:** 28

| Flag | Chapters |
|---|---|
| TELL-NOT-SHOW | 10 |
| NOT-X-BUT-Y | 6 |
| ABSTRACT-DENSE | 5 |
| STACKED-EM-DASHES | 3 |
| ECHO-CLOSER | 3 |
| ABSTRACT-OVER-BODY | 1 |

## Chapter-level detail

### ## Chapter One—The Boat at Morning
- **Word count:** 3498
- **Sentence count:** 509
- **Flags:**
  - NOT-X-BUT-Y (3 hits)
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (9 hits)
  - ABSTRACT-DENSE (22 abstract terms, 107 body terms)

### ## Chapter Two—Terms of Welcome
- **Word count:** 3938
- **Sentence count:** 496
- **Flags:**
  - TELL-NOT-SHOW (5 hits)

### ## Chapter Three—Three Requests
- **Word count:** 2175
- **Sentence count:** 281
- **Flags:**
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (2 hits)

### ## Chapter Four—Lang's Folder
- **Word count:** 4408
- **Sentence count:** 516
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - TELL-NOT-SHOW (5 hits)
  - ABSTRACT-DENSE (21 abstract terms, 95 body terms)

### ## Chapter Five—The Names They Carry
- **Word count:** 3800
- **Sentence count:** 458
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (5 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (12 hits)
  - ABSTRACT-DENSE (26 abstract terms, 84 body terms)

### ## Chapter Six—The Compact
- **Word count:** 3707
- **Sentence count:** 444
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - TELL-NOT-SHOW (7 hits)
  - ABSTRACT-DENSE (30 abstract terms, 69 body terms)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 0 body)

### ## Chapter Seven—A Crown With an End
- **Word count:** 2945
- **Sentence count:** 353
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (3 hits)

### ## Chapter Eight—The Cost of Consent
- **Word count:** 3826
- **Sentence count:** 496
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - TELL-NOT-SHOW (5 hits)

### ## Chapter Nine—The Packet
- **Word count:** 3499
- **Sentence count:** 456
- **Flags:**
  - TELL-NOT-SHOW (1 hits)
  - ABSTRACT-DENSE (22 abstract terms, 86 body terms)

### ## Chapter Ten—The Handover
- **Word count:** 1997
- **Sentence count:** 237
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (3 hits)

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
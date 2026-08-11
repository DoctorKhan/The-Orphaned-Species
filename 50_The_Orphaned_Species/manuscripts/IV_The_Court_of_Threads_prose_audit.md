# Volume IV — *The Court of Threads* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 10
- **Total flag instances:** 35

| Flag | Chapters |
|---|---|
| STACKED-EM-DASHES | 10 |
| ABSTRACT-OVER-BODY | 10 |
| TELL-NOT-SHOW | 9 |
| ABSTRACT-DENSE | 2 |
| NOT-X-BUT-Y | 2 |
| OPEN-LIGHT-ON-BODY | 1 |
| ECHO-CLOSER | 1 |

## Chapter-level detail

### ## Chapter One—The Doors
- **Word count:** 6967
- **Sentence count:** 762
- **Flags:**
  - STACKED-EM-DASHES (7 hits)
  - TELL-NOT-SHOW (14 hits)
  - ABSTRACT-DENSE (44 abstract terms, 169 body terms)
  - ABSTRACT-OVER-BODY (windowed 44 abstract vs 0 body)

### ## Chapter Two—Present Consent
- **Word count:** 1547
- **Sentence count:** 246
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - ABSTRACT-OVER-BODY (windowed 9 abstract vs 0 body)

### ## Chapter Three—Three Rooms
- **Word count:** 2360
- **Sentence count:** 283
- **Flags:**
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-OVER-BODY (windowed 14 abstract vs 0 body)
  - OPEN-LIGHT-ON-BODY

### ## Chapter Four—What We Build
- **Word count:** 2774
- **Sentence count:** 345
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-OVER-BODY (windowed 17 abstract vs 1 body)

### ## Chapter Five—The Rumor
- **Word count:** 2117
- **Sentence count:** 290
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-OVER-BODY (windowed 20 abstract vs 0 body)

### ## Chapter Six—The Body of State
- **Word count:** 2281
- **Sentence count:** 303
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (3 hits)
  - ABSTRACT-OVER-BODY (windowed 18 abstract vs 0 body)

### ## Chapter Seven—The Two Houses
- **Word count:** 3069
- **Sentence count:** 357
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (7 hits)
  - ABSTRACT-OVER-BODY (windowed 16 abstract vs 0 body)

### ## Chapter Eight—The False Heir
- **Word count:** 2802
- **Sentence count:** 336
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-OVER-BODY (windowed 15 abstract vs 1 body)

### ## Chapter Nine—The Room Prepared
- **Word count:** 1638
- **Sentence count:** 227
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (2 hits)
  - ABSTRACT-OVER-BODY (windowed 5 abstract vs 0 body)

### ## Chapter Ten—Before the First Breath
- **Word count:** 3916
- **Sentence count:** 454
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (6 hits)
  - ABSTRACT-DENSE (21 abstract terms, 102 body terms)
  - ABSTRACT-OVER-BODY (windowed 21 abstract vs 4 body)

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
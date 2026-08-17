# Volume IV — *The Court of Threads* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 10
- **Flagged chapters:** 9
- **Total flag instances:** 17

| Flag | Chapters |
|---|---|
| TELL-NOT-SHOW | 9 |
| STACKED-EM-DASHES | 3 |
| ABSTRACT-DENSE | 1 |
| OPEN-LIGHT-ON-BODY | 1 |
| ECHO-CLOSER | 1 |
| NOT-X-BUT-Y | 1 |
| ABSTRACT-OVER-BODY | 1 |

## Chapter-level detail

### ## Chapter One—The Doors
- **Word count:** 6850
- **Sentence count:** 762
- **Flags:**
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (11 hits)
  - ABSTRACT-DENSE (42 abstract terms, 168 body terms)

### ## Chapter Two—Present Consent
- **Word count:** 1494
- **Sentence count:** 242
- **Flags:** none

### ## Chapter Three—Three Rooms
- **Word count:** 2361
- **Sentence count:** 283
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (6 hits)
  - OPEN-LIGHT-ON-BODY

### ## Chapter Four—What We Build
- **Word count:** 2845
- **Sentence count:** 351
- **Flags:**
  - TELL-NOT-SHOW (6 hits)

### ## Chapter Five—The Rumor
- **Word count:** 2074
- **Sentence count:** 289
- **Flags:**
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (6 hits)

### ## Chapter Six—The Statement
- **Word count:** 2279
- **Sentence count:** 303
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - TELL-NOT-SHOW (3 hits)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 1 body)

### ## Chapter Seven—The Two Houses
- **Word count:** 3062
- **Sentence count:** 357
- **Flags:**
  - TELL-NOT-SHOW (7 hits)

### ## Chapter Eight—The Succession Debate
- **Word count:** 2800
- **Sentence count:** 336
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (4 hits)

### ## Chapter Nine—The Room Prepared
- **Word count:** 1638
- **Sentence count:** 227
- **Flags:**
  - TELL-NOT-SHOW (2 hits)

### ## Chapter Ten—Before the First Breath
- **Word count:** 4113
- **Sentence count:** 492
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
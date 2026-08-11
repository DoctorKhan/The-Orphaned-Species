# Volume I — *The Breach* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 13
- **Flagged chapters:** 13
- **Total flag instances:** 45

| Flag | Chapters |
|---|---|
| STACKED-EM-DASHES | 13 |
| TELL-NOT-SHOW | 12 |
| ABSTRACT-OVER-BODY | 10 |
| NOT-X-BUT-Y | 7 |
| ECHO-CLOSER | 1 |
| ABSTRACT-DENSE | 1 |
| OPEN-LIGHT-ON-BODY | 1 |

## Chapter-level detail

### ## Chapter One—The Hour That Belongs to No One
- **Word count:** 5865
- **Sentence count:** 488
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (36 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (22 hits)
  - ABSTRACT-DENSE (28 abstract terms, 272 body terms)
  - ABSTRACT-OVER-BODY (windowed 28 abstract vs 2 body)

### ## Chapter Two—His Hand
- **Word count:** 9589
- **Sentence count:** 736
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (63 hits)
  - TELL-NOT-SHOW (39 hits)
  - ABSTRACT-OVER-BODY (windowed 19 abstract vs 0 body)

### ## Chapter Three—What Didn't Die
- **Word count:** 2472
- **Sentence count:** 214
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (11 hits)
  - TELL-NOT-SHOW (7 hits)

### ## Chapter Four—The Passage
- **Word count:** 1976
- **Sentence count:** 176
- **Flags:**
  - STACKED-EM-DASHES (8 hits)
  - TELL-NOT-SHOW (2 hits)
  - ABSTRACT-OVER-BODY (windowed 7 abstract vs 0 body)

### ## Chapter Five—The Field That Counts
- **Word count:** 3677
- **Sentence count:** 311
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (14 hits)
  - TELL-NOT-SHOW (13 hits)
  - ABSTRACT-OVER-BODY (windowed 7 abstract vs 2 body)

### ## Chapter Six—First Witness
- **Word count:** 1492
- **Sentence count:** 131
- **Flags:**
  - STACKED-EM-DASHES (7 hits)
  - TELL-NOT-SHOW (4 hits)
  - ABSTRACT-OVER-BODY (windowed 5 abstract vs 1 body)

### ## Chapter Seven—The Forming Line
- **Word count:** 2508
- **Sentence count:** 198
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (11 hits)
  - TELL-NOT-SHOW (7 hits)
  - ABSTRACT-OVER-BODY (windowed 13 abstract vs 2 body)

### ## Chapter Eight—Ila's Hands
- **Word count:** 1448
- **Sentence count:** 128
- **Flags:**
  - STACKED-EM-DASHES (6 hits)
  - TELL-NOT-SHOW (1 hits)
  - ABSTRACT-OVER-BODY (windowed 7 abstract vs 2 body)

### ## Chapter Nine—Two Teams
- **Word count:** 1449
- **Sentence count:** 104
- **Flags:**
  - STACKED-EM-DASHES (7 hits)
  - TELL-NOT-SHOW (7 hits)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 1 body)
  - OPEN-LIGHT-ON-BODY

### ## Chapter Ten—People Over Evidence
- **Word count:** 1804
- **Sentence count:** 176
- **Flags:**
  - STACKED-EM-DASHES (7 hits)

### ## Chapter Eleven—Human Doors
- **Word count:** 3938
- **Sentence count:** 421
- **Flags:**
  - STACKED-EM-DASHES (9 hits)
  - TELL-NOT-SHOW (11 hits)
  - ABSTRACT-OVER-BODY (windowed 11 abstract vs 1 body)

### ## Chapter Twelve—The Tree with No Top
- **Word count:** 2077
- **Sentence count:** 224
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (7 hits)

### ## Chapter Thirteen—The Living Route
- **Word count:** 3989
- **Sentence count:** 465
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (10 hits)
  - TELL-NOT-SHOW (13 hits)
  - ABSTRACT-OVER-BODY (windowed 15 abstract vs 2 body)

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
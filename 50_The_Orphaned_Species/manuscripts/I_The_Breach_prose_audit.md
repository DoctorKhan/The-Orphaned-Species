# Volume I — *The Breach* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 13
- **Flagged chapters:** 13
- **Total flag instances:** 49

| Flag | Chapters |
|---|---|
| SHORT-PARA-RUN | 13 |
| TELL-NOT-SHOW | 12 |
| STACKED-EM-DASHES | 11 |
| NOT-X-BUT-Y | 6 |
| TIDY-COMPARISON | 3 |
| ECHO-CLOSER | 2 |
| SUMMARY-OPEN | 1 |
| OPEN-LIGHT-ON-BODY | 1 |

## Chapter-level detail

### ## Chapter One—The Hour That Belongs to No One
- **Word count:** 5529
- **Sentence count:** 489
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (7 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (15 hits)
  - SUMMARY-OPEN (1 hits)
  - SHORT-PARA-RUN (4 run(s) of 3+ short paragraphs)

### ## Chapter Two—His Hand
- **Word count:** 10482
- **Sentence count:** 912
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - TELL-NOT-SHOW (43 hits)
  - SHORT-PARA-RUN (8 run(s) of 3+ short paragraphs)

### ## Chapter Three—What Didn't Die
- **Word count:** 2486
- **Sentence count:** 217
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (8 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (6 hits)
  - SHORT-PARA-RUN (3 run(s) of 3+ short paragraphs)

### ## Chapter Four—The Passage
- **Word count:** 1987
- **Sentence count:** 176
- **Flags:**
  - STACKED-EM-DASHES (3 hits)
  - TELL-NOT-SHOW (2 hits)
  - SHORT-PARA-RUN (3 run(s) of 3+ short paragraphs)

### ## Chapter Five—The Field That Counts
- **Word count:** 3806
- **Sentence count:** 327
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - STACKED-EM-DASHES (7 hits)
  - TELL-NOT-SHOW (13 hits)
  - SHORT-PARA-RUN (2 run(s) of 3+ short paragraphs)

### ## Chapter Six—First Witness
- **Word count:** 1238
- **Sentence count:** 112
- **Flags:**
  - STACKED-EM-DASHES (2 hits)
  - TELL-NOT-SHOW (2 hits)
  - SHORT-PARA-RUN (1 run(s) of 3+ short paragraphs)

### ## Chapter Seven—The Forming Line
- **Word count:** 2252
- **Sentence count:** 183
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - TIDY-COMPARISON (1 hits)
  - STACKED-EM-DASHES (8 hits)
  - TELL-NOT-SHOW (5 hits)
  - SHORT-PARA-RUN (3 run(s) of 3+ short paragraphs)

### ## Chapter Eight—Ila's Hands
- **Word count:** 1443
- **Sentence count:** 127
- **Flags:**
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (1 hits)
  - SHORT-PARA-RUN (2 run(s) of 3+ short paragraphs)

### ## Chapter Nine—Two Teams
- **Word count:** 1383
- **Sentence count:** 103
- **Flags:**
  - TIDY-COMPARISON (1 hits)
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (6 hits)
  - OPEN-LIGHT-ON-BODY
  - SHORT-PARA-RUN (3 run(s) of 3+ short paragraphs)

### ## Chapter Ten—People Over Evidence
- **Word count:** 1902
- **Sentence count:** 185
- **Flags:**
  - STACKED-EM-DASHES (6 hits)
  - SHORT-PARA-RUN (4 run(s) of 3+ short paragraphs)

### ## Chapter Eleven—Human Doors
- **Word count:** 3993
- **Sentence count:** 425
- **Flags:**
  - STACKED-EM-DASHES (4 hits)
  - TELL-NOT-SHOW (11 hits)
  - SHORT-PARA-RUN (16 run(s) of 3+ short paragraphs)

### ## Chapter Twelve—The Tree with No Top
- **Word count:** 2041
- **Sentence count:** 221
- **Flags:**
  - TIDY-COMPARISON (1 hits)
  - STACKED-EM-DASHES (1 hits)
  - TELL-NOT-SHOW (7 hits)
  - SHORT-PARA-RUN (9 run(s) of 3+ short paragraphs)

### ## Chapter Thirteen—The Living Route
- **Word count:** 3066
- **Sentence count:** 418
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - TELL-NOT-SHOW (1 hits)
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
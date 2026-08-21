# Volume I — *The Breach* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 25
- **Flagged chapters:** 10
- **Total flag instances:** 14

| Flag | Chapters |
|---|---|
| STACKED-EM-DASHES | 8 |
| NOT-X-BUT-Y | 4 |
| ECHO-CLOSER | 2 |

## Chapter-level detail

### ## Chapter 1—The Hour That Belongs to No One [PLACEHOLDER]
- **Word count:** 2258
- **Sentence count:** 195
- **Flags:** none

### ## Chapter 2—Saturday Departure [SPLIT-FROM: Ch 1]
- **Word count:** 2255
- **Sentence count:** 195
- **Flags:** none

### ## Chapter 3—His Hand / Checkpoints and the Stack [PLACEHOLDER]
- **Word count:** 16
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 4—Singapore Intake [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 5—What Didn't Die [SPLIT-FROM: Ch 3]
- **Word count:** 3285
- **Sentence count:** 318
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 6—Breach Recovery [SPLIT-FROM: Ch 3]
- **Word count:** 3284
- **Sentence count:** 318
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 7—The Passage [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 8—Departure and Wat [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 9—The Field That Counts [SPLIT-FROM: Ch 5]
- **Word count:** 3685
- **Sentence count:** 373
- **Flags:**
  - NOT-X-BUT-Y (1 hits)

### ## Chapter 10—Grounding Arrival [SPLIT-FROM: Ch 5]
- **Word count:** 3683
- **Sentence count:** 373
- **Flags:**
  - NOT-X-BUT-Y (1 hits)

### ## Chapter 11—Midpoint: First Witness [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 12—Witness Ground [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 13—The Forming Line [SPLIT-FROM: Ch 7]
- **Word count:** 2208
- **Sentence count:** 198
- **Flags:**
  - STACKED-EM-DASHES (2 hits)

### ## Chapter 14—The Cooperative Edge [SPLIT-FROM: Ch 7]
- **Word count:** 2208
- **Sentence count:** 198
- **Flags:**
  - STACKED-EM-DASHES (2 hits)

### ## Chapter 15—Ila's Hands [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 16—Hands and Repair [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 17—Two Teams [SPLIT-FROM: Ch 9]
- **Word count:** 3271
- **Sentence count:** 291
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 18—Civilian Response [SPLIT-FROM: Ch 9]
- **Word count:** 3271
- **Sentence count:** 291
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 19—People Over Evidence [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 20—Evidence Burn [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 21—Human Doors [SPLIT-FROM: Ch 11]
- **Word count:** 2519
- **Sentence count:** 223
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (6 hits)
  - ECHO-CLOSER (1 hits)

### ## Chapter 22—The Laos Border [SPLIT-FROM: Ch 11]
- **Word count:** 2520
- **Sentence count:** 223
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - STACKED-EM-DASHES (6 hits)
  - ECHO-CLOSER (1 hits)

### ## Chapter 23—The Tree with No Top [PLACEHOLDER]
- **Word count:** 14
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 24—Conservation Campus [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 25—The Living Route [SPLIT-FROM: Ch 13]
- **Word count:** 2061
- **Sentence count:** 179
- **Flags:** none

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
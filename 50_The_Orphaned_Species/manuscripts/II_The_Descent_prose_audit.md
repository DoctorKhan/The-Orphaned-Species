# Volume II — *The Descent* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 25
- **Flagged chapters:** 10
- **Total flag instances:** 12

| Flag | Chapters |
|---|---|
| NOT-X-BUT-Y | 7 |
| STACKED-EM-DASHES | 3 |
| ABSTRACT-DENSE | 2 |

## Chapter-level detail

### ## Chapter 1—What Came Home [PLACEHOLDER]
- **Word count:** 3086
- **Sentence count:** 354
- **Flags:**
  - NOT-X-BUT-Y (1 hits)

### ## Chapter 2—The Westbound Packet [SPLIT-FROM: Ch 1]
- **Word count:** 3088
- **Sentence count:** 354
- **Flags:**
  - NOT-X-BUT-Y (1 hits)

### ## Chapter 3—The Folly [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 4—The Archive Exit [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 5—The Buried Instrument [SPLIT-FROM: Ch 3]
- **Word count:** 3998
- **Sentence count:** 479
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - ABSTRACT-DENSE (31 abstract terms, 120 body terms)

### ## Chapter 6—The Clinic Approach [SPLIT-FROM: Ch 3]
- **Word count:** 3998
- **Sentence count:** 479
- **Flags:**
  - NOT-X-BUT-Y (2 hits)
  - ABSTRACT-DENSE (31 abstract terms, 120 body terms)

### ## Chapter 7—Laurel Crossing [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 8—The Healer's Clinic [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 9—The Holding Entry [SPLIT-FROM: Ch 5]
- **Word count:** 4645
- **Sentence count:** 610
- **Flags:**
  - NOT-X-BUT-Y (3 hits)

### ## Chapter 10—The Midpoint Revelation [SPLIT-FROM: Ch 5]
- **Word count:** 4645
- **Sentence count:** 610
- **Flags:**
  - NOT-X-BUT-Y (3 hits)

### ## Chapter 11—Ring and Romance Cost [SPLIT-FROM: Ch 5]
- **Word count:** 4646
- **Sentence count:** 610
- **Flags:**
  - NOT-X-BUT-Y (3 hits)

### ## Chapter 12—The Changing Map [SPLIT-FROM: Ch 6]
- **Word count:** 14
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 13—The Broken-Line Church [SPLIT-FROM: Ch 6]
- **Word count:** 14
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 14—The Stray Settlement [SPLIT-FROM: Ch 6]
- **Word count:** 14
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 15—The Riddling Ground [SPLIT-FROM: Ch 7]
- **Word count:** 3702
- **Sentence count:** 532
- **Flags:** none

### ## Chapter 16—Callum Recovery and Renewal [SPLIT-FROM: Ch 7]
- **Word count:** 3703
- **Sentence count:** 532
- **Flags:** none

### ## Chapter 17—The Transfer-Records Discovery [SPLIT-FROM: Ch 7]
- **Word count:** 3702
- **Sentence count:** 532
- **Flags:** none

### ## Chapter 18—The Corridor Signal [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 19—One-Way Contact [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 20—The Transmission Station [SPLIT-FROM: Ch 9]
- **Word count:** 3202
- **Sentence count:** 561
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 21—The Instrument Cap [SPLIT-FROM: Ch 9]
- **Word count:** 3202
- **Sentence count:** 561
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 22—The Avebury Approach [SPLIT-FROM: Ch 9]
- **Word count:** 3202
- **Sentence count:** 561
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 23—Release [SPLIT-FROM: Ch 10]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 24—The Release Choice [SPLIT-FROM: Ch 10]
- **Word count:** 14
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 25—Aftermath and Book III Ignition [SPLIT-FROM: Ch 10]
- **Word count:** 15
- **Sentence count:** 1
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
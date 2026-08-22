# Volume III — *The Compact* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 15
- **Flagged chapters:** 11
- **Total flag instances:** 25

| Flag | Chapters |
|---|---|
| SHORT-PARA-RUN | 9 |
| ABSTRACT-DENSE | 4 |
| OPEN-LIGHT-ON-BODY | 4 |
| ECHO-CLOSER | 3 |
| STACKED-EM-DASHES | 2 |
| TELL-NOT-SHOW | 1 |
| ABSTRACT-OVER-BODY | 1 |
| IDENTICAL-PARA-OPENING | 1 |

## Chapter-level detail

### ## Chapter 1—The Boat at Morning [PLACEHOLDER]
- **Word count:** 3459
- **Sentence count:** 509
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - ABSTRACT-DENSE (22 abstract terms, 103 body terms)
  - SHORT-PARA-RUN (27 run(s) of 3+ short paragraphs)

### ## Chapter 3—The First Sponsorship [PLACEHOLDER]
- **Word count:** 3939
- **Sentence count:** 496
- **Flags:**
  - SHORT-PARA-RUN (22 run(s) of 3+ short paragraphs)

### ## Chapter 5—The Artifact Delivery [SPLIT-FROM: Ch 3]
- **Word count:** 2179
- **Sentence count:** 281
- **Flags:**
  - ECHO-CLOSER (1 hits)
  - SHORT-PARA-RUN (13 run(s) of 3+ short paragraphs)

### ## Chapter 7—The Repair Dock Evening [PLACEHOLDER]
- **Word count:** 4416
- **Sentence count:** 517
- **Flags:**
  - ABSTRACT-DENSE (21 abstract terms, 95 body terms)
  - SHORT-PARA-RUN (26 run(s) of 3+ short paragraphs)

### ## Chapter 9—The Sideways Record [SPLIT-FROM: Ch 5]
- **Word count:** 8367
- **Sentence count:** 991
- **Flags:**
  - STACKED-EM-DASHES (6 hits)
  - ECHO-CLOSER (1 hits)
  - TELL-NOT-SHOW (1 hits)
  - ABSTRACT-DENSE (59 abstract terms, 173 body terms)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 0 body)
  - OPEN-LIGHT-ON-BODY
  - SHORT-PARA-RUN (58 run(s) of 3+ short paragraphs)

### ## Chapter 13—Qiao's Testimony and the Survivor [SPLIT-FROM: Ch 7]
- **Word count:** 2929
- **Sentence count:** 353
- **Flags:**
  - ECHO-CLOSER (1 hits)
  - SHORT-PARA-RUN (18 run(s) of 3+ short paragraphs)
  - IDENTICAL-PARA-OPENING (1 run(s) of 3+ same-shape openings)

### ## Chapter 15—The Signing and the Shed Fire [PLACEHOLDER]
- **Word count:** 3811
- **Sentence count:** 494
- **Flags:**
  - OPEN-LIGHT-ON-BODY
  - SHORT-PARA-RUN (16 run(s) of 3+ short paragraphs)

### ## Chapter 17—A Crown With an End [PLACEHOLDER]
- **Word count:** 3504
- **Sentence count:** 456
- **Flags:**
  - ABSTRACT-DENSE (22 abstract terms, 86 body terms)
  - SHORT-PARA-RUN (17 run(s) of 3+ short paragraphs)

### ## Chapter 19—Gutter Clearing and the Work Song [PLACEHOLDER]
- **Word count:** 9
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 20—The Corridor Order [SPLIT-FROM: Ch 13]
- **Word count:** 309
- **Sentence count:** 31
- **Flags:**
  - SHORT-PARA-RUN (1 run(s) of 3+ short paragraphs)

### ## Chapter 21—The Cost of Consent [PLACEHOLDER]
- **Word count:** 22
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 22—The Drone-Strike Cost [SPLIT-FROM: Ch 15]
- **Word count:** 274
- **Sentence count:** 27
- **Flags:** none

### ## Chapter 23—The Hearing Room and the Side Room [PLACEHOLDER]
- **Word count:** 25
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 24—The Hearing Begins [SPLIT-FROM: Ch 17]
- **Word count:** 279
- **Sentence count:** 25
- **Flags:**
  - OPEN-LIGHT-ON-BODY

### ## Chapter 25—The Handover [SPLIT-FROM: Ch 18]
- **Word count:** 289
- **Sentence count:** 31
- **Flags:**
  - OPEN-LIGHT-ON-BODY

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
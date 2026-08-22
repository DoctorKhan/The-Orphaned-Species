# Volume IV — *The Court of Threads* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 16
- **Flagged chapters:** 10
- **Total flag instances:** 19

| Flag | Chapters |
|---|---|
| SHORT-PARA-RUN | 10 |
| STACKED-EM-DASHES | 3 |
| ABSTRACT-DENSE | 1 |
| IDENTICAL-PARA-OPENING | 1 |
| OPEN-LIGHT-ON-BODY | 1 |
| ABSTRACT-DISTANCE | 1 |
| ECHO-CLOSER | 1 |
| ABSTRACT-OVER-BODY | 1 |

## Chapter-level detail

### ## Chapter 1—The Doors [PLACEHOLDER]
- **Word count:** 7288
- **Sentence count:** 787
- **Flags:**
  - STACKED-EM-DASHES (2 hits)
  - ABSTRACT-DENSE (44 abstract terms, 187 body terms)
  - SHORT-PARA-RUN (33 run(s) of 3+ short paragraphs)
  - IDENTICAL-PARA-OPENING (2 run(s) of 3+ same-shape openings)

### ## Chapter 3—Three Rooms [PLACEHOLDER]
- **Word count:** 1512
- **Sentence count:** 238
- **Flags:**
  - SHORT-PARA-RUN (8 run(s) of 3+ short paragraphs)

### ## Chapter 5—The Rumor [SPLIT-FROM: Ch 3]
- **Word count:** 2361
- **Sentence count:** 283
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - OPEN-LIGHT-ON-BODY
  - SHORT-PARA-RUN (12 run(s) of 3+ short paragraphs)

### ## Chapter 7—The Two Houses [PLACEHOLDER]
- **Word count:** 2952
- **Sentence count:** 361
- **Flags:**
  - ABSTRACT-DISTANCE (1 hits)
  - SHORT-PARA-RUN (11 run(s) of 3+ short paragraphs)

### ## Chapter 9—The Room Prepared [SPLIT-FROM: Ch 5]
- **Word count:** 2081
- **Sentence count:** 289
- **Flags:**
  - ECHO-CLOSER (1 hits)
  - SHORT-PARA-RUN (8 run(s) of 3+ short paragraphs)

### ## Chapter 11—The Stag Teacher [PLACEHOLDER]
- **Word count:** 2312
- **Sentence count:** 307
- **Flags:**
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 1 body)
  - SHORT-PARA-RUN (14 run(s) of 3+ short paragraphs)

### ## Chapter 13—The Nacre Audit [SPLIT-FROM: Ch 7]
- **Word count:** 3389
- **Sentence count:** 377
- **Flags:**
  - SHORT-PARA-RUN (17 run(s) of 3+ short paragraphs)

### ## Chapter 15—The Recruitment Hearing [PLACEHOLDER]
- **Word count:** 2801
- **Sentence count:** 336
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - SHORT-PARA-RUN (14 run(s) of 3+ short paragraphs)

### ## Chapter 17—The Southern Canopy [SPLIT-FROM: Ch 9]
- **Word count:** 1706
- **Sentence count:** 231
- **Flags:**
  - SHORT-PARA-RUN (6 run(s) of 3+ short paragraphs)

### ## Chapter 19—The False Heir Draft [PLACEHOLDER]
- **Word count:** 7
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 20—The Hospital Conversation [PLACEHOLDER]
- **Word count:** 6
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 21—The Continuity Extension File [SPLIT-FROM: Ch 11]
- **Word count:** 24
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 22—The Praetorian Demand [SPLIT-FROM: Ch 11]
- **Word count:** 1195
- **Sentence count:** 136
- **Flags:**
  - SHORT-PARA-RUN (6 run(s) of 3+ short paragraphs)

### ## Chapter 23—The Labor Inversion [PLACEHOLDER]
- **Word count:** 21
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 24—The Sideways Four Seconds [SPLIT-FROM: Ch 13]
- **Word count:** 24
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 25—The Flight Departure [PLACEHOLDER]
- **Word count:** 21
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
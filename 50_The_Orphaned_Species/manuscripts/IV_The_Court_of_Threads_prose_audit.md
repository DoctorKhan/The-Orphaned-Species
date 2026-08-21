# Volume IV — *The Court of Threads* — Prose Audit
*Generated from on-disk files. Rerun after prose revisions.*

> **Generated:** current as of last script run.
> Treat as draft until manual review.

## Summary
- **Chapters audited:** 25
- **Flagged chapters:** 9
- **Total flag instances:** 14

| Flag | Chapters |
|---|---|
| STACKED-EM-DASHES | 6 |
| ABSTRACT-DENSE | 2 |
| LONG-PARAGRAPH | 2 |
| ECHO-CLOSER | 2 |
| NOT-X-BUT-Y | 1 |
| ABSTRACT-OVER-BODY | 1 |

## Chapter-level detail

### ## Chapter 1—The Doors [PLACEHOLDER]
- **Word count:** 2923
- **Sentence count:** 275
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 2—Present Consent [SPLIT-FROM: Ch 1]
- **Word count:** 2925
- **Sentence count:** 275
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 3—Three Rooms [PLACEHOLDER]
- **Word count:** 11
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 4—What We Build [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 5—The Rumor [SPLIT-FROM: Ch 3]
- **Word count:** 1815
- **Sentence count:** 196
- **Flags:** none

### ## Chapter 6—The Body of State [SPLIT-FROM: Ch 3]
- **Word count:** 1817
- **Sentence count:** 196
- **Flags:** none

### ## Chapter 7—The Two Houses [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 8—The False Heir [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 9—The Room Prepared [SPLIT-FROM: Ch 5]
- **Word count:** 2564
- **Sentence count:** 320
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 10—Before the First Breath [SPLIT-FROM: Ch 5]
- **Word count:** 2565
- **Sentence count:** 320
- **Flags:**
  - STACKED-EM-DASHES (1 hits)

### ## Chapter 11—The Stag Teacher [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 12—The Five Forms Week [PLACEHOLDER]
- **Word count:** 13
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 13—The Nacre Audit [SPLIT-FROM: Ch 7]
- **Word count:** 3854
- **Sentence count:** 521
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - ABSTRACT-DENSE (27 abstract terms, 69 body terms)
  - LONG-PARAGRAPH (1 paragraph(s) over 250 words)

### ## Chapter 14—The Cloister Risk Score [SPLIT-FROM: Ch 7]
- **Word count:** 3855
- **Sentence count:** 521
- **Flags:**
  - STACKED-EM-DASHES (1 hits)
  - ABSTRACT-DENSE (27 abstract terms, 69 body terms)
  - LONG-PARAGRAPH (1 paragraph(s) over 250 words)

### ## Chapter 15—The Recruitment Hearing [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 16—The Ilyara Boundary [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 17—The Southern Canopy [SPLIT-FROM: Ch 9]
- **Word count:** 2948
- **Sentence count:** 361
- **Flags:** none

### ## Chapter 18—The Work-Song Class [SPLIT-FROM: Ch 9]
- **Word count:** 2948
- **Sentence count:** 361
- **Flags:** none

### ## Chapter 19—The False Heir Draft [PLACEHOLDER]
- **Word count:** 13
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 20—The Hospital Conversation [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 21—The Continuity Extension File [SPLIT-FROM: Ch 11]
- **Word count:** 2079
- **Sentence count:** 289
- **Flags:**
  - ECHO-CLOSER (1 hits)

### ## Chapter 22—The Praetorian Demand [SPLIT-FROM: Ch 11]
- **Word count:** 2078
- **Sentence count:** 289
- **Flags:**
  - ECHO-CLOSER (1 hits)

### ## Chapter 23—The Labor Inversion [PLACEHOLDER]
- **Word count:** 12
- **Sentence count:** 1
- **Flags:** none

### ## Chapter 24—The Sideways Four Seconds [SPLIT-FROM: Ch 13]
- **Word count:** 2323
- **Sentence count:** 307
- **Flags:**
  - NOT-X-BUT-Y (1 hits)
  - ABSTRACT-OVER-BODY (windowed 4 abstract vs 1 body)

### ## Chapter 25—The Flight Departure [PLACEHOLDER]
- **Word count:** 11
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
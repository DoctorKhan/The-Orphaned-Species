# The Orphaned Species — Agent Instructions

Read `SERIES_STRUCTURE.md` (repo root) first if unsure how many books this series has, what's in each one, or what a filename refers to — it is the authoritative volume map.

## Writing style — applies to every document, not just manuscript prose

Before writing or editing any prose paragraph in this repo — bible files, lock notes, companion volumes, beatsheets, thesis documents, and manuscript chapters alike — read `50_The_Orphaned_Species/14_literary_speculative_thriller_style_guide.md` § *Generic-cadence / AI-pattern checklist* and § *Human-prose lock*.

The single most common failure, and the reason this note exists: reflexive **"it's not X, it's Y"** / **"not X but Y"** contrastive templates, used as a default sentence shape rather than because a given contrast actually earns its place. It is easy to write several of these per paragraph without noticing. Also watch for:

- Undifferentiated triads and litany-lists reached for out of habit rather than because three items are genuinely what's there.
- Echo-closers — a final sentence that just restates an earlier image to sound like an ending, without costing or revealing anything new.
- Rhythm drift into generic "literary" cadence via stacked em dashes and colon-heavy constructions.
- Reflexive bold-emphasis used as a substitute for the sentence actually landing on its own.

**These checks apply to lock-note and doctrine prose exactly as much as to fiction.** Bureaucratic-sounding "LOCKED" paragraphs, thesis passages, and beatsheet cards are not exempt from craft scrutiny just because they read as reference material rather than narrative — if anything, AI-cadence drift is more likely to go unnoticed there. Before saving any new prose paragraph anywhere in this repo, run it past the checklist the same way a chapter would be.

## Prose discipline — mandatory anti-cadence checks

Before accepting any rewritten or drafted prose, verify all of the following:

1. **No abstraction without a body.** Abstract nouns ("the obligation," "the debt," "the procedure") are forbidden until they have been touched, smelled, or physically reacted to on-page. Replace with a concrete noun from the viewpoint character's world.
2. **No repetition as structure.** If a sentence needs a parallel item to balance its rhythm, the item must be new and concrete, not a repeated abstract concept introduced for the sake of the sentence shape.
3. **No tell-not-show abstractions in narration.** Cut phrases like "a boy who needs a wage or a place to sleep" when the same beat can be delivered through a specific action, object, or bodily sensation.
4. **No faux-scriptural closers.** A final sentence that restates the paragraph's theme without costing or revealing anything new is an echo-closer. End on the last sentence that actually changed something.
5. **No "not X but Y" as default shape.** Hedge-contrast constructions are allowed only when the contrast changes what the reader can do with the next sentence.
6. **No stacked em dashes and colon-heavy constructions as default register.** Long cumulative sentences must be checked against the surrounding scene's rhythm before being accepted.
7. **Opening-image lock.** Chapter and scene opens must lead with physical scene and action. No appended interpretation, no simile that explains permanence or theme in the opening paragraph, no mystification before observation.
8. **Revision test.** Highlight every sentence that tells the reader what the previous sentence meant. Delete it first. Restore only the information the scene cannot function without, in the viewpoint character's own vocabulary.
9. **Whole-document frequency check — do this last, mechanically, not just while drafting.** An instance that looks earned in isolation can still be a tic in aggregate. Before calling any chapter or long passage done, actually search the full file (`grep -n` for "not X, ", "not.*but", stacked em dashes, colon-led inventory lines) rather than relying on having noticed each one while writing. Apply a frequency ceiling: no more than one or two instances of any single flagged construction per chapter, full stop — if a search turns up more, cut down to the strongest instance instead of defending each one on its own merits. This also catches structural repeats a keyword search misses: the same sentence *architecture* (e.g. a "Behind X: ... In his pocket: ..." inventory) reused twice in one chapter is the same failure as a repeated phrase, even with different words in it — read the full document once, specifically hunting for a structure repeating on itself, separate from the line-by-line drafting pass.

If any item above flags, fix it before saving.

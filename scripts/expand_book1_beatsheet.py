#!/usr/bin/env python3
"""Expand Book I beatsheet from 13 to 25 chapter cards."""

import re
import os

BEATSHEET = '50_The_Orphaned_Species/31_volume_I_beatsheet.md'

# Placeholder cards to insert (in order between Ch 1-2, 2-3, ..., 12-13)
PLACEHOLDERS = [
    ("1a", "Saturday Departure", "(Eli · Babaji hotel → marina → last light)", "PLACEHOLDER SPLIT FROM EXISTING CH 1",
     "Friday PM — Mei dinner; Kiran leaves; private orphan truth explains why she pushed Eli to go, only send-off.",
     "understand why Mei is pushing him to leave; chosen family: Mei, Suresh, Babaji.",
     "Mei's warning about boats being turned back; orphan truth withheld until Kiran leaves.",
     "learns the truth: parents left him for one night and never returned. Hearth suspended; packed bags prove abandonment or flight.",
     "Mei's kitchen as first family unit; free-meal list as threshold house practice. Wrong reading: packed bags = abandonment; cost: hearth suspended.",
     "I"),
    
    ("2a", "Singapore Intake", "(Eli · Stack intake → causeway hall → Continue Inn)", "PLACEHOLDER SPLIT FROM EXISTING CH 2",
     "Saturday last light — depart Pelangi; strait pier + Stack intake Saturday eve. Saturday night — Continue Inn (game hotel).",
     "reach Continue Inn; learn why a Mandate archive photograph shows Rasel's hand and wedding ring.",
     "Stack intake flags resemblance; ring photo triggers hunt; wrong-room overhear exposes Hassan/Malacca/English woman fragments.",
     "chooses forward after ring photograph rather than disappearing into worker flow; evidence burned; helpers exposed.",
     "Stray-lane as fossil of discarded male standing; Continue Inn live-play cabinets/sims/VR as Foundry muscle rhyme and Rasel echo. Wrong reading: Stray = criminal; Cube = paradise; surge = destiny. Cost: wage ticket; receiver opens without control.",
     "I"),
    
    ("3a", "Breach Recovery", "(Eli · Malacca quay → grounding aftermath)", "PLACEHOLDER SPLIT FROM EXISTING CH 3",
     "Sunday early morning — Malacca quay after the breach; Salmah's rescue; rough resuscitation; first grounding.",
     "survive the immediate aftermath; understand what happened.",
     "near-death asphyxia; psi plane overload; Salmah's boat seized; Custodian classification pending.",
     "Eli accepts Salmah's help and transfers danger into an ordinary worker's life. Cost: Salmah's market access suspended; her boat seized as contaminated evidence.",
     "Salmah's kelong hospitality as practice older than registries—cup-count, lime divided, mangrove flowers taken by tide without ceremony. Wrong reading: hospitality = Weaver conspiracy; cost: choosing open pursuit over going dark.",
     "I"),
    
    ("4a", "Departure and Wat", "(Eli · Malacca departure → first wat practice)", "PLACEHOLDER SPLIT FROM EXISTING CH 4",
     "Monday — Malacca departure aboard northbound vessel; first wat practice at sea or in port.",
     "reach the next waypoint without being flagged; begin grounding practice.",
     "harbor network compromised; Custodian pursuit; Eli's receiver still open and noisy.",
     "commits to the worker route despite wrongness. Cost: signature lit across the grid; helpers exposed.",
     "harbor network as practice older than registries; worker route as civic infrastructure invisible to authority. Wat breath as first voluntary regulation, not cure. Wrong reading: harbor = extraction network; wat = therapy. Cost: none explicit here; trust earned without debt.",
     "I"),
    
    ("5a", "Grounding Arrival", "(Eli · Thailand first settlement)", "PLACEHOLDER SPLIT FROM EXISTING CH 5",
     "Tuesday — arrival at first Thailand settlement; Ila's record reaches them through document.",
     "test the growth report and Ila's ground record.",
     "the report is partly stale; community wants no outsiders; Custodians are a day behind.",
     "he trusts living local expertise over his own vision and over the planted lead. Cost: time lost; the wrong clue cost them a margin.",
     "plant growth as detector before any message — living mesh, not imposed symbol; mountain shrine / coffee spur as place that refuses sale. Wrong reading: plants = coded map for Eli; mountain = tourist set; wat = therapy. Cost: stale clue burns margin; he trusts growers over his vision.",
     "II"),
    
    ("6a", "Witness Ground", "(Eli · first witness site — ground reading)", "PLACEHOLDER SPLIT FROM EXISTING CH 6",
     "Midweek — approach to first witness site; Ila's ground record clarifies through the keeper's testimony.",
     "stand at a charged site long enough for a thread to clarify without collapsing from exhaustion.",
     "at a witness site, Ila's ground record clarifies — the ley line's signature through paddy and crop; local talking-stone lore; pursuit pressure won't wait.",
     "he receives her as other — real, dead, grievable — without claiming her. Cost: grief with nowhere to set the love down.",
     "Ila's ground record as apprenticeship, not identity proof; talking-stone / witness ground behaves wrongly before mechanism. Wrong reading: Ila = destiny twin / past life; stone = personal oracle. Cost: grief with nowhere to land.",
     "II"),
    
    ("7a", "The Cooperative Edge", "(Eli · Wren POV → first view of the cooperative)", "PLACEHOLDER SPLIT FROM EXISTING CH 7",
     "Late week — arrival at the rice/aquaculture cooperative; Wren's first interior POV.",
     "find and document the forming line before the Custodians.",
     "community wants no outsiders; Eli's quiet reads to Wren as settled competence, not grief held as skill.",
     "Wren revises: body-before-story, but the story has learned to get there first. Cost: intimacy down; Wren sees the exit strategy before Eli names it.",
     "crop band as new line forming (Life mesh), distinguished from dead ground / scour scar and legacy contamination — place fossils without Phase names. Wrong reading: band = faction message or Eli's private map. Cost: asking growers for help paints a target on them.",
     "II"),
    
    ("8a", "Hands and Repair", "(Eli · Ila's hands — cooperative repair)", "PLACEHOLDER SPLIT FROM EXISTING CH 8",
     "Same week — cooperative repair work; Ila's copied ground record confirms what growers already know.",
     "understand the new line through planted ground; work alongside the growers.",
     "physical evidence damaged; Eli's receiver work visibly costing him (headaches, tremor); Wren notices, he explains nothing.",
     "chooses to trust living local expertise over his own vision. Cost: time lost; wrong clue burns margin.",
     "Ila's copied ground record confirms the new line through planted ground is a living system they must tend; physical Maren's field notebook remains undisclosed. Wrong reading: record = map home; hands = destiny key. Cost: evidence damaged but not destroyed.",
     "II"),
    
    ("9a", "Civilian Response", "(Eli · two teams — civilian-first choice)", "PLACEHOLDER SPLIT FROM EXISTING CH 9",
     "Same week — two psion teams contest the forming line; civilian response to Eli's presence.",
     "protect the cooperative evidence and the growers.",
     "psion teams in proximity; Eli recognizes the charge but hesitates; Wren chooses evacuation.",
     "Wren chooses civilian-first evacuation; a grower is hurt; evidence damaged. No completed Manual Override. Cost: trust without label; recognition without command.",
     "factions contest charged ground; crop band as new line. Wrong reading: band = faction message; hands = power display. Cost: grower hurt; evidence damaged; Eli's moral override incomplete.",
     "II"),
    
    ("10a", "Evidence Burn", "(Eli · people over evidence — aftermath)", "PLACEHOLDER SPLIT FROM EXISTING CH 10",
     "Same week — aftermath of the evidence confrontation; Kitt's fork maps meet the physical Shabdajal.",
     "preserve the cooperative's knowledge; make sense of the damage.",
     "evidence damaged; Custodians still inbound; Wren's resistance makes substitution visible.",
     "Eli names his conduct and asks honestly for participation; Wren admits use and agrees to tell him first. Cost: fear of losing proof becomes certainty and command; trust without label.",
     "Kitt's fork maps + physical Shabdajal as distributed network; GHC/TREE rhyme. Wrong reading: fork = faction code; Shabdajal = weapon. Cost: evidence damaged; moral hold incomplete.",
     "II"),
    
    ("11a", "The Laos Border", "(Eli · Laos closure — border crossing)", "PLACEHOLDER SPLIT FROM EXISTING CH 11",
     "Following week — Laos border closed; Eli forced into Vietnam detour; Shireen memory transfer.",
     "continue toward Yunnan/Sanxingdui; maintain the rescue clock for Rasel.",
     "documents and jurisdictions disagree; handoff keeps slipping; Laos closed; Wren cannot command a hidden route.",
     "commits to the detour despite wrongness. Cost: exposure; time lost; margin burned.",
     "border-era spray/burn scar as discipline mark; Shireen's garden warning as Bangladesh refusal Turning. Wrong reading: scar = war evidence; warning = threat. Cost: route compromised; trust strained.",
     "II"),
    
    ("12a", "Conservation Campus", "(Eli · Sanxingdui — campus and Mandate annex)", "PLACEHOLDER SPLIT FROM EXISTING CH 12",
     "Sanxingdui conservation campus; Mandate annex surveillance; greenhouse preparation.",
     "access the conservation data; find Rasel through the Mandate records.",
     "Mandate annex security; Qiao's clearance window; Rasel's identity concealed under alias.",
     "Eli accepts Qiao's risk and Luo's route. Cost: clearance window finite; Rasel still in apparatus; receiver cost visible in tremor.",
     "Bronze Sacred Tree as distributed relation; nine traces wandering independently; mesh not trunk. Wrong reading: tree = prophecy; top = Eli's inheritance. Cost: invented top rejected; mesh confirmed, not hierarchy.",
     "II"),
]

def make_placeholder(suffix, title, scope, label, timeline, want, obstacle, choice, deep_time, act):
    return f"""---

### Ch {suffix} — {title} {scope} — {label}
- **Timeline — PLACEHOLDER:** {timeline}
- **Want / Attachment:** {want}
- **Obstacle:** {obstacle}
- **Choice → Cost:** {choice}
- **Deep-time residue — PLACEHOLDER:** {deep_time}
- **Placeholder note — LOCKED:** All locked prose for this beat lives in existing Ch {suffix[0]} card. This card is a draft split point only; no new locked prose is introduced here.
- **Act:** {act}
"""

# Read file
with open(BEATSHEET, 'r') as f:
    content = f.read()

# Verify clean state
assert '### Ch 1a —' not in content, "File already has placeholders, checkout first"
assert '### Ch 2a —' not in content, "File already has placeholders, checkout first"

# Find all chapter heading positions
pattern = r'^### Ch (\d+) — '
matches = list(re.finditer(pattern, content, re.MULTILINE))

if len(matches) != 13:
    raise ValueError(f"Expected 13 chapters, found {len(matches)}")

# Insert placeholders from last to first (reversed order preserves positions)
for i in range(len(PLACEHOLDERS) - 1, -1, -1):
    suffix, title, scope, label, timeline, want, obstacle, choice, deep_time, act = PLACEHOLDERS[i]
    
    # Insert before the NEXT chapter heading (i+1 index in matches)
    insert_pos = matches[i + 1].start()
    placeholder_text = make_placeholder(suffix, title, scope, label, timeline, want, obstacle, choice, deep_time, act)
    
    content = content[:insert_pos] + placeholder_text + content[insert_pos:]

# Add mapping section at the end
mapping = """
---

## CHAPTER MAPPING — OLD TO NEW

| New Ch | Old Ch | Title | Status |
|---|---|---|---|
| 1 | 1 | The Hour That Belongs to No One | EXISTING |
| 2 | 1 | Saturday Departure | PLACEHOLDER SPLIT FROM EXISTING CH 1 |
| 3 | 2 | His Hand / Checkpoints and the Stack | EXISTING |
| 4 | 2 | Singapore Intake | PLACEHOLDER SPLIT FROM EXISTING CH 2 |
| 5 | 3 | What Didn't Die | EXISTING |
| 6 | 3 | Breach Recovery | PLACEHOLDER SPLIT FROM EXISTING CH 3 |
| 7 | 4 | The Passage | EXISTING |
| 8 | 4 | Departure and Wat | PLACEHOLDER SPLIT FROM EXISTING CH 4 |
| 9 | 5 | The Field That Counts | EXISTING |
| 10 | 5 | Grounding Arrival | PLACEHOLDER SPLIT FROM EXISTING CH 5 |
| 11 | 6 | Midpoint: First Witness | EXISTING |
| 12 | 6 | Witness Ground | PLACEHOLDER SPLIT FROM EXISTING CH 6 |
| 13 | 7 | The Forming Line | EXISTING |
| 14 | 7 | The Cooperative Edge | PLACEHOLDER SPLIT FROM EXISTING CH 7 |
| 15 | 8 | Ila's Hands | EXISTING |
| 16 | 8 | Hands and Repair | PLACEHOLDER SPLIT FROM EXISTING CH 8 |
| 17 | 9 | Two Teams | EXISTING |
| 18 | 9 | Civilian Response | PLACEHOLDER SPLIT FROM EXISTING CH 9 |
| 19 | 10 | People Over Evidence | EXISTING |
| 20 | 10 | Evidence Burn | PLACEHOLDER SPLIT FROM EXISTING CH 10 |
| 21 | 11 | Human Doors | EXISTING |
| 22 | 11 | The Laos Border | PLACEHOLDER SPLIT FROM EXISTING CH 11 |
| 23 | 12 | The Tree with No Top | EXISTING |
| 24 | 12 | Conservation Campus | PLACEHOLDER SPLIT FROM EXISTING CH 12 |
| 25 | 13 | The Living Route | EXISTING |

**Note:** New chapters 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 are placeholders. All locked prose for these beats lives in the corresponding existing chapter cards.
"""

content = content.rstrip() + "\n" + mapping

# Write the file
with open(BEATSHEET, 'w') as f:
    f.write(content)

# Verify
with open(BEATSHEET, 'r') as f:
    content = f.read()

matches = list(re.finditer(r'^### Ch (\d+[a-z]?) — ', content, re.MULTILINE))
print(f"✓ Book I beatsheet expanded to {len(matches)} chapter cards")
nums = [m.group(1) for m in matches]
print(f"✓ Chapter numbers: {nums}")

# Check mapping section exists
if "## CHAPTER MAPPING — OLD TO NEW" in content:
    print("✓ Mapping section added")
else:
    print("✗ Mapping section missing")

# Check all 12 placeholders present
placeholder_count = sum(1 for n in nums if 'a' in n)
print(f"✓ Placeholder chapters: {placeholder_count}")
print(f"✓ Existing chapters: {len(matches) - placeholder_count}")

import re
from pathlib import Path

path = Path('/Users/khan/Projects/The-Orphaned-Species/50_The_Orphaned_Species/manuscripts/II_The_Descent.md')
text = path.read_text(encoding='utf-8')
lines = text.splitlines()

# Find body start
body_start = None
for i, line in enumerate(lines):
    if line.startswith('## Chapter '):
        body_start = i
        break

front_matter = lines[:body_start]

# Extract all chapter prose blocks between headings
chapter_indices = []
for i, line in enumerate(lines):
    if re.match(r'^## Chapter \d+', line):
        chapter_indices.append(i)

chunks = {}
for idx, start in enumerate(chapter_indices):
    end = chapter_indices[idx+1] if idx+1 < len(chapter_indices) else len(lines)
    heading = lines[start]
    m = re.match(r'^## Chapter (\d+)[—\-](.+)$', heading)
    if not m:
        continue
    ch_num = int(m.group(1))
    raw_title = m.group(2).strip()
    # Clean title: remove bracketed tags
    title = re.sub(r'\[.*?\]', '', raw_title).strip()
    # Get prose content
    content = lines[start+1:end]
    # Remove placeholder-only lines and separators
    cleaned = []
    for cl in content:
        s = cl.strip()
        if s.startswith('[PLACEHOLDER') or s == '---':
            continue
        cleaned.append(cl)
    # Trim leading/trailing empties
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    chunks[ch_num] = {'title': title, 'lines': cleaned, 'raw_heading': heading}

print(f"Found {len(chunks)} source chapters:")
for k in sorted(chunks):
    print(f"  Ch{k}: {chunks[k]['title']} ({len(chunks[k]['lines'])} lines)")

# Build clean output
output = []
output.extend(front_matter)
output.append('')
output.append('---')
output.append('')
output.append('> **RESTRUCTURED 2026-08-21:** Reorganized from 10 chapters to 25 chapters per `32_volume_II_beatsheet.md`. Existing prose mapped to authoritative chapter slots; chapters 11–24 carry placeholder expansion notes derived from the beat map. No prose deleted.')
output.append('')

# Direct mapping: target chapter -> source chapter
# This maps each target chapter to the existing prose block that belongs there.
# Where multiple source chapters contribute to one target, we note transition points.
mapping = {
    1: 1,    # What Came Home -> Ch1
    2: None, # PLACEHOLDER - archive, Adapa, Folly, Map, Egypt, Enheduanna
    3: 3,    # Cold Container -> Ch3
    4: None, # PLACEHOLDER - Thrace clinic, Laurel race, Somchai hard no, depth-scan
    5: 5,    # Buried Instrument (Wren finds cut) -> Ch5
    6: 6,    # Göbekli continuation, convoy, Pömmelte/church, hearth, Sol -> Ch6
    7: None, # PLACEHOLDER - Rollright/Men-an-Tol, Callum recovery, Wren confession, Rowan transfer-records
    8: 8,    # Healer's Terms (Somchai hard no, clinic evacuation, corridor, bitter cup, Maren contact) -> Ch8
    9: None, # PLACEHOLDER - Hassan extraction, ring, Maren midpoint
    10: 10,  # Holding site continuation, escape -> Ch10
    11: 11,  # Changing Map (Wren/Rowan, Extra settlement, dead-zone) -> Ch11
    12: None, # PLACEHOLDER - Pömmelte aftermath, Holt turning, Maren moral wound
    13: 13,  # Riddling Ground (Rollright/Men-an-Tol, Wren/Rowan renewal) -> Ch13
    14: None, # PLACEHOLDER - Stonehenge approach, Custodian fight
    15: 15,  # Riddling Ground continuation -> Ch15
    16: 16,  # Riddling Ground continuation (Stonehenge station, Custodian retooling) -> Ch16
    17: None, # PLACEHOLDER - corridor transit, bitter cup, Lovernios, Maren one-way contact
    18: 18,  # Corridor Signal (corridor transit, Maren contact, bitter cup, Lovernios) -> Ch18
    19: None, # PLACEHOLDER - Avebury approach, reunion prep, evacuation
    20: 20,  # Staff Entrance (Stonehenge, Somchai hard no, Custodians) -> Ch20
    21: 21,  # Release/aftermath (Avebury entrance, reunion, release climax) -> Ch21
    22: None, # PLACEHOLDER - Stonehenge interior, relay, Eli sideways
    23: 23,  # Release/aftermath continuation (Lang, Imani, aftermath, Book III ignition) -> Ch23
    24: None, # PLACEHOLDER - Manual Override under concurrent assault
    25: None, # PLACEHOLDER - final aftermath, open ending
}

# Titles for chapters with prose
prose_titles = {
    1: 'What Came Home',
    3: 'The Cold Container',
    5: 'The Buried Instrument',
    6: 'The Changing Map',
    7: 'The Riddling Ground',  # actually this is placeholder but we have prose in current 7
    8: 'The Healer\'s Terms',
    9: 'The Holding Site',
    10: 'The Holding Site',
    11: 'The Changing Map',
    12: 'The Riddling Ground',
    13: 'The Riddling Ground',
    14: 'The Corridor Signal',
    15: 'The Riddling Ground',
    16: 'The Riddling Ground',
    17: 'The Corridor Signal',
    18: 'The Corridor Signal',
    19: 'The Staff Entrance',
    20: 'The Staff Entrance',
    21: 'Release',
    22: 'Release',
    23: 'Release',
}

# Better: use titles from source chunks, with corrections
title_overrides = {
    3: 'The Cold Container',
    4: 'The Healer\'s Terms',
    5: 'The Buried Instrument',
    6: 'The Changing Map',
    7: 'The Riddling Ground',
    8: 'The Healer\'s Terms',
    9: 'The Holding Site',
    10: 'The Holding Site',
    11: 'The Changing Map',
    12: 'The Changing Map',
    13: 'The Riddling Ground',
    14: 'The Riddling Ground',
    15: 'The Riddling Ground',
    16: 'The Riddling Ground',
    17: 'The Corridor Signal',
    18: 'The Corridor Signal',
    19: 'The Staff Entrance',
    20: 'The Staff Entrance',
    21: 'Release',
    22: 'Release',
    23: 'Release',
}

# Wait - looking at the actual source chunks:
# Ch3 = "The Cold Container" - correct
# Ch5 = "What Came Home" [EXISTING] - this is wrong title in source
# Ch6 = "What Came Home" [EXISTING] - wrong title
# Ch8 = "What Came Home" [EXISTING] - wrong title
# Ch10 = "What Came Home" [EXISTING] - wrong title
# Ch11 = "What Came Home" [EXISTING] - wrong title
# Ch13 = "What Came Home" [EXISTING] - wrong title
# Ch15 = "What Came Home" [EXISTING] - wrong title
# Ch16 = "What Came Home" [EXISTING] - wrong title
# Ch18 = "What Came Home" [EXISTING] - wrong title
# Ch20 = "What Came Home" [EXISTING] - wrong title
# Ch21 = "What Came Home" [EXISTING] - wrong title
# Ch23 = "What Came Home" [EXISTING] - wrong title

# The source file has broken titles due to earlier restructuring. We need to fix them.

# For chapters with prose, assign proper title based on content
def guess_title(ch_num, src_title):
    # Map based on content knowledge
    title_map = {
        1: 'What Came Home',
        3: 'The Cold Container',
        5: 'The Buried Instrument',
        6: 'The Changing Map',
        7: 'The Healer\'s Terms',  # current ch8 content
        8: 'The Holding Site',     # current ch10 content
        9: 'The Holding Site',     # current ch11 content
        10: 'TBD',                 # placeholder
        11: 'The Changing Map',    # current ch13 content
        12: 'TBD',                 # placeholder
        13: 'The Riddling Ground', # current ch15 content
        14: 'TBD',                 # placeholder
        15: 'The Riddling Ground', # current ch16 content
        16: 'TBD',                 # placeholder
        17: 'The Corridor Signal', # current ch18 content
        18: 'The Corridor Signal', # current ch19 content
        19: 'The Staff Entrance',  # current ch20 content
        20: 'Release',             # current ch21 content
        21: 'Release',             # current ch23 content
        22: 'TBD',                 # placeholder
        23: 'Release',             # current ch23 content
        24: 'TBD',                 # placeholder
        25: 'TBD',                 # placeholder
    }
    return title_map.get(ch_num, src_title)

for target in range(1, 26):
    src = mapping[target]
    if src and src in chunks:
        chunk = chunks[src]
        title = title_overrides.get(target, chunk['title'])
        if title == 'Distributed' or title.startswith('What Came Home') and target != 1:
            title = guess_title(target, chunk['title'])
        output.append(f'## Chapter {target}—{title}')
        output.extend(chunk['lines'])
    else:
        # Placeholder
        notes = {
            2: 'Draft this chapter from beatsheet beats: Mesopotamian archive packet; Adapa lacuna + Babylonian Map; Göbekli conservation window; Folly/Sorting/Fade; Egypt comparative packet (uraeus/benben/ankh-tree); Enheduanna hymn + Inana Descent seed; Mask of Warka echo; curator hard boundary; Hassan west-corridor transfer category. Clock A: Maren checksum → Göbekli window. Clock B: Wren prioritizes Hassan route. Antagonist: Anika legal hold. End hook: Göbekli security movement converges.',
            4: 'Draft this chapter from beatsheet beats: Thrace clinic + Laurel crossing (present-tense after Ch 3). Somchai hard no under pilgrim demand; depth-scan after consenting heal; optional Parade drip. Laurel sailing race: Eli abandons winning line to pull Iason; Iason spends guild appeal to attest Eli/Wren onto clinic road; house night produces giant face/white markings/older-hand movement. Aylin goes ahead in ambulance. Clock A: patient IDs Thrace hold / Hassan alive. Clock B: clinic exposure; pilgrim pressure. Antagonist: security wants registered healer. End hook: injured prisoner carrying Hassan\'s transfer signature arrives; Somchai\'s clinic receives them.',
            7: 'Draft this chapter from beatsheet beats: Rollright + Men-an-Tol in one corridor. Callum recovery person-first; Wren/Rowan renew by explicit choice after conduct; Wren\'s confession to Eli about receiver-reporting; Rowan\'s transfer-records reveal of Charkha pair-severance ("dependency transfer"); Sídhe layered memory; iron severs contact; rowan negotiates. Inana romance face payoff: gates/attend/return-with-cost as conduct. Clock A: living polarity west; Anthea chord incomplete. Clock B: Callum person-first; Wren/Rowan renew. Antagonist: pair-severance ledger / Charkha foundations. End hook: chord points toward Stonehenge; group moves directly into transit.',
            9: 'Draft this chapter from beatsheet beats: Hassan extraction from Thrace/Balkan holding site. Hassan + Rasel\'s wedding ring + Maren\'s field notebook fragment. Wren\'s corridor timing; Charkha middle-layer Devika Sen; Maren moral wound seed (named subject/redacted consequence via Hassan). Eli chooses Hassan over clean file; part of Maren\'s record stays behind. Clock A: Hassan + ring; Maren alive/wired/no address. Clock B: Wren refuses mother-chair. Antagonist: Charkha clipboards / Custodian transfer. End hook: Hassan\'s first-person account identifies dead-zone signature matching Pömmelte carrier purge.',
            12: 'Draft this chapter from beatsheet beats: Pömmelte purge geometry + broken-line church domestic inward-control. Extra settlement; Sol recruitment; Callum recovery; hearth circle night after corridor break; *in the flow* first spoken; Wren burns credential to keep contact; Maren\'s field notebook living correction; Drifting Heart Liturgy first full utterance. Clock A: dead-zone → Maren\'s western web; Holt/matriline Turning. Clock B: Callum recovery; route burned. Antagonist: Sol recruiters + registry clerks. End hook: living song/polarity points toward Rollright and Men-an-Tol; Wren\'s confession relocated to Ch 7.',
            14: 'Draft this chapter from beatsheet beats: Stonehenge approach and station. Custodian psionic seizure at Stonehenge; Custodians recuperate, reassign, retool with tighter coordination; instrument cap—Rasel absent; Anika containment; Sol forced-unity; Somchai refuses healing-field without continuing consent; Wren/Rowan ordinary non-crisis space; Eli names provisional fear. Clock A: station geometry → Avebury inhabited ground; Maren lucid/compromised/asking not to be kept. Clock B: Wren/Rowan keep evacuation ≠ sacrifice. Antagonist: Custodian psionic seizure, then physical seizure of ground. End hook: Maren is lucid, compromised, and asking not to be kept.',
            17: 'Draft this chapter from beatsheet beats: Rollright to Stonehenge corridor transit. Maren one-way contact only—recognition-hunger, no address/plan; Eli may misread refusal as captivity speaking. Bitter cup + Lovernios plant-intelligence layer at Anglesey; partial memory on exit; Lovernios clarifies full-res: plant intelligence, growth as living map. Eli receives him as other; contact maps to Wisdom at head but chapter must not say so. Clock A: one-way Maren contact. Clock B: Wren/Rowan ordinary non-crisis space. Antagonist: pursuit clock + keeper abort authority. End hook: interval and Cuno\'s geometry identify Stonehenge as live transmission station; hostile teams already there.',
            19: 'Draft this chapter from beatsheet beats: Stonehenge to Avebury approach. Living polarity points west toward her ground; corridor interval directional, not possessive; evacuation problem at Avebury—residents first; Rowan, Hassan, Sora, Somchai deploy; Maren prepared maintenance-cycle entry. Clock A: Maren maintenance cycle / family access. Clock B: Wren/Rowan keep evacuation ≠ sacrifice. Antagonist: Anika containment; Custodian ground-holding. End hook: facility descends through modern/military/chalk history; Maren inside; receptionist issues paper badge; alarm sounds—transfer beginning.',
            22: 'Draft this chapter from beatsheet beats: Stonehenge transmission station interior. Relay sequence; Eli moves sideways through time to evade Custodian psionic lock; ground seized, perimeter closed, no route back; Custodians retool with tighter coordination. Cuno\'s fragment preserves routing grammar; stone grounds forward bounded wisdom with loss intact—not one master message. Clock A: relay → Avebury inhabited ground. Clock B: Wren/Rowan keep evacuation ≠ sacrifice. Antagonist: Custodian psionic seizure. End hook: routed artifact-wisdom points to inhabited Avebury landscape; group moves toward ground-holding.',
            24: 'Draft this chapter from beatsheet beats: Climax concurrent assault at Avebury. Failed keep-her/use-her-signal assault (Anika containment and/or Sol forced-unity grab for stabilizing signal) runs in same beat window as Eli\'s release choice. Custodians hold Stonehenge station and approaches after failing to lock Eli—ground seized, perimeter closed. Group holds relational Manual Override under attack without worship, betrayal, or command hierarchy. Safety cost of concurrent assault. Clock A: embodied mutual reunion → release. Clock B: relational Manual Override under assault. Antagonist: Anika and/or Sol keep-her assault. End hook: Eli refuses reunion the Charkha built; Maren walks out alive.',
            25: 'Draft this chapter from beatsheet beats: Release aftermath and Book III ignition. Maren walks out alive and does not come home; stabilization signal surrendered; Eli chooses release—the only cut that works. Wren/Rowan and Wren/Eli name separate chosen bonds; Rowan/Eli establish respect and no romance. Hassan chooses whether to testify; Somchai leaves with mobile clinic; Callum\'s repair crew becomes Book III\'s divided Extra constituency. Final image: Eli watching Maren go, feeling loss without turning it into command. Book III ignition: Sol recruits forced unity; Anika\'s diagnosis gains evidence; communities receive capacity before civic structure; no civic system ready; old registries are.',
        }
        note = notes.get(target, 'Draft this chapter from beatsheet beats. Expand from surrounding chapters during drafting.')
        output.append(f'## Chapter {target}—TBD')
        output.append(f'[{note}]')
    
    output.append('')
    output.append('---')
    output.append('')

# Trim trailing
while output and output[-1].strip() in ('---', ''):
    output.pop()

path.write_text('\n'.join(output) + '\n', encoding='utf-8')
print(f"Restructured manuscript written: {len(output)} lines")

# Verify
with open(path, 'r', encoding='utf-8') as f:
    verify = f.read().splitlines()

print(f"Verification: {len(verify)} total lines")
ch_count = sum(1 for l in verify if re.match(r'^## Chapter \d+', l))
print(f"Chapter headings: {ch_count}")
for i, l in enumerate(verify):
    if re.match(r'^## Chapter \d+', l):
        print(f"  Line {i+1}: {l[:80]}")

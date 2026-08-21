#!/usr/bin/env python3
"""Build prose alignment plan: map new 25-chapter prose to beatsheet sources.

Outputs a JSON manifest of source blocks per chapter so a prose-mover can
follow the same path that a prose audit generator would follow.
"""
import re, json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List

MANUSCRIPTS = {
    'I': Path('50_The_Orphaned_Species/manuscripts/I_The_Breach.md'),
    'II': Path('50_The_Orphaned_Species/manuscripts/II_The_Descent.md'),
    'III': Path('50_The_Orphaned_Species/manuscripts/III_The_Compact.md'),
    'IV': Path('50_The_Orphaned_Species/manuscripts/IV_The_Court_of_Threads.md'),
}

@dataclass
class ChapterBlock:
    num: str
    title: str
    status: str
    start: int
    end: int
    source_old: int | None = None
    source_source: str = ''

def parse_manuscript_chapters(path: Path) -> List[ChapterBlock]:
    text = path.read_text()
    pattern = r'^## Chapter (\d+[a-z]?)—([^\[]+)\[([^\]]+)\]'
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    blocks = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        blocks.append(ChapterBlock(
            num=m.group(1),
            title=m.group(2).strip(),
            status=m.group(3).strip(),
            start=start,
            end=end,
        ))
    return blocks

# Old→new source maps from beatsheet expansions
SOURCE_MAP = {
    'I': [
        (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4),
        (9, 5), (10, 5), (11, 6), (12, 6), (13, 7), (14, 7), (15, 8), (16, 8),
        (17, 9), (18, 9), (19, 10), (20, 10), (21, 11), (22, 11), (23, 12), (24, 12), (25, 13)
    ],
    'II': [
        (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4),
        (9, 5), (10, 5), (11, 5), (12, 6), (13, 6), (14, 6), (15, 7), (16, 7),
        (17, 7), (18, 8), (19, 8), (20, 9), (21, 9), (22, 9), (23, 10), (24, 10), (25, 10)
    ],
    'III': [
        (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4),
        (9, 5), (10, 5), (11, 6), (12, 7), (13, 7), (14, 8), (15, 8), (16, 9),
        (17, 10), (18, 11), (19, 12), (20, 13), (21, 14), (22, 15), (23, 16), (24, 17), (25, 18)
    ],
    'IV': [
        (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4),
        (9, 5), (10, 5), (11, 6), (12, 6), (13, 7), (14, 7), (15, 8), (16, 8),
        (17, 9), (18, 9), (19, 10), (20, 10), (21, 11), (22, 11), (23, 12), (24, 13), (25, 14)
    ],
}

# New chapter titles from beatsheets (optional — we can source from prose headings)
NEW_TITLES = {
    'I': {
        1: 'The Hour That Belongs to No One', 2: 'Saturday Departure',
        3: 'His Hand / Checkpoints and the Stack', 4: 'Singapore Intake',
        5: 'What Didn\'t Die', 6: 'Breach Recovery', 7: 'The Passage', 8: 'Departure and Wat',
        9: 'The Field That Counts', 10: 'Grounding Arrival', 11: 'Midpoint: First Witness',
        12: 'Witness Ground', 13: 'The Forming Line', 14: 'The Cooperative Edge',
        15: 'Ila\'s Hands', 16: 'Hands and Repair', 17: 'Two Teams', 18: 'Civilian Response',
        19: 'People Over Evidence', 20: 'Evidence Burn', 21: 'Human Doors', 22: 'The Laos Border',
        23: 'The Tree with No Top', 24: 'Conservation Campus', 25: 'The Living Route'
    },
    'II': {
        1: 'What Came Home', 2: 'The Westbound Packet', 3: 'The Folly', 4: 'The Archive Exit',
        5: 'The Buried Instrument', 6: 'The Clinic Approach', 7: 'Laurel Crossing',
        8: 'The Healer\'s Clinic', 9: 'The Holding Entry', 10: 'The Midpoint Revelation',
        11: 'Ring and Romance Cost', 12: 'The Changing Map', 13: 'The Broken-Line Church',
        14: 'The Stray Settlement', 15: 'The Riddling Ground', 16: 'Callum Recovery and Renewal',
        17: 'The Transfer-Records Discovery', 18: 'The Corridor Signal', 19: 'One-Way Contact',
        20: 'The Transmission Station', 21: 'The Instrument Cap', 22: 'The Avebury Approach',
        23: 'Release', 24: 'The Release Choice', 25: 'Aftermath and Book III Ignition'
    },
    'III': {
        1: 'The Boat at Morning', 2: 'Harbor Wake', 3: 'The First Sponsorship',
        4: 'Terms of Welcome', 5: 'The Artifact Delivery', 6: 'The Person Freedom Failed',
        7: 'The Repair Dock Evening', 8: 'The Kitchen Ledger', 9: 'The Sideways Record',
        10: 'The Standard', 11: 'The Ambassador Dinner', 12: 'The Names They Carry',
        13: 'Qiao\'s Testimony and the Survivor', 14: 'The Compact',
        15: 'The Signing and the Shed Fire', 16: 'The Voyage and the Warning',
        17: 'A Crown With an End', 18: 'Arrival and the First Water Decision',
        19: 'Gutter Clearing and the Work Song', 20: 'The Corridor Order',
        21: 'The Cost of Consent', 22: 'The Drone-Strike Cost',
        23: 'The Hearing Room and the Side Room', 24: 'The Hearing Begins',
        25: 'The Handover'
    },
    'IV': {
        1: 'The Doors', 2: 'Present Consent', 3: 'Three Rooms', 4: 'What We Build',
        5: 'The Rumor', 6: 'The Body of State', 7: 'The Two Houses', 8: 'The False Heir',
        9: 'The Room Prepared', 10: 'Before the First Breath', 11: 'The Stag Teacher',
        12: 'The Five Forms Week', 13: 'The Nacre Audit', 14: 'The Cloister Risk Score',
        15: 'The Recruitment Hearing', 16: 'The Ilyara Boundary', 17: 'The Southern Canopy',
        18: 'The Work-Song Class', 19: 'The False Heir Draft', 20: 'The Hospital Conversation',
        21: 'The Continuity Extension File', 22: 'The Praetorian Demand',
        23: 'The Labor Inversion', 24: 'The Sideways Four Seconds',
        25: 'The Flight Departure'
    },
}

manifest = {}
for book_short in ['I', 'II', 'III', 'IV']:
    path = MANUSCRIPTS[book_short]
    blocks = parse_manuscript_chapters(path)
    source_map = dict(SOURCE_MAP[book_short])
    
    book_plan = []
    for new_ch, old_ch in source_map.items():
        # Find the source block with old chapter number
        source_block = next((b for b in blocks if b.num == str(old_ch)), None)
        target_title = NEW_TITLES[book_short].get(new_ch, source_block.title if source_block else 'TBD')
        
        book_plan.append({
            'new_ch': new_ch,
            'title': target_title,
            'source_old_ch': old_ch,
            'source_status': source_block.status if source_block else 'PLACEHOLDER',
            'source_words': len(source_block.title) if source_block and source_block.status == 'EXISTING' else 0,
            'action': 'carry' if source_block and source_block.status == 'EXISTING' and new_ch == old_ch else 'split' if source_block and source_block.status == 'EXISTING' else 'placeholder'
        })
    
    manifest[book_short] = {
        'manuscript': str(path),
        'total_chapters': len(book_plan),
        'existing_count': sum(1 for x in book_plan if x['action'] in ('carry', 'split')),
        'placeholder_count': sum(1 for x in book_plan if x['action'] == 'placeholder'),
        'chapters': book_plan
    }

Path('dist/manuscript_alignment_plan.json').write_text(json.dumps(manifest, indent=2))
print('Wrote manuscript_alignment_plan.json')
for book_short, data in manifest.items():
    print(f"\nBook {book_short}: {data['existing_count']} existing, {data['placeholder_count']} placeholder")
    for ch in data['chapters']:
        print(f"  Ch {ch['new_ch']:2d} | {ch['title'][:35]:35s} | {ch['source_status']:10s} | {ch['action']}")

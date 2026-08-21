#!/usr/bin/env python3
"""Realign manuscript prose from old chapter structure to new 25-chapter structure.

For each book:
- Carry chapters keep their existing prose in place.
- Split chapters duplicate the source old-chapter prose block into the new slot.
- Placeholder chapters get a minimal [PLACEHOLDER] block.
"""
import re
from pathlib import Path

BOOKS = {
    'I': {
        'src': Path('50_The_Orphaned_Species/manuscripts/I_The_Breach.md'),
        'dst': Path('dist/I_The_Breach_aligned.md'),
        'title': 'The Orphaned Species Book I: The Breach',
        'map': [
            (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4),
            (9, 5), (10, 5), (11, 6), (12, 6), (13, 7), (14, 7), (15, 8), (16, 8),
            (17, 9), (18, 9), (19, 10), (20, 10), (21, 11), (22, 11), (23, 12), (24, 12), (25, 13)
        ],
        'titles': {
            1: 'The Hour That Belongs to No One', 2: 'Saturday Departure',
            3: 'His Hand / Checkpoints and the Stack', 4: 'Singapore Intake',
            5: 'What Didn\'t Die', 6: 'Breach Recovery', 7: 'The Passage', 8: 'Departure and Wat',
            9: 'The Field That Counts', 10: 'Grounding Arrival', 11: 'Midpoint: First Witness',
            12: 'Witness Ground', 13: 'The Forming Line', 14: 'The Cooperative Edge',
            15: 'Ila\'s Hands', 16: 'Hands and Repair', 17: 'Two Teams', 18: 'Civilian Response',
            19: 'People Over Evidence', 20: 'Evidence Burn', 21: 'Human Doors', 22: 'The Laos Border',
            23: 'The Tree with No Top', 24: 'Conservation Campus', 25: 'The Living Route'
        },
    },
    'II': {
        'src': Path('50_The_Orphaned_Species/manuscripts/II_The_Descent.md'),
        'dst': Path('dist/II_The_Descent_aligned.md'),
        'title': 'The Orphaned Species Book II: The Descent',
        'map': [
            (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4),
            (9, 5), (10, 5), (11, 5), (12, 6), (13, 6), (14, 6), (15, 7), (16, 7),
            (17, 7), (18, 8), (19, 8), (20, 9), (21, 9), (22, 9), (23, 10), (24, 10), (25, 10)
        ],
        'titles': {
            1: 'What Came Home', 2: 'The Westbound Packet', 3: 'The Folly', 4: 'The Archive Exit',
            5: 'The Buried Instrument', 6: 'The Clinic Approach', 7: 'Laurel Crossing',
            8: 'The Healer\'s Clinic', 9: 'The Holding Entry', 10: 'The Midpoint Revelation',
            11: 'Ring and Romance Cost', 12: 'The Changing Map', 13: 'The Broken-Line Church',
            14: 'The Stray Settlement', 15: 'The Riddling Ground', 16: 'Callum Recovery and Renewal',
            17: 'The Transfer-Records Discovery', 18: 'The Corridor Signal', 19: 'One-Way Contact',
            20: 'The Transmission Station', 21: 'The Instrument Cap', 22: 'The Avebury Approach',
            23: 'Release', 24: 'The Release Choice', 25: 'Aftermath and Book III Ignition'
        },
    },
    'III': {
        'src': Path('50_The_Orphaned_Species/manuscripts/III_The_Compact.md'),
        'dst': Path('dist/III_The_Compact_aligned.md'),
        'title': 'The Orphaned Species Book III: The Compact',
        'map': [
            (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4),
            (9, 5), (10, 5), (11, 6), (12, 7), (13, 7), (14, 8), (15, 8), (16, 9),
            (17, 10), (18, 11), (19, 12), (20, 13), (21, 14), (22, 15), (23, 16), (24, 17), (25, 18)
        ],
        'titles': {
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
    },
    'IV': {
        'src': Path('50_The_Orphaned_Species/manuscripts/IV_The_Court_of_Threads.md'),
        'dst': Path('dist/IV_The_Court_of_Threads_aligned.md'),
        'title': 'The Orphaned Species Book IV: The Court of Threads',
        'map': [
            (1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4),
            (9, 5), (10, 5), (11, 6), (12, 6), (13, 7), (14, 7), (15, 8), (16, 8),
            (17, 9), (18, 9), (19, 10), (20, 10), (21, 11), (22, 11), (23, 12), (24, 13), (25, 14)
        ],
        'titles': {
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
    },
}

def parse_chapter_blocks(text: str):
    pattern = r'^## Chapter (\d+[a-z]?)—([^\[]+)\[([^\]]+)\]'
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    blocks = {}
    for i, m in enumerate(matches):
        num = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        blocks[num] = {
            'heading': m.group(0),
            'title': m.group(2).strip(),
            'status': m.group(3).strip(),
            'start': start,
            'end': end,
            'content': text[start:end],
        }
    return blocks

for book_key, cfg in BOOKS.items():
    text = cfg['src'].read_text()
    blocks = parse_chapter_blocks(text)
    
    # Split header from chapter body
    first_ch = text.find('\n## Chapter')
    header = text[:first_ch] if first_ch != -1 else text[:4000]
    # Remove trailing status tables from header (keep only prose header)
    header_lines = []
    in_table = False
    for line in header.split('\n'):
        if line.strip().startswith('|'):
            in_table = True
            continue
        if in_table and not line.strip():
            in_table = False
        if not in_table:
            header_lines.append(line)
    header = '\n'.join(header_lines).rstrip() + '\n\n'
    
    new_chapters = []
    for new_ch, old_ch in cfg['map']:
        title = cfg['titles'][new_ch]
        source_block = blocks.get(str(old_ch))
        
        if new_ch == old_ch and source_block and source_block['status'] == 'EXISTING':
            # Carry: keep original block as-is
            block_content = source_block['content']
        elif source_block and source_block['status'] == 'EXISTING':
            # Split: duplicate source prose with new heading
            block_content = source_block['content']
            # Replace heading line with new chapter number, title, and split tag
            block_content = re.sub(
                r'^## Chapter \d+[a-z]?—[^\[]+\[[^\]]+\]',
                f'## Chapter {new_ch}—{title} [SPLIT-FROM: Ch {old_ch}]',
                block_content,
                count=1
            )
        else:
            # Placeholder
            block_content = f'## Chapter {new_ch}—{title} [PLACEHOLDER]\n[PLACEHOLDER — draft prose here]\n'
        
        new_chapters.append(block_content)
    
    # Write new manuscript
    new_text = header + '\n---\n\n'.join(new_chapters) + '\n'
    cfg['dst'].write_text(new_text)
    
    # Verify
    new_blocks = parse_chapter_blocks(new_text)
    print(f"Book {book_key}: {len(new_blocks)} chapters written to {cfg['dst']}")
    missing = [i for i in range(1, 26) if str(i) not in new_blocks and not any(str(i) in k for k in new_blocks)]
    if missing:
        print(f"  MISSING: {missing}")
    else:
        print(f"  All 25 chapters present ✓")

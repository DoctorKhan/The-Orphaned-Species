#!/usr/bin/env python3
"""Clean aligned manuscript chapter headings to remove stale 'Distributed'/'TBD' labels."""

import re
from pathlib import Path

MANUSCRIPTS = {
    'I': Path('50_The_Orphaned_Species/manuscripts/I_The_Breach.md'),
    'II': Path('50_The_Orphaned_Species/manuscripts/II_The_Descent.md'),
    'III': Path('50_The_Orphaned_Species/manuscripts/III_The_Compact.md'),
    'IV': Path('50_The_Orphaned_Species/manuscripts/IV_The_Court_of_Threads.md'),
}

TITLES = {
    'I': {
        1: 'The Hour That Belongs to No One',
        2: 'Saturday Departure',
        3: 'His Hand / Checkpoints and the Stack',
        4: 'Singapore Intake',
        5: "What Didn't Die",
        6: 'Breach Recovery',
        7: 'The Passage',
        8: 'Departure and Wat',
        9: 'The Field That Counts',
        10: 'Grounding Arrival',
        11: 'Midpoint: First Witness',
        12: 'Witness Ground',
        13: 'The Forming Line',
        14: 'The Cooperative Edge',
        15: "Ila's Hands",
        16: 'Hands and Repair',
        17: 'Two Teams',
        18: 'Civilian Response',
        19: 'People Over Evidence',
        20: 'Evidence Burn',
        21: 'Human Doors',
        22: 'The Laos Border',
        23: 'The Tree with No Top',
        24: 'Conservation Campus',
        25: 'The Living Route',
    },
    'II': {
        1: 'What Came Home',
        2: 'The Westbound Packet',
        3: 'The Folly',
        4: 'The Archive Exit',
        5: 'The Buried Instrument',
        6: 'The Clinic Approach',
        7: 'Laurel Crossing',
        8: "The Healer's Clinic",
        9: 'The Holding Entry',
        10: 'The Midpoint Revelation',
        11: 'Ring and Romance Cost',
        12: 'The Changing Map',
        13: 'The Broken-Line Church',
        14: 'The Stray Settlement',
        15: 'The Riddling Ground',
        16: 'Callum Recovery and Renewal',
        17: 'The Transfer-Records Discovery',
        18: 'The Corridor Signal',
        19: 'One-Way Contact',
        20: 'The Transmission Station',
        21: 'The Instrument Cap',
        22: 'The Avebury Approach',
        23: 'Release',
        24: 'The Release Choice',
        25: 'Aftermath and Book III Ignition',
    },
    'III': {
        1: 'The Boat at Morning',
        2: 'Harbor Wake',
        3: 'The First Sponsorship',
        4: 'Terms of Welcome',
        5: 'The Artifact Delivery',
        6: 'The Person Freedom Failed',
        7: 'The Repair Dock Evening',
        8: 'The Kitchen Ledger',
        9: 'The Sideways Record',
        10: 'The Standard',
        11: 'The Ambassador Dinner',
        12: 'The Names They Carry',
        13: "Qiao's Testimony and the Survivor",
        14: 'The Compact',
        15: 'The Signing and the Shed Fire',
        16: 'The Voyage and the Warning',
        17: 'A Crown With an End',
        18: 'Arrival and the First Water Decision',
        19: 'Gutter Clearing and the Work Song',
        20: 'The Corridor Order',
        21: 'The Cost of Consent',
        22: 'The Drone-Strike Cost',
        23: 'The Hearing Room and the Side Room',
        24: 'The Hearing Begins',
        25: 'The Handover',
    },
    'IV': {
        1: 'The Doors',
        2: 'Present Consent',
        3: 'Three Rooms',
        4: 'What We Build',
        5: 'The Rumor',
        6: 'The Body of State',
        7: 'The Two Houses',
        8: 'The False Heir',
        9: 'The Room Prepared',
        10: 'Before the First Breath',
        11: 'The Stag Teacher',
        12: 'The Five Forms Week',
        13: 'The Nacre Audit',
        14: 'The Cloister Risk Score',
        15: 'The Recruitment Hearing',
        16: 'The Ilyara Boundary',
        17: 'The Southern Canopy',
        18: 'The Work-Song Class',
        19: 'The False Heir Draft',
        20: 'The Hospital Conversation',
        21: 'The Continuity Extension File',
        22: 'The Praetorian Demand',
        23: 'The Labor Inversion',
        24: 'The Sideways Four Seconds',
        25: 'The Flight Departure',
    },
}

SPLIT_SOURCES = {
    'I': {2:1, 5:3, 6:3, 9:5, 10:5, 13:7, 14:7, 17:9, 18:9, 21:11, 22:11, 25:13},
    'II': {2:1, 5:3, 6:3, 9:5, 10:5, 11:5, 12:6, 13:6, 14:6, 15:7, 16:7, 17:7, 20:9, 21:9, 22:9, 23:10, 24:10, 25:10},
    'III': {2:1, 5:3, 6:3, 9:5, 10:5, 12:7, 13:7, 16:9, 18:11, 20:13, 22:15, 24:17, 25:18},
    'IV': {2:1, 5:3, 6:3, 9:5, 10:5, 13:7, 14:7, 17:9, 18:9, 21:11, 22:11, 24:13},
}

for book, path in MANUSCRIPTS.items():
    text = path.read_text()

    def replace_heading(m):
        num = m.group(1)
        old_status = m.group(2).strip()
        title = TITLES[book].get(int(num), m.group(3).strip())
        if num == '1' and old_status == 'EXISTING':
            status = 'EXISTING'
        elif int(num) in SPLIT_SOURCES[book]:
            status = f"SPLIT-FROM: Ch {SPLIT_SOURCES[book][int(num)]}"
        else:
            status = 'PLACEHOLDER'
        return f'## Chapter {num}—{title} [{status}]'

    text = re.sub(r'^## Chapter (\d+[a-z]?)—([^\[]+)\[([^\]]+)\]', replace_heading, text, flags=re.MULTILINE)
    path.write_text(text)
    print(f"{path}: headings cleaned")

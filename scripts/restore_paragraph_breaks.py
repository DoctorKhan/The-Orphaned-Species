#!/usr/bin/env python3
"""Restore paragraph breaks from HEAD~2 for all prose chapters."""

import re
from pathlib import Path
import subprocess

MANUSCRIPTS = {
    'I': 'I_The_Breach.md',
    'II': 'II_The_Descent.md',
    'III': 'III_The_Compact.md',
    'IV': 'IV_The_Court_of_Threads.md',
}

BASE = Path('50_The_Orphaned_Species/manuscripts')

NEW_TO_OLD = {
    'I': {1:1, 2:1, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 9:5, 10:5,
          11:6, 12:6, 13:7, 14:7, 15:8, 16:8, 17:9, 18:9, 19:10, 20:10,
          21:11, 22:11, 23:12, 24:12, 25:13},
    'II': {1:1, 2:1, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 9:5, 10:5,
           11:6, 12:6, 13:6, 14:7, 15:7, 16:7, 17:8, 18:8, 19:8,
           20:9, 21:9, 22:9, 23:10, 24:10, 25:10},
    'III': {1:1, 2:1, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 9:5, 10:5,
            11:6, 12:6, 13:7, 14:7, 15:8, 16:8, 17:9, 18:9,
            19:10, 20:11, 21:12, 22:13, 23:14, 24:15, 25:16},
    'IV': {1:1, 2:1, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 9:5, 10:5,
           11:6, 12:6, 13:7, 14:7, 15:8, 16:8, 17:9, 18:9,
           19:10, 20:10, 21:11, 22:11, 23:12, 24:13, 25:14},
}

for book_key, filename in MANUSCRIPTS.items():
    path = BASE / filename
    text = path.read_text()
    
    # Get old chapters from HEAD~2
    old_path = f'50_The_Orphaned_Species/manuscripts/{filename}'
    result = subprocess.run(['git', 'show', f'HEAD~2:{old_path}'],
                          capture_output=True, text=True,
                          cwd='/Users/khan/Projects/The-Orphaned-Species')
    old_text = result.stdout
    
    old_chapters = {}
    old_blocks = re.split(r'(?=^## Chapter \d+)', old_text, flags=re.MULTILINE)
    for block in old_blocks:
        if block.startswith('## Chapter '):
            m = re.match(r'^## Chapter (\d+)', block)
            if m:
                num = int(m.group(1))
                old_chapters[num] = block.strip()
    
    # Find current chapter positions
    chapter_positions = list(re.finditer(r'^## Chapter (\d+)', text, re.MULTILINE))
    
    new_content = []
    for i, match in enumerate(chapter_positions):
        num = int(match.group(1))
        start = match.start()
        end = chapter_positions[i+1].start() if i+1 < len(chapter_positions) else len(text)
        
        heading = text[start:end].split('\n')[0]
        
        old_num = NEW_TO_OLD[book_key].get(num)
        
        if old_num and old_num in old_chapters:
            old = old_chapters[old_num]
            old_lines = old.split('\n')
            prose_lines = []
            skip = True
            for line in old_lines:
                if skip and line.startswith('## Chapter '):
                    skip = False
                    continue
                if not skip:
                    prose_lines.append(line)
            prose = '\n'.join(prose_lines).strip()
            new_content.append(f"{heading}\n{prose}")
            print(f"  {filename} Ch {num}: restored from old Ch {old_num}, prose length {len(prose)}")
        else:
            # Keep existing content
            existing = text[start:end].strip()
            new_content.append(existing)
            print(f"  {filename} Ch {num}: kept existing (length {len(existing)})")
    
    path.write_text('\n'.join(new_content))
    print(f"{filename}: done")

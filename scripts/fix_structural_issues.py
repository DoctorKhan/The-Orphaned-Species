#!/usr/bin/env python3
"""Fix structural issues in manuscripts that cause audit noise."""
import re
from pathlib import Path

manuscripts = [
    ('I_The_Breach', '50_The_Orphaned_Species/manuscripts/I_The_Breach.md'),
    ('II_The_Descent', '50_The_Orphaned_Species/manuscripts/II_The_Descent.md'),
    ('III_The_Compact', '50_The_Orphaned_Species/manuscripts/III_The_Compact.md'),
    ('IV_The_Court_of_Threads', '50_The_Orphaned_Species/manuscripts/IV_The_Court_of_Threads.md'),
]

for name, path in manuscripts:
    text = Path(path).read_text()
    original = text
    
    # Fix 1: Split chapters that are exact duplicates of parent
    # Pattern: Chapter N+1 [SPLIT-FROM: Ch N] followed by same content as Chapter N
    # This is the main source of inflated flags
    lines = text.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check if this is a split chapter heading
        split_match = re.match(r'^## Chapter \d+.*\[SPLIT-FROM: Ch (\d+)\]', line)
        if split_match:
            parent_num = int(split_match.group(1))
            # Find the parent chapter
            parent_heading = None
            for j in range(i-1, max(-1, i-50), -1):
                if re.match(rf'^## Chapter {parent_num}\b', lines[j]):
                    parent_heading = lines[j]
                    break
            
            if parent_heading:
                # Check if next 10 lines are identical to parent's next 10 lines
                parent_start = None
                for j in range(i-1, max(-1, i-100), -1):
                    if lines[j] == parent_heading:
                        parent_start = j + 1
                        break
                
                if parent_start:
                    # Compare next 15 lines of content
                    identical = True
                    for k in range(15):
                        if i + k + 1 >= len(lines) or parent_start + k >= len(lines):
                            break
                        if lines[i + k + 1].strip() != lines[parent_start + k].strip():
                            identical = False
                            break
                    
                    if identical:
                        # This is a duplicate, skip it
                        print(f'{name}: Skipping duplicate split chapter at line {i+1}')
                        # Skip until next chapter
                        while i < len(lines) and not re.match(r'^## Chapter \d+', lines[i]):
                            i += 1
                        continue
        
        new_lines.append(line)
        i += 1
    
    text = '\n'.join(new_lines)
    
    # Fix 2: Malformed headings on single line
    # Pattern: ] ## Chapter N, → separate lines
    text = re.sub(r'\] ## Chapter ', ']\n---\n\n## Chapter ', text)
    text = re.sub(r'## Chapter (\d+),', r'## Chapter \1—', text)
    
    if text != original:
        Path(path).write_text(text)


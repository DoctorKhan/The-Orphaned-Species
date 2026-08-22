#!/usr/bin/env python3
"""Fix split chapters that contain duplicated prose from their parent chapter."""
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
    
    # Find split chapters: [SPLIT-FROM: Ch N]
    split_pattern = re.compile(r'^## Chapter \d+.*\[SPLIT-FROM: Ch \d+\]\n(.*?)(?=^## Chapter \d+|\Z)', re.MULTILINE | re.DOTALL)
    
    for match in split_pattern.finditer(text):
        split_content = match.group(1)
        split_num = match.group(0).count('\n## Chapter ')
        
        # Find the parent chapter
        parent_match = re.search(rf'^## Chapter {split_num}\n(.*?)(?=^## Chapter \d+|\Z)', text, re.MULTILINE | re.DOTALL)
        if parent_match:
            parent_content = parent_match.group(1)
            
            # Check if split content starts with parent content
            if split_content.strip().startswith(parent_content.strip()[:200]):
                # Remove duplicated prefix
                new_split_content = split_content[len(parent_content):].strip()
                if new_split_content:
                    # Replace in text
                    old_block = match.group(0)
                    new_block = match.group(0).replace(split_content, new_split_content)
                    text = text.replace(old_block, new_block, 1)
                    print(f'{name}: Removed duplicated prose from split chapter {split_num + 1}')
    
    if text != original:
        Path(path).write_text(text)


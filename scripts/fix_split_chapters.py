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
    
    # Find all split chapters
    split_pattern = re.compile(r'^## Chapter (\d+).*\[SPLIT-FROM: Ch (\d+)\]', re.MULTILINE)
    
    for match in split_pattern.finditer(text):
        split_num = int(match.group(1))
        parent_num = int(match.group(2))
        
        # Find the split chapter content
        split_heading_pattern = re.compile(
            rf'^## Chapter {split_num}.*\n(.*?)(?=^## Chapter \d+|\Z)',
            re.MULTILINE | re.DOTALL
        )
        split_match = split_heading_pattern.search(text)
        
        if not split_match:
            continue
            
        split_content = split_match.group(1)
        
        # Find the parent chapter content
        parent_heading_pattern = re.compile(
            rf'^## Chapter {parent_num}.*\n(.*?)(?=^## Chapter \d+|\Z)',
            re.MULTILINE | re.DOTALL
        )
        parent_match = parent_heading_pattern.search(text)
        
        if not parent_match:
            continue
            
        parent_content = parent_match.group(1)
        
        # Check if split content starts with parent content
        # Use first 200 words as signature
        parent_words = parent_content.split()[:200]
        split_words = split_content.split()[:200]
        
        if parent_words == split_words:
            # Remove duplicated prefix
            unique_content = split_content[len(parent_content):].strip()
            if unique_content:
                old_block = f'## Chapter {split_num}.*?\n{split_content}'
                new_block = f'## Chapter {split_num}\n{unique_content}'
                text = re.sub(old_block, new_block, text, flags=re.MULTILINE | re.DOTALL)
                print(f'{name}: Fixed Ch{split_num} (removed {len(parent_content.split())} duplicated words)')
    
    if text != original:
        Path(path).write_text(text)


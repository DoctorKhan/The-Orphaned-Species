#!/usr/bin/env python3
import re
from pathlib import Path

manuscripts = [
    Path('50_The_Orphaned_Species/manuscripts/II_The_Descent.md'),
    Path('50_The_Orphaned_Species/manuscripts/III_The_Compact.md'),
    Path('50_The_Orphaned_Species/manuscripts/IV_The_Court_of_Threads.md'),
]

for ms in manuscripts:
    text = ms.read_text()
    original = text
    
    # Fix lines where chapter headings are jammed together
    # Pattern: ] ## Chapter
    text = re.sub(r'\] ## Chapter ', ']\n---\n\n## Chapter ', text)
    # Fix chapter numbering: ## Chapter N, → ## Chapter N—
    text = re.sub(r'## Chapter (\d+),', r'## Chapter \1—', text)
    
    if text != original:
        ms.write_text(text)
        print(f'{ms.name}: fixed')
    else:
        print(f'{ms.name}: no changes')

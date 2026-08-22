#!/usr/bin/env python3
"""Fix chapter status tags in manuscripts to match actual prose content."""
import re
from pathlib import Path

manuscripts = [
    Path('50_The_Orphaned_Species/manuscripts/I_The_Breach.md'),
    Path('50_The_Orphaned_Species/manuscripts/II_The_Descent.md'),
    Path('50_The_Orphaned_Species/manuscripts/III_The_Compact.md'),
    Path('50_The_Orphaned_Species/manuscripts/IV_The_Court_of_Threads.md'),
]

# Pattern to detect real placeholder chapters
# A placeholder has [PLACEHOLDER] marker followed by placeholder text or is very short
PLACEHOLDER_PATTERN = re.compile(r'\[PLACEHOLDER[^\]]*\]', re.IGNORECASE)

for ms in manuscripts:
    text = ms.read_text()
    original = text
    lines = text.split('\n')
    modified = False
    
    for i, line in enumerate(lines):
        if line.strip().startswith('## Chapter ') and '[PLACEHOLDER]' in line:
            # Look ahead to see if this is a real placeholder or has actual prose
            j = i + 1
            has_placeholder_marker = False
            has_real_prose = False
            
            # Scan next 20 lines to determine chapter type
            for k in range(i+1, min(i+25, len(lines))):
                stripped = lines[k].strip()
                if stripped.startswith('## Chapter '):
                    # Hit next chapter, stop
                    break
                if PLACEHOLDER_PATTERN.search(stripped):
                    has_placeholder_marker = True
                    break
                if stripped and not stripped.startswith('---') and not stripped.startswith('>'):
                    # Count prose words
                    if len(stripped.split()) > 10:
                        has_real_prose = True
                        break
            
            # If has real prose but marked placeholder, change to EXISTING
            if has_real_prose and not has_placeholder_marker:
                lines[i] = line.replace('[PLACEHOLDER]', '[EXISTING]')
                modified = True
                print(f'{ms.name}: {lines[i].strip()}')
    
    if modified:
        ms.write_text('\n'.join(lines))


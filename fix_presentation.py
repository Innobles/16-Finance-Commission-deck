import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Case Studies Slide
# Find the start and end of the Case Studies slide
start_idx = content.find('<!-- =================== SLIDE 14: CASE STUDIES =================== -->')
if start_idx != -1:
    end_idx = content.find('<!-- =================== SLIDE 15: SNA FUND FLOW =================== -->', start_idx)
    if end_idx != -1:
        # Remove the block entirely
        content = content[:start_idx] + content[end_idx:]

# 2. Fix missing line in SNA Diagram
content = content.replace('var(--green-light)', 'var(--green)')

# 3. Renumber slide IDs sequentially starting from s1
def replacer(m):
    replacer.count += 1
    active_str = m.group(1) if m.group(1) else ""
    return f'<div class="slide{active_str}" id="s{replacer.count}">'

replacer.count = 0
content = re.sub(r'<div class="slide( active)?"(?:[ \t]+id="s\d+")?>', replacer, content)

# 4. Update progress counter text correctly if needed? Wait Javascript handles that automatically (s.length)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Case studies removed. SNA line fixed. {replacer.count} slides renumbered.")

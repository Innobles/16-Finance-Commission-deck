import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

insert_idx = content.find('<!-- =================== SLIDE 13: PROOF OF WORK =================== -->')

new_slide = """    <!-- =================== SLIDE 13: COMPLIANCE BURDEN =================== -->
    <div class="slide">
        <div class="bg-glow glow-1 pulse"></div>
        <div class="bg-glow glow-3 pulse" style="animation-delay:1.5s"></div>
        <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;height:100%;text-align:center;padding:0 40px;">
            <div style="font-size:4.5rem;color:var(--axis);margin-bottom:30px;opacity:0.8;text-shadow:0 0 20px rgba(151,20,77,0.5)"><i class="fas fa-quote-left"></i></div>
            <h2 style="font-size:2.8rem;line-height:1.4;margin-bottom:30px;font-family:var(--font-head);font-weight:800;color:#fff;max-width:1050px;">
                “Every 16FC guideline is already mapped to a live module in our PLD Engine — <span class="highlight">reducing Axis Bank’s compliance burden to zero.</span>”
            </h2>
            <div style="margin-top:20px;display:flex;align-items:center;gap:12px;background:rgba(0,200,83,.1);padding:12px 24px;border-radius:100px;border:1px solid rgba(0,200,83,.3);">
                <i class="fas fa-shield-check" style="color:var(--green);font-size:1.2rem;"></i>
                <span style="color:var(--green-light);font-weight:700;letter-spacing:1px;font-size:0.9rem;text-transform:uppercase;">Turnkey 16FC Compliance Ready</span>
            </div>
        </div>
    </div>

"""
content = content[:insert_idx] + new_slide + content[insert_idx:]

# Renumber slide IDs sequentially starting from s1
def replacer(m):
    replacer.count += 1
    active_str = m.group(1) if m.group(1) else ""
    return f'<div class="slide{active_str}" id="s{replacer.count}">'

replacer.count = 0
content = re.sub(r'<div class="slide( active)?"(?:[ \t]+id="s\d+")?>', replacer, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Slide inserted and {replacer.count} slides renumbered.")

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <br /> inside h2.medium-text before the span
content = re.sub(r'<h2 class="medium-text(.*?)"(.*?)>(\s*.*?)(<br\s*/>|<br>)\s*<span', r'<h2 class="medium-text\1"\2>\3 <span', content, flags=re.DOTALL)

# Also reduce margin-bottom on h2 to save vertical space
content = content.replace('medium-text mb-8', 'medium-text mb-4')
content = content.replace('medium-text mb-6', 'medium-text mb-4')

# Optional: If padding of slides is too huge, let's just make sure the content fits better
# Slide 8 has too much text, so putting it on 1 line helps.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

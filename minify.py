import re

with open('index.dev.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract style block
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if style_match:
    css = style_match.group(1)
    # Minify CSS
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)  # remove comments
    css = re.sub(r'\s+', ' ', css)  # collapse whitespace
    css = re.sub(r'\s*{\s*', '{', css)
    css = re.sub(r'\s*}\s*', '}', css)
    css = re.sub(r'\s*:\s*', ':', css)
    css = re.sub(r'\s*;\s*', ';', css)
    css = re.sub(r'\s*,\s*', ',', css)
    css = css.strip()
    html = html[:style_match.start(1)] + css + html[style_match.end(1):]

# Extract script block
script_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if script_match:
    js = script_match.group(1)
    # Minify JS (basic - collapse whitespace, preserve strings)
    # Remove single-line comments (but not URLs with //)
    js = re.sub(r'(?<!:)//(?!/).*?$', '', js, flags=re.MULTILINE)
    # Remove multi-line comments
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    # Collapse whitespace
    js = re.sub(r'\n\s*\n', '\n', js)
    js = re.sub(r'  +', ' ', js)
    # Remove newlines around operators/braces
    js = re.sub(r'\s*\n\s*', ' ', js)
    js = js.strip()
    html = html[:script_match.start(1)] + js + html[script_match.end(1):]

# Minify HTML (collapse whitespace between tags)
# Remove HTML comments
html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
# Collapse whitespace between tags
html = re.sub(r'>\s+<', '><', html)
# Collapse remaining multi-line whitespace
lines = html.split('\n')
lines = [l.strip() for l in lines if l.strip()]
html = ''.join(lines)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Minified index.html ({len(html)} bytes)")

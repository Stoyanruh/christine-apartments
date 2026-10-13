"""Rebuild index.html for christineapartments.com from _build/template.html.

The template is the artifact version of the page (no <html>/<head> wrapper,
hero image as a __HERO__ data-URI placeholder). This script wraps it in a
full document, points the hero at hero-1899.jpg, and adds favicon/meta tags.
Run from the repo root:  python3 _build/build.py
"""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
t = (root / "_build" / "template.html").read_text(encoding="utf-8")

# hero: data URI -> file
t = t.replace('src="data:image/jpeg;base64,__HERO__"', 'src="hero-1899.jpg" width="1594" height="1293"')
assert "__HERO__" not in t

# email becomes a real mailto link on the hosted site
t = t.replace('<span class="email" id="email">christineapartments@outlook.com</span>',
              '<a class="email" id="email" href="mailto:christineapartments@outlook.com">christineapartments@outlook.com</a>')

head_end = t.index("</style>") + len("</style>")
head, body = t[:head_end], t[head_end:]

meta = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="canonical" href="https://christineapartments.com/">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="Christine Apartments">
<meta property="og:description" content="Historic apartments at 526 Niagara Street on Buffalo's West Side.">
<meta property="og:url" content="https://christineapartments.com/">
<meta property="og:image" content="https://christineapartments.com/hero-1899.jpg">
<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}a.email{text-decoration:none}</style>
"""
doc = "<!doctype html>\n<html lang=\"en\">\n<head>\n" + meta + head + "\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n"
(root / "index.html").write_text(doc, encoding="utf-8")
print("index.html", len(doc), "bytes")

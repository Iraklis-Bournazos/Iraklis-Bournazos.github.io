#!/usr/bin/env python3
"""
Build the site.

    python3 build.py

Reads the Markdown files in content/ and writes index.html and projects/*.html.
You should never need to edit HTML by hand — edit the files in content/ instead.
"""

import html as _html
import re
from pathlib import Path

import markdown
import yaml

SITE_URL = "https://iraklis-bournazos.github.io"

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
OUT_PROJECTS = ROOT / "projects"

MD = markdown.Markdown(extensions=["extra", "smarty", "toc"])


# --------------------------------------------------------------------------
# reading content files
# --------------------------------------------------------------------------

def read(path):
    """Split a Markdown file into (front-matter dict, rendered HTML body)."""
    raw = Path(path).read_text(encoding="utf-8")
    meta, body = {}, raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    MD.reset()
    return meta, MD.convert(body.strip())


def read_raw(path):
    """Same, but return the body as Markdown text rather than HTML."""
    raw = Path(path).read_text(encoding="utf-8")
    meta, body = {}, raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    return meta, body.strip()


def md(text):
    MD.reset()
    return MD.convert((text or "").strip())


def esc(text):
    """Escape plain-text fields (titles, meta lines) for safe HTML."""
    return _html.escape(str(text or ""), quote=True)


def md_inline(text):
    """Render a short string without wrapping it in <p>."""
    out = md(text)
    return re.sub(r"^<p>|</p>$", "", out.strip())


def split_h2(body_md):
    """Turn '## Title\\ntext' blocks into [(title, html), ...]."""
    items = []
    for chunk in re.split(r"^## ", body_md, flags=re.M):
        if not chunk.strip():
            continue
        title, _, rest = chunk.partition("\n")
        items.append((title.strip(), md(rest)))
    return items


# --------------------------------------------------------------------------
# small HTML helpers
# --------------------------------------------------------------------------

def tags_html(tags, muted=()):
    out = []
    for t in tags or []:
        cls = "tag muted" if t in muted else "tag"
        out.append(f'<span class="{cls}">{esc(t)}</span>')
    return "".join(out)


def page(title, description, body, depth=0, cv_page=False, canon=""):
    """Wrap body content in the shared page shell."""
    up = "../" * depth
    cls = ' class="cv-page"' if cv_page else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE_URL}/{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE_URL}/{canon}">
<meta property="og:image" content="{SITE_URL}/img/photo.jpg">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}style.css">
</head>
<body{cls}>

<div class="topbar">
  <div class="wrap">
    <a class="brand" href="{up}index.html">Iraklis Bournazos</a>
    <nav class="topnav">
      <a href="{up}index.html#work">Work</a>
      <a href="{up}index.html#background" class="hide-sm">Background</a>
      <a href="{up}cv.html">CV</a>
      <a href="{up}index.html#contact" class="hide-sm">Contact</a>
      <a href="https://github.com/Iraklis-Bournazos">GitHub</a>
    </nav>
  </div>
</div>

{body}

<footer>
  <div class="wrap">
    <span>Iraklis Bournazos — Stockholm</span>
    <span><a href="https://github.com/Iraklis-Bournazos">Source on GitHub</a></span>
  </div>
</footer>

</body>
</html>
"""


# --------------------------------------------------------------------------
# the pages
# --------------------------------------------------------------------------

def load_projects():
    projects = []
    for f in sorted((CONTENT / "projects").glob("*.md")):
        meta, body_md = read_raw(f)
        meta["slug"] = re.sub(r"^\d+-", "", f.stem)
        meta["body"] = md(body_md)
        meta["has_page"] = bool(body_md.strip())
        projects.append(meta)
    return projects


def build_home(projects):
    home_meta, home_body = read(CONTENT / "home.md")
    _, focus_md = read_raw(CONTENT / "focus.md")
    bg_meta, _ = read(CONTENT / "background.md")
    contact_meta, contact_body = read(CONTENT / "contact.md")

    focus = "".join(
        f"<div><h4>{title}</h4>{html}</div>"
        for title, html in split_h2(focus_md)
    )

    cards = []
    for p in projects:
        href = f'projects/{p["slug"]}.html' if p["has_page"] else p.get("link", "")
        tag = "a" if href else "div"
        attr = f' href="{href}"' if href else ""
        more = '<span class="more">Read more →</span>' if p["has_page"] else ""
        cards.append(f"""
    <{tag} class="project"{attr}>
      <p class="project-meta">{esc(p['meta'])}</p>
      <h3>{esc(p['title'])}</h3>
      <p class="blurb">{md_inline(p['summary'])}</p>
      <div class="tags">{tags_html(p.get('tags'), p.get('muted_tags', []))}{more}</div>
    </{tag}>""")

    edu = "".join(f"""
    <div class="edu-item">
      <div class="edu-when">{esc(e['when'])}</div>
      <div>
        <h3>{esc(e['title'])}</h3>
        <p class="where">{esc(e['where'])}</p>
        <p class="note">{md_inline(e['note'])}</p>
      </div>
    </div>""" for e in bg_meta.get("entries", []))

    links = "".join(
        f'<a class="btn{" primary" if i == 0 else ""}" href="{l["url"]}">{esc(l["label"])}</a>'
        for i, l in enumerate(contact_meta.get("links", []))
    )

    body = f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <img class="portrait" src="img/photo.jpg" alt="Iraklis Bournazos">
      <div>
        <p class="eyebrow">{esc(home_meta['location'])}</p>
        <h1>{esc(home_meta['name'])}</h1>
        <p class="role">{esc(home_meta['role'])}</p>
        {home_body}
        <div class="status"><span class="dot"></span>{md_inline(home_meta['status'])}</div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>What I work on</h2>
    <div class="focus">{focus}</div>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <h2>Selected work</h2>
    {"".join(cards)}
  </div>
</section>

<section id="background">
  <div class="wrap">
    <h2>Background</h2>
    {edu}
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <h2>Contact</h2>
    <div class="contact-text">{contact_body}</div>
    <div class="contact-row">{links}</div>
  </div>
</section>
"""
    (ROOT / "index.html").write_text(
        page(esc(home_meta["page_title"]), esc(home_meta["description"]), body, canon=""), encoding="utf-8"
    )


def build_project(p):
    links = ""
    if p.get("report"):
        links += (f'<a class="btn primary" href="../files/{p["report"]}">'
                  f'Read the full report (PDF)</a>')
    links += "".join(
        f'<a class="btn" href="{l["url"]}">{esc(l["label"])}</a>'
        for l in p.get("links", [])
    )
    body = f"""
<section class="hero project-hero">
  <div class="wrap">
    <a class="back" href="../index.html#work">← All work</a>
    <p class="project-meta">{esc(p['meta'])}</p>
    <h1>{esc(p['title'])}</h1>
    <p class="role">{md_inline(p['summary'])}</p>
    <div class="tags">{tags_html(p.get('tags'), p.get('muted_tags', []))}</div>
    {f'<div class="contact-row">{links}</div>' if links else ''}
  </div>
</section>

<section>
  <div class="wrap">
    <article class="prose">{p['body']}</article>
  </div>
</section>
"""
    OUT_PROJECTS.mkdir(exist_ok=True)
    (OUT_PROJECTS / f"{p['slug']}.html").write_text(
        page(esc(f"{p['title']} — Iraklis Bournazos"), esc(p["summary"][:150]), body,
             depth=1, canon=f"projects/{p['slug']}.html"),
        encoding="utf-8",
    )



def build_cv():
    cv, _ = read(CONTENT / "cv.md")
    qr = (ROOT / "img" / "qr.svg").read_text(encoding="utf-8")
    qr = re.sub(r"<\?xml[^>]*\?>", "", qr).strip()

    def entries(items):
        out = []
        for e in items:
            bullets = "".join(f"<li>{md_inline(b)}</li>" for b in e.get("bullets", []))
            notes = "".join(f"<li>{md_inline(n)}</li>" for n in e.get("notes", []))
            head = (f"{esc(e['role'])} <span class=\"at\">·</span> {esc(e['org'])}"
                    if "role" in e else f"{esc(e['degree'])}")
            sub = esc(e.get("org", "")) if "degree" in e else ""
            out.append(f"""
      <div class="cv-entry">
        <div class="cv-when">{esc(e['when'])}</div>
        <div class="cv-body">
          <h3>{head}</h3>
          <p class="cv-sub">{sub}{' · ' if sub else ''}{esc(e['place'])}</p>
          {f'<ul>{bullets}</ul>' if bullets else ''}
          {f'<ul class="tight">{notes}</ul>' if notes else ''}
        </div>
      </div>""")
        return "".join(out)

    projects = "".join(f"""
      <div class="cv-entry">
        <div class="cv-when">{esc(p['when'])}</div>
        <div class="cv-body">
          <h3>{esc(p['title'])}</h3>
          <p class="cv-sub">{esc(p['org'])}</p>
          <p class="cv-text">{md_inline(p['text'])}</p>
        </div>
      </div>""" for p in cv["projects"])

    skills = "".join(
        f'<p class="cv-skill"><b>{esc(s["group"])}</b> — {esc(s["items"])}</p>'
        for s in cv["skills"]
    )

    skills += f'<p class="cv-skill"><b>Languages</b> — {esc(cv["languages"])}</p>' 
    awards = "".join(f"<li>{md_inline(a)}</li>" for a in cv["awards"])

    body = f"""
<div class="cv-actions no-print">
  <span>Press <kbd>Cmd</kbd>+<kbd>P</kbd> and choose <em>Save as PDF</em> — the layout is set up for A4.</span>
  <button onclick="window.print()">Save as PDF</button>
</div>

<article class="cv">

  <header class="cv-head">
    <img class="cv-photo" src="img/photo.jpg" alt="">
    <div class="cv-id">
      <h1>{esc(cv['name'])}</h1>
      <p class="cv-tagline">{esc(cv['tagline'])}</p>
      <p class="cv-contact">
        {esc(cv['location'])} &nbsp;·&nbsp; {esc(cv['phone'])} &nbsp;·&nbsp;
        <a href="mailto:{esc(cv['email'])}">{esc(cv['email'])}</a><br>
        <a href="https://{esc(cv['site'])}">{esc(cv['site'])}</a> &nbsp;·&nbsp;
        <a href="https://{esc(cv['linkedin'])}">{esc(cv['linkedin'])}</a> &nbsp;·&nbsp;
        <a href="https://{esc(cv['github'])}">{esc(cv['github'])}</a>
      </p>
    </div>
    <div class="cv-qr">
      {qr}
    </div>
  </header>

  <p class="cv-summary">{md_inline(cv['summary'])}</p>

  <section class="cv-section"><h2>Experience</h2>{entries(cv['experience'])}</section>
  <section class="cv-section"><h2>Education</h2>{entries(cv['education'])}</section>
  <section class="cv-section"><h2>Selected projects</h2>{projects}</section>
  <section class="cv-section"><h2>Skills &amp; languages</h2>{skills}</section>

  <section class="cv-section">
    <h2>Awards &amp; scholarships</h2>
    <ul class="tight">{awards}</ul>
  </section>

</article>
"""
    (ROOT / "cv.html").write_text(
        page(f"CV — {esc(cv['name'])}", esc(cv["tagline"]), body, cv_page=True, canon="cv.html"),
        encoding="utf-8",
    )


def write_seo_files(projects):
    urls = ["", "cv.html"] + [f"projects/{p['slug']}.html" for p in projects if p["has_page"]]
    entries = "".join(f"  <url><loc>{SITE_URL}/{u}</loc></url>\n" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")


def main():
    projects = load_projects()
    build_home(projects)
    build_cv()
    write_seo_files(projects)
    built = 0
    for p in projects:
        if p["has_page"]:
            build_project(p)
            built += 1
    print(f"Built index.html, cv.html and {built} project pages.")
    print("Open index.html in your browser to check, then: git add -A && git commit -m 'update' && git push")


if __name__ == "__main__":
    main()

# Personal site

Source for [iraklis-bournazos.github.io](https://iraklis-bournazos.github.io).

## How to change the text

**You never edit HTML.** All the words live in `content/`:

| File | What it controls |
|---|---|
| `content/home.md` | Name, role line, the intro paragraphs, the status pill |
| `content/focus.md` | The three "What I work on" items |
| `content/background.md` | The education entries |
| `content/contact.md` | The contact paragraph and the buttons |
| `content/projects/*.md` | One file per project — short blurb *and* full page |

Edit the file, then:

```bash
python3 build.py        # regenerates index.html and projects/*.html
open index.html         # check it looks right
```

Happy with it? Publish:

```bash
git add -A
git commit -m "update projects"
git push
```

The live site updates about 30 seconds later.

## Adding a new project

Create a new file in `content/projects/`. The number prefix sets the order on the homepage.

```markdown
---
title: What the project was
meta: Where and when · 2026
summary: >
  One or two sentences. This is what shows on the homepage.
tags: [Python, LightGBM]
links:
  - label: Code on GitHub
    url: https://github.com/...
---

## A section heading

The full write-up. This becomes its own page. Write as much as you like —
markdown means **bold**, *italic*, lists, [links](https://example.com) and
`code` all work.
```

Then `python3 build.py`. That's it — the homepage card and the project page are both
generated. If you leave the body empty, the card links straight to the GitHub repo instead
of getting its own page.

## One-time setup on a new machine

```bash
pip3 install markdown pyyaml
```

## Files

```
content/          the words          <- you edit these
style.css         the design         <- edit to change colours/fonts
img/              images
build.py          the build script
index.html        GENERATED - do not edit
projects/*.html   GENERATED - do not edit
```

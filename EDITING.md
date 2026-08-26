# How to change the texts

Everything you can edit lives in `content/`. You never touch HTML.

## The loop

1. Open a file in `content/` and change the words.
2. Run the build:
   ```bash
   cd ~/Desktop/"Job finder "/personal-site
   python3 build.py
   ```
3. Look at it: `open index.html`
4. If you like it, publish: `git add -A && git commit -m "update" && git push`

Steps 1–3 take about ten seconds. Do them as often as you like — nothing is
published until step 4.

## Which file controls what

| I want to change... | Open this file |
|---|---|
| The intro paragraphs on the front page | `content/home.md` |
| My name, job title line, the "Currently at..." pill | `content/home.md` (top section) |
| The three "What I work on" boxes | `content/focus.md` |
| The education list | `content/background.md` |
| The contact paragraph and buttons | `content/contact.md` |
| Anything on the CV | `content/cv.md` |
| A project — both its card and its full page | `content/projects/NN-name.md` |

## Anatomy of a file

Every file has two parts, separated by `---` lines:

```markdown
---
title: Municipal-scale net load forecasting for Norway
meta: MSc thesis · rebase.energy & KTH · 2026
summary: >
  This short text is what appears on the FRONT PAGE card.
tags: [Python, LightGBM, Elhub AMI]
report: msc-thesis-net-load-forecasting-norway.pdf
---

## This is the full page

Everything below the second `---` becomes the project's own page.
Write as much as you want here.
```

- **Between the `---` lines** = settings. Keep the `name:` labels, change the values.
- **Below the second `---`** = the page text. Free writing.

### The `summary` field

The `>` means "a long line follows". Keep every line **indented by two spaces**:

```yaml
summary: >
  First line of the summary,
  and it continues here.
```

If you break that indentation the build will complain. That's the one rule that
catches people out.

## Writing the page text

Plain text works. When you want more:

```markdown
## A section heading

A normal paragraph. **Bold** and *italic* work.

- a bullet
- another bullet

[A link](https://example.com)

| Column | Column |
|---|---|
| value  | value  |
```

## Adding a project

Create a new file in `content/projects/`. The number at the front sets the order
on the front page — `08-my-project.md` appears last.

Copy an existing file and replace the contents. Leave the text below the `---`
empty and the front-page card links straight to GitHub instead of making its own
page.

## Adding a report PDF

1. Put the PDF in `files/projects/`
2. Add one line to the project's file:
   ```yaml
   report: my-report.pdf
   ```
3. `python3 build.py`

A "Read the full report (PDF)" button appears. If you mistype the filename the
build prints a **MISSING REPORT FILES** warning — read what it says.

## If something breaks

The build tells you what it didn't like. Two common ones:

- `yaml.scanner.ScannerError` → the settings block is misaligned. Check the
  indentation under a `>` line, and that every `label:` has a space after the colon.
- A `:` inside a value → wrap the whole value in quotes:
  `title: "Forecasting: a study"`

Nothing you do in `content/` can break the design. Worst case:

```bash
git checkout content/    # undo all uncommitted text changes
```

## Undoing a published change

```bash
git log --oneline        # find the version you liked
git revert <that-id>     # undo it
git push
```

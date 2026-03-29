# Publishing Guide

This repository is meant to be shareable without exposing personal job-search data.

## What Should Be Public

Recommended for public GitHub:

- `project-skill/`
- `README.md`
- `PUBLISHING.md`
- `LICENSE`
- `.gitignore`
- redacted examples

## What Should Stay Private

Keep these local or in a private repo:

- browser login profiles
- raw scraped datasets
- personal resume PDFs
- private spreadsheet workbooks
- personal market analysis reports

## Recommended Public Framing

This repository should be presented as:

`a reusable Codex skill pattern for job-market intelligence`

not as:

`a dump of one person's private job-search materials`

## Before You Push

Run:

```powershell
git status --short
```

Make sure you do not see:

- `profile/`
- `output/`
- `.env`
- resume PDFs
- xlsx workbooks
- raw csv exports

## Recommended Split

If you use this workflow long term, the cleanest setup is:

### Public repo

- reusable skill
- documentation
- redacted examples

### Private repo

- live datasets
- personal reports
- browser state
- resume materials
- workbook artifacts

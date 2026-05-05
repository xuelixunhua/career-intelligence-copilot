# Publishing Guide

This repository is meant to publish the reusable workflow, not a personal job-search archive.

## Publish

- skill instructions
- reference rules
- safe merge scripts
- sanitized examples
- generic setup documentation

## Keep Private

- browser profiles and cookies
- raw scraped postings
- master datasets from a real search
- generated market and personal-positioning reports
- resumes, interview notes, offer notes, compensation records
- private Excel workbooks

## Replacement Policy

When replacing an older public version, replace the content in this repository instead of creating a new GitHub project.

Before pushing, verify that the staged diff contains only the public layer:

```powershell
git status --short
git diff --cached --stat
git diff --cached --name-only
```

Stop before pushing if any of these appear:

- `profile/`
- `output/`
- `tmp/`
- `private/`
- real resumes
- real reports
- real datasets
- browser cache or account files
- personal salary or offer notes

## Suggested Public Structure

```text
project-skill/
scripts/
examples/
README.md
PUBLISHING.md
LICENSE
.gitignore
```

## Suggested Private Structure

```text
profile/
output/
tmp/
private/
workbook.xlsx
resume/
interviews/
offers/
```

The public repository explains how the system works. The private workspace contains the user's data.

# Career Intelligence Copilot

A project-local Codex skill for turning job search research into a repeatable workflow.

Instead of treating job scraping, market analysis, company ranking, and resume optimization as separate tasks, this repository packages them into one reusable skill-driven pipeline.

## What It Does

This repository is designed for workflows like:

1. Collect job postings from real websites with a browser-first approach
2. Maintain a deduplicated master dataset
3. Analyze market structure, compensation, company types, and role patterns
4. Reverse-engineer resume strategy from real job samples
5. Rank companies based on both market quality and personal fit
6. Sync conclusions back into a spreadsheet or decision board

## Why This Is Not Just Another Scraper Repo

Most repos stop at `crawl -> dump csv`.

This one is built around a broader loop:

`collect -> dedupe -> analyze -> interpret -> personalize -> update decision system`

That makes it much more useful for:

- recurring weekly job-market tracking
- resume iteration based on real demand
- role clustering and company ranking
- keeping one long-lived personal research workspace

## Repository Structure

```text
career-intelligence-copilot/
├── README.md
├── PUBLISHING.md
├── LICENSE
├── .gitignore
├── examples/
│   └── power-trading-case.md
└── project-skill/
    └── career-intelligence-copilot/
        ├── README.md
        ├── SKILL.md
        └── references/
            ├── file-map.md
            ├── workbook-rules.md
            ├── real-role-derived-guidance.md
            └── adaptation-guide.md
```

## Recommended Positioning

This repo is intentionally generic.

It can be used for:

- power trading roles
- product roles
- strategy roles
- data roles
- operations roles
- other domain-specific hiring markets

The current power trading workflow is just one strong example, not a hard limitation.

## The Core Skill

The reusable skill lives in `project-skill/career-intelligence-copilot/`.

Its job is to help Codex treat the following as one connected pipeline:

- job collection
- master dataset maintenance
- market analysis
- company filtering
- resume reverse-engineering
- workbook updates

## How To Use It

### Option 1: Use It Inside a Project

Open the repository in Codex and ask for tasks such as:

```text
Use the career-intelligence-copilot skill to update my latest job dataset,
refresh the market analysis, and tell me which companies are most worth targeting.
```

```text
Use the skill to reverse-engineer my resume against the latest real job postings
and tell me what skills, projects, and positioning I should strengthen next.
```

```text
Use the skill to deduplicate this week's new postings into the master dataset
and add a new execution date column for longitudinal analysis.
```

### Option 2: Adapt It To Your Own Workspace

Copy `project-skill/career-intelligence-copilot/` into your own project and update:

- input file paths
- output file paths
- workbook sheet rules
- platform scope
- filtering logic

See `references/adaptation-guide.md` for the fastest way to do that.

## Design Principles

### 1. Browser First

Use real browser interaction for websites that require login, dynamic rendering, or anti-bot friction.

### 2. Real Job Evidence First

Company ranking and resume recommendations should come from real job samples, not generic career advice.

### 3. Decision System, Not Notes

The spreadsheet or workbook should be maintained as a reusable decision board, not a rough scratchpad.

### 4. Local Privacy By Default

This repo is structured so you can publish the method without publishing:

- browser profiles
- personal resumes
- raw job datasets
- private reports

## Current Example Use Case

The repository includes a concrete example based on Beijing power trading roles:

- Boss / Liepin job collection
- company deduplication
- market analysis
- company ranking
- resume reverse-engineering

See `examples/power-trading-case.md`.

## Suggested GitHub Metadata

Repository name ideas:

- `career-intelligence-copilot`
- `job-market-intelligence-copilot`
- `resume-market-copilot`

Suggested subtitle:

`A Codex skill for job-market scraping, company ranking, and resume reverse-engineering from real job postings.`

Suggested topics:

- `codex-skill`
- `career-intelligence`
- `job-market`
- `resume`
- `browser-automation`
- `research-workflow`

## Publishing Advice

For a public repository, publish:

- the skill
- the workflow rules
- the documentation
- redacted examples

Do not publish:

- `profile/`
- `output/`
- personal resumes
- private spreadsheets
- raw scraped datasets tied to personal accounts

See `PUBLISHING.md` for a release checklist.

# PATCH: Personal continuation

This repository was copied from the collaborative hackathon project
[lamek-tsegay/patch](https://github.com/lamek-tsegay/patch).
The original README documents component ownership and contributions.
This personal continuation is not a claim of sole authorship.

## What works without credentials

- SQLite-backed findings and ranked proposals
- Demo repository and seeded example vulnerabilities
- Policy evaluation and audit event generation
- React dashboard demo data and local development UI
- Automated tests for proposals and approval-gated patch writing

## What needs external services

- Nemotron scanning and fix generation require a running NIM endpoint and
  an API key supplied through environment variables.
- Opening pull requests requires a GitHub token with access to the target
  repository. Set GITHUB_REPO explicitly; there is no default that could
  accidentally write to the original team's repository.
- Human approval must be supplied explicitly to commit_fix_approved.
  Calling the function without approval never writes to GitHub.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
cd dashboard && npm install && npm run dev
```

Use .env.example as a template. Never commit your .env or tokens.

## Import notes

The source was transferred through GitHub's text-file API, which does not
support transferring the upstream PNG asset. The file
dashboard/src/assets/hero.png is not present in this copy.
All other text-based tracked source files were imported.

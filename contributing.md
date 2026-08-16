# Contribution Guidelines

Please note that this project is released with a [Contributor Code of Conduct](code_of_conduct.md). By participating in this project you agree to abide by its terms.

## Pull requests

- Always open PRs from a new branch. Do not commit to `main`.
- One addition (or one focused fix) per pull request.
- New categories belong in a separate pull request from item additions.
- Search the list first. Duplicates will be closed.
- Use the pull request template. Fill in the link, section, and why the item is awesome.

## Adding an item

- Fit the item into an existing section. [Open a suggestion](https://github.com/kzndotsh/awesome-discordpy/issues/new/choose) before proposing a new section.
- Add it at the bottom of that section.
- Link the **GitHub repo** (or gist). Do not link PyPI, docs sites, or homepages unless there is no public repo.
- The project should be more than 30 days old, documented, and maintained.
- Archived, deprecated, or unmaintained projects belong in [archived.md](archived.md), not the main list.
- If something similar is already listed, say in the PR why yours is better or distinct.
- Star count is not a hard cutoff. Empty stubs and abandoned repos will be rejected.

Format:

```md
- [item name](https://github.com/owner/repo) - Description.
```

- Description starts with a capital letter and ends with a period.
- Do not start the description with "A" or "An".
- Do not use marketing taglines.
- Do not repeat "discord.py" in the description; it is implied.
- Keep it short and specific about what the reader gets.
- Check spelling and grammar.
- Do not add last-activity dates by hand. A weekly GitHub Action stamps `(last activity YYYY-MM)` onto GitHub, gist, and PyPI links. Locally: `python .github/scripts/update_activity_dates.py` (set `GITHUB_TOKEN` if you hit rate limits).

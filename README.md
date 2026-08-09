# Big Walk Guide

A static English game-wiki site for the cooperative online adventure **Big Walk** (House House / Panic), built for the "overseas game hot-word station" challenge.

## Live URL

- Cloudflare Pages: https://big-walk-guide-3nr.pages.dev (canonical)
- GitHub Pages: https://jiachen-ludens.github.io/big-walk-guide/

GitHub repo: https://github.com/Jiachen-Ludens/big-walk-guide

## Why Big Walk

Selection was based on the keyword judgment submissions from the 2026-08 Shengcai navigation cohort (task 87388), analyzed from 102 of 135 submissions that had been image-extracted:

- **Big Walk** was the most frequent "doable" keyword among classmates: 24 mentions, 22 judged doable.
- Student-reported metrics clustered at KD 8-27 (SimilarWeb/Ahrefs), with 889+ suggested subkeywords and a clear long-tail gap (puzzle solutions, tower guides, walkthrough, achievements, crossplay).
- Verification confirmed the opportunity: the game launched August 4, 2026 at $19.99 with a 25% launch discount, scored 94 on Metacritic (PC) at launch, and mature wiki coverage (Fandom etc.) was not yet established.
- The island-exploration puzzle game has a rich, well-documented long-tail: red bridge, red tower, yellow maze, green tower, chairlift, coordinate puzzle, achievements.

Other frequently judged doable keywords: Mistfall Hunter (18 doable mentions), Beast of Reincarnation (10), Sephiria (13), Fields of Mistria (12), Corsair Cove (9).

## Site Pages

15 pages, all facts linked to verified sources (verified August 8, 2026):

- index.html
- walkthrough.html
- red-bridge.html
- red-tower.html
- yellow-maze.html
- green-tower.html
- chairlift.html
- coordinate-puzzle.html
- achievements.html
- backpack.html
- crossplay.html
- release-date.html
- tips.html
- faq.html
- sources.html

## Deploy

Static HTML/CSS, no build step. Deployed with GitHub Pages (legacy build from `main`).

## Update Flow

Cloudflare Pages uses direct upload; after changing site files:

```bash
cd /Users/weijiachen/.codex/skills/game-wiki-builder
CLOUDFLARE_API_TOKEN="$TOKEN" CLOUDFLARE_ACCOUNT_ID="c712eb2c173cd2b62b0a3acc80115ea7" \
  scripts/deploy_pages.sh /Users/weijiachen/出海学习/big-walk-guide big-walk-guide
```

GitHub Pages (legacy build from `main`) rebuilds automatically on push:

```bash
git add -A
git -c commit.gpgsign=false commit -m "update"
git push origin main
```

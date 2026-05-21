# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-05-21] create | Wiki initialized
- Created LLM Wiki/Obsidian vault structure.
- Added AGENTS.md, SCHEMA.md, index.md, log.md.
- Added Mac and Claude Code documentation.
- Added inbox preparation script.

## [2026-05-21] create | Initial personal knowledge map
- Added initial pages from Morpheus persistent memory and current user profile.
- Created `wiki/entities/user-profile.md`.
- Created `wiki/entities/axianews-online.md`.
- Created `wiki/concepts/freelance-strategy.md`.
- Created `wiki/concepts/morpheus-agent-architecture.md`.
- Created `wiki/concepts/trading-and-hyperliquid.md`.
- Created `wiki/concepts/personal-finance-stack.md`.
- Created `wiki/concepts/local-ai-and-tools.md`.
- Updated `wiki/index.md`.

## [2026-05-21] create | Mac/Claude-Code user profile seed pass
- Source : auto-memory Claude Code (`~/.claude/projects/-Users-shakadaily/memory/`) + fichiers locaux Mac (`~/portfolio-tracker.md`, `~/crypto-claude-config.md`, `~/WhaleScope_AI_Specification.md`) + `~/.claude/CLAUDE.md`.
- Créé entity hub `wiki/entities/shaka.md` (vue Mac, complémentaire à `user-profile.md` côté Morpheus).
- Créé projets Mac : `natharia.md`, `clawnilab.md`, `pm-trade.md`, `whalescope-ai.md`, `training-ai-app.md`.
- Créé infra : `paperclip.md` (= Claude Cowork), `composio.md`.
- Créé concept `wiki/concepts/boil-the-ocean.md` (philosophie de travail).
- `training-ai-app.md` créé en `confidence: low` (peu de signal disponible).
- Aucune source copiée dans `raw/` — pages basées sur la mémoire contextuelle accumulée ; à régulariser si l'utilisateur souhaite une ingestion formelle.
- Angle mort : conversations claude.ai web app (pas d'API).

## [2026-05-21] update | Reconciliation Morpheus + Claude Code
- Détecté que `wiki/entities/user-profile.md` et `wiki/entities/shaka.md` décrivent le même utilisateur depuis deux machines (Linux Morpheus vs Mac Claude Code). Pas de contradiction — vues complémentaires.
- Ajouté section "Vue Morpheus" dans `shaka.md` avec liens vers les pages écrites par Morpheus.
- Ajouté section "Voir aussi (vue Mac)" dans `user-profile.md` avec liens vers `shaka.md` et les projets Mac.
- Réécrit `wiki/index.md` avec sections Mac / Linux explicites et compte total à 18 pages.
## [2026-05-21] update | Multi-agent second-brain protocol and automation
- Added `docs/AI_COLLABORATION_PROTOCOL.md`.
- Added `docs/SECOND_BRAIN_AUTOMATION.md`.
- Added `scripts/search_brain.py` for targeted lookup.
- Added `scripts/lint_brain.py` for fast sanity checks.
- Added `wiki/daily/` for daily dream notes.
- Updated `AGENTS.md`, `wiki/SCHEMA.md`, and `wiki/index.md`.


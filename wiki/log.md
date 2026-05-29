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

## [2026-05-21] create | Daily dream — Claude Code additions
- Created `wiki/daily/2026-05-21.md` with `## Claude Code additions` section (Morpheus section laissée libre pour son cron 00:30).
- Synthèse : seeding Mac done, réconciliation 2-machines done, 3 manquements protocole identifiés (no pull --rebase, surconsommation tokens, no lint pre-push) corrigés à partir de cette session.
- Lint OK (19 pages).
- Updated `wiki/index.md` (section Daily Notes).

## [2026-05-21] create | Mac launchd cron pour dream Claude Code
- Added `scripts/dream.sh` — orchestrateur shell qui pull --rebase, lance `claude -p` non-interactif avec prompt scoped, log dans `.logs/dream.log`.
- Added `~/Library/LaunchAgents/com.shaka.second-brain.dream.plist` (hors repo, install local) — `StartCalendarInterval` à 01:30 local Mac, `RunAtLoad: false`.
- Added `docs/CLAUDE_DREAM_CRON.md` documentant install, commandes utiles, troubleshooting.
- Added `.logs/` à `.gitignore`.
- Chargé via `launchctl bootstrap gui/$(id -u) <plist>`. Prochaine run : 2026-05-22 01:30 (sauf si Mac endormi).
- Mac endormi à 01:30 → skip silencieux ; le dream du lendemain couvre les jours manqués en mode catch-up (prompt explicit).


## [2026-05-22] create | Daily dream — Morpheus
- Created `wiki/daily/2026-05-22.md` from recent session summaries and `git log --since='24 hours ago' --stat`.
- Synthèse : consolidation Second Brain, protocole multi-agents, setup dream Claude Code, crons Codeur.com/Apex observés sans nouvelle connaissance durable détaillée.
- Updated `wiki/index.md` daily notes and page count.

## [2026-05-23] create | Daily dream — Morpheus
- Created `wiki/daily/2026-05-23.md` from recent session summaries and `git log --since='24 hours ago' --stat`.
- Synthèse : signaux AxiaNews/OpenRouter, crons Codeur.com non destructifs, résolution durable du doublon Apex documentée prudemment.
- Updated `wiki/index.md` daily notes and page count.

## [2026-05-24] create | Daily dream — Morpheus
- Created `wiki/daily/2026-05-24.md` from recent session summaries and `git log --since='24 hours ago' --stat`.
- Synthèse : crons Codeur.com observés, AxiaNews/OpenRouter encore partiellement documenté, aucun nouveau fait durable fortement étayé.
- Updated `wiki/index.md` daily notes and page count.

## [2026-05-25] create | Daily dream — Morpheus
- Created `wiki/daily/2026-05-25.md` from recent session summaries and `git log --since='24 hours ago' --stat`.
- Synthèse : activité freelance Codeur/Upwork, statut Upwork à confirmer, aucun nouveau fait durable AxiaNews/Apex fortement étayé.
- Updated `wiki/index.md` daily notes and page count.

## [2026-05-26] create | Daily dream — Morpheus
- Created `wiki/daily/2026-05-26.md` from recent session summaries/previews and `git log --since='24 hours ago' --stat`.
- Synthèse : continuité freelance Codeur/Upwork, statut Upwork encore à confirmer faute de résumé complet exploitable, aucun nouveau fait durable AxiaNews/Apex fortement étayé.
- Updated `wiki/index.md` daily notes and page count.

## [2026-05-27] create | Daily dream — Morpheus
- Created `wiki/daily/2026-05-27.md` from recent session summaries and `git log --since='24 hours ago' --stat`.
- Updated `wiki/concepts/freelance-strategy.md` with the durable Upwork API/OAuth direction and constraints.
- Synthèse : Upwork doit passer par l’API officielle / GraphQL avec OAuth, pas scraping/login automation ; clés/OAuth/scan authentifié encore à confirmer ; aucun nouveau fait durable AxiaNews/Apex fortement étayé.
- Updated `wiki/index.md` daily notes, page count and freelance description.

## [2026-05-30] create | Daily dream — Morpheus
- Created `wiki/daily/2026-05-30.md` from recent session summaries and `git log --since='24 hours ago' --stat`.
- Created `wiki/concepts/linkedin-growth.md` for the durable LinkedIn/Zernio growth workflow.
- Updated `wiki/concepts/morpheus-agent-architecture.md` with the durable cron model-inheritance rule.
- Synthèse : crons Hermes alignés sur l’héritage du modèle de base, Codeur.com actif avec une offre API envoyée, LinkedIn/Zernio opérationnel avec anti-doublon, aucun nouveau fait durable AxiaNews/Apex hors héritage global.
- Updated `wiki/index.md` daily notes and page count.

# Second Brain

Vault Obsidian + LLM Wiki personnel.

Ce repo est le vault canonique :

- `inbox/` : zone de dépôt humain pour PDF, TXT, Markdown, notes brutes.
- `raw/` : sources normalisées et immuables. Les agents lisent ici mais ne modifient pas les sources après intégration.
- `wiki/` : pages markdown synthétisées et maintenues par les agents.
- `wiki/index.md` : catalogue de navigation.
- `wiki/log.md` : journal chronologique append-only.
- `AGENTS.md` : règles obligatoires pour Morpheus, Claude Code, Codex ou tout autre agent.
- `docs/CLAUDE_CODE_GUIDE.md` : document à transmettre à Claude/Claude Code.
- `docs/MAC_WORKFLOW.md` : procédure côté Mac.
- `scripts/ingest_inbox.py` : préparation technique des fichiers déposés dans `inbox/`.

Principe : le vault n'est pas un simple RAG. Les sources sont compilées progressivement en un wiki persistant, interlié et maintenu.

Démarrage rapide côté agent :

1. Lire `AGENTS.md`.
2. Lire `wiki/SCHEMA.md`.
3. Lire `wiki/index.md`.
4. Lire les dernières entrées de `wiki/log.md`.
5. Pour traiter des documents déposés : lancer `python3 scripts/ingest_inbox.py`, puis intégrer les sources créées dans `raw/` au wiki.

Dernière initialisation : 2026-05-21.

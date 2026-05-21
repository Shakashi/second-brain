# AI Collaboration Protocol — Second Brain

Ce document est destiné à Claude, Claude Code, Codex, Morpheus, Marcus, Apex et tout autre agent qui collabore sur ce vault.

## Résumé en une phrase

Ne charge pas tout le second-brain. Synchronise le repo, lis l'index, cherche seulement ce dont tu as besoin, modifie proprement, puis commit/push.

## Chemin canonique

Sur la machine Morpheus :

```bash
/home/shaka/second-brain
```

Sur Mac, chemin recommandé :

```bash
~/Documents/second-brain
```

Repo :

```text
https://github.com/Shakashi/second-brain
```

## Protocole obligatoire au début d'une tâche

Si la tâche touche l'utilisateur, ses projets, ses agents, ses préférences, ses décisions ou son historique :

1. Se placer à la racine du vault.
2. Synchroniser :

```bash
git pull --rebase
```

Si des changements locaux existent, ne pas écraser brutalement. Committer ou stash selon le cas.

3. Lire :

```text
AGENTS.md
wiki/SCHEMA.md
wiki/index.md
```

4. Lire les entrées récentes :

```bash
tail -80 wiki/log.md
```

5. Chercher ciblé au lieu de tout charger :

```bash
python3 scripts/search_brain.py "termes de recherche"
```

ou :

```bash
rg -i "terme" wiki raw docs
```

6. Lire uniquement les pages pertinentes.

## Quand consulter le second-brain

Consulter le vault quand la tâche concerne :

- stratégie personnelle ou business ;
- AxiaNews ;
- Apex / trading / HyperLiquid ;
- Codeur.com / freelance ;
- finance personnelle ;
- préférences utilisateur ;
- architecture d'agents ;
- décisions prises précédemment ;
- documents déposés dans `inbox/`.

Ne pas consulter pour une question triviale sans dépendance au contexte utilisateur.

## Règle de consommation token

Ne jamais charger tout `wiki/` sauf instruction explicite.

Ordre recommandé :

1. `wiki/index.md` — carte du vault.
2. `scripts/search_brain.py "query"` — recherche ciblée.
3. Pages pertinentes uniquement.
4. `raw/` seulement si la page synthétique ne suffit pas ou si une source doit être vérifiée.

## Modifier le vault

Après toute modification :

1. Mettre à jour `wiki/index.md` si une page est créée, renommée ou changée significativement.
2. Ajouter une entrée dans `wiki/log.md`.
3. Préserver le frontmatter YAML.
4. Utiliser des wikilinks Obsidian.
5. Vérifier :

```bash
python3 scripts/lint_brain.py
```

6. Commit/push :

```bash
git status --short
git add .
git commit -m "Update second brain: sujet"
git push
```

## Ingestion de documents

Les documents humains vont dans :

```text
inbox/
```

Puis :

```bash
python3 scripts/ingest_inbox.py
```

Ensuite l'agent doit faire l'intégration cognitive : résumer, créer/mettre à jour les pages, lier, indexer, loguer.

## Dream quotidien

Le "dream" est une synthèse quotidienne : l'agent relit les signaux récents, les commits, les logs et éventuellement ses conversations récentes, puis écrit une page durable dans `wiki/daily/`.

But : condenser ce qui mérite d'être conservé, détecter décisions/questions ouvertes, et alimenter le second-brain sans tout recopier.

Règles :

- une page par jour ;
- ne pas inclure de secrets ;
- ne pas inventer ;
- citer les pages/commits/sources utiles ;
- créer des liens vers les pages existantes ;
- si une information mérite une page dédiée, créer ou mettre à jour cette page.

## Collaboration multi-agents

Morpheus est l'orchestrateur central. Marcus/AxiaNews et Apex doivent consulter le second-brain seulement pour leur domaine, pas charger tout le vault.

Claude Code doit suivre ce document avant toute modification du vault.

Si plusieurs agents travaillent le même jour :

- Morpheus dream : vers 00:30.
- Claude dream : idéalement 01:00 ou 01:30.
- Chaque agent doit `git pull --rebase` avant de travailler.
- En cas de conflit, préserver les notes humaines et demander arbitrage si ambigu.

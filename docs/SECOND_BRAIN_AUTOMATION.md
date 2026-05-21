# Second Brain Automation

## Objectif

Garder le vault synchronisé et produire une synthèse quotidienne utile, sans charger tout le second-brain dans chaque conversation.

## Sync automatique

Le vault est synchronisé via GitHub.

Sur Mac : Obsidian Git fait pull au démarrage, backup/commit/push périodique.

Sur Morpheus : les jobs cron doivent toujours commencer par :

```bash
cd /home/shaka/second-brain
git pull --rebase
```

## Backup existant

Un backup chiffré quotidien Morpheus existe déjà à minuit via cron Hermes :

```text
Morpheus encrypted daily backup — 0 0 * * *
```

Le dream Morpheus doit tourner après ce backup, à 00:30.

## Dream Morpheus

Horaire recommandé :

```text
30 0 * * *
```

Tâche :

1. Pull latest.
2. Lire `AGENTS.md`, `wiki/SCHEMA.md`, `wiki/index.md`, `wiki/log.md` récent.
3. Utiliser `session_search` pour résumer les conversations récentes de la journée précédente.
4. Lire les commits Git des dernières 24h.
5. Créer ou mettre à jour :
   - `wiki/daily/YYYY-MM-DD.md`.
6. Ajouter dans la page :
   - résumé exécutif ;
   - décisions ;
   - projets touchés ;
   - pages créées/modifiées ;
   - questions ouvertes ;
   - prochaines actions suggérées.
7. Mettre à jour `wiki/index.md` si nécessaire.
8. Ajouter `wiki/log.md`.
9. Commit/push.

## Dream Claude Code

Horaire suggéré :

```text
0 1 * * *
```

ou :

```text
30 1 * * *
```

Claude doit lire `docs/AI_COLLABORATION_PROTOCOL.md` et compléter la page quotidienne sans dupliquer Morpheus. Il peut ajouter une section :

```markdown
## Claude Code additions
```

## Anti-patterns

- Ne pas copier toute la conversation brute dans le daily.
- Ne pas écrire des secrets.
- Ne pas créer une page pour chaque micro-événement.
- Ne pas réécrire `raw/`.
- Ne pas faire de dream concurrent à Morpheus sans `git pull --rebase`.

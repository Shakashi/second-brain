# AGENTS.md — Second Brain Operating Rules

Ce fichier est obligatoire pour tout agent qui lit ou modifie ce vault : Morpheus, Claude Code, Codex, OpenCode, etc.

## Mission

Maintenir un wiki personnel persistant selon le pattern LLM Wiki : les sources brutes sont conservées, puis les informations importantes sont compilées dans des pages markdown interliées, versionnées et cumulatives.

## Orientation obligatoire au début de chaque session

Avant toute modification :

1. Lire `wiki/SCHEMA.md`.
2. Lire `wiki/index.md`.
3. Lire les 20 dernières entrées de `wiki/log.md`.
4. Chercher dans le vault avant de créer une nouvelle page, pour éviter les doublons.

## Structure

- `inbox/` : dépôt temporaire de nouveaux documents par l'utilisateur.
- `raw/` : sources normalisées, immuables après ingestion technique.
  - `raw/articles/` : articles web ou exports markdown.
  - `raw/papers/` : PDFs et papiers.
  - `raw/texts/` : textes libres, notes, transcriptions.
  - `raw/assets/` : images et pièces jointes.
- `wiki/` : pages maintenues par les agents.
  - `wiki/entities/` : personnes, organisations, produits, lieux, projets.
  - `wiki/concepts/` : concepts, thèmes, méthodes, idées.
  - `wiki/comparisons/` : comparaisons structurées.
  - `wiki/queries/` : réponses/synthèses importantes issues de questions.
  - `wiki/sources/` : résumés par source.
  - `wiki/_meta/` : cartes, taxonomie, rapports de lint.
  - `wiki/_archive/` : pages archivées.

## Règles critiques

- Ne jamais modifier une source dans `raw/` après sa création. Les corrections vont dans `wiki/`.
- Ne jamais supprimer une source brute sans instruction explicite de l'utilisateur.
- Chaque page wiki doit avoir un frontmatter YAML valide.
- Utiliser des wikilinks Obsidian `[[Nom de page]]` pour relier les pages.
- Mettre à jour `wiki/index.md` à chaque création de page.
- Ajouter une entrée append-only dans `wiki/log.md` à chaque ingest, query, lint ou changement notable.
- Quand une nouvelle information contredit une page existante, ne pas écraser silencieusement : documenter les deux versions avec dates/sources, mettre `contested: true` si nécessaire.
- Les tags utilisés doivent exister dans la taxonomie de `wiki/SCHEMA.md`.
- Préférer des pages courtes et maintenables. Scinder au-delà d'environ 200 lignes.

## Consultation ciblée du second-brain

Pour toute tâche dépendant du contexte utilisateur/projets, ne charge pas tout le vault. Fais plutôt :

1. `git pull --rebase` depuis la racine.
2. Lire `wiki/index.md`.
3. Chercher ciblé avec `python3 scripts/search_brain.py "query"`.
4. Lire uniquement les pages pertinentes.
5. Si tu modifies le vault, lancer `python3 scripts/lint_brain.py`, puis commit/push.

Voir `docs/AI_COLLABORATION_PROTOCOL.md` pour le protocole complet multi-agents.

## Workflow d'ingestion d'un document dans `inbox/`

1. Lancer `python3 scripts/ingest_inbox.py` depuis la racine du repo.
2. Le script copie/convertit les documents vers `raw/` et ajoute un frontmatter source.
3. Lire chaque nouvelle source dans `raw/`.
4. Créer ou mettre à jour une page dans `wiki/sources/` avec :
   - résumé factuel ;
   - points clés ;
   - entités/concepts détectés ;
   - questions ouvertes ;
   - liens vers pages existantes ou nouvelles.
5. Mettre à jour les pages `wiki/entities/`, `wiki/concepts/`, `wiki/comparisons/` pertinentes.
6. Mettre à jour `wiki/index.md`.
7. Ajouter une entrée dans `wiki/log.md` avec les fichiers modifiés.
8. Commit Git avec un message explicite.

## Workflow de question/réponse

1. Lire `wiki/index.md`.
2. Chercher les mots-clés dans `wiki/` et `raw/` si nécessaire.
3. Lire les pages pertinentes.
4. Répondre avec citations vers les pages ou sources : `[[page]]`, `raw/...`.
5. Si la réponse est durablement utile, la sauvegarder dans `wiki/queries/` ou `wiki/comparisons/`.
6. Loguer l'action.

## Nommage

- Fichiers : lowercase, tirets, extension `.md`.
- Pas d'espaces dans les noms de fichiers.
- Titre humain dans le frontmatter `title:`.
- Exemple : `wiki/concepts/llm-wiki.md` avec `title: LLM Wiki`.

## Frontmatter minimal des pages wiki

```yaml
---
title: Example Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | source-summary | meta
tags: [tag]
sources: [raw/texts/example.md]
confidence: high | medium | low
contested: false
---
```

## Git

- Faire des commits petits et lisibles.
- Pull avant de travailler si le repo peut avoir changé ailleurs.
- Ne pas committer de secrets, clés privées, tokens, exports confidentiels non voulus.
- En cas de conflit Git, ne pas résoudre agressivement : préserver le contenu humain et signaler les fichiers concernés si ambigu.

## Commandes utiles

```bash
# Préparer les documents déposés dans inbox/
python3 scripts/ingest_inbox.py

# Voir les changements
git status --short

# Chercher dans le wiki
rg "mot-clé" wiki raw

# Commit classique
git add .
git commit -m "Ingest sources: sujet"
git push
```

# Guide pour Claude / Claude Code — Second Brain

Ce document peut être copié dans Claude ou ouvert par Claude Code.

## Objectif

Tu travailles dans un vault Obsidian appelé `second-brain`, organisé selon le pattern LLM Wiki. Ton rôle est de maintenir un wiki persistant, pas de répondre uniquement depuis des chunks éphémères.

## Règle absolue

Avant toute modification :

1. Lis `AGENTS.md`.
2. Lis `wiki/SCHEMA.md`.
3. Lis `wiki/index.md`.
4. Lis les dernières entrées de `wiki/log.md`.
5. Fais une recherche dans le vault avant de créer une page.

## Structure

- `inbox/` : documents déposés par l'utilisateur.
- `raw/` : sources préparées et immuables.
- `wiki/` : pages de connaissance maintenues par agents.
- `wiki/sources/` : résumé par source.
- `wiki/entities/` : personnes, organisations, produits, projets.
- `wiki/concepts/` : idées, thèmes, méthodes.
- `wiki/comparisons/` : comparaisons.
- `wiki/queries/` : réponses utiles conservées.
- `wiki/index.md` : index à maintenir.
- `wiki/log.md` : journal append-only.

## Pour intégrer des documents déposés

Depuis la racine du repo :

```bash
python3 scripts/ingest_inbox.py
```

Ensuite, pour chaque nouveau fichier dans `raw/` :

1. Lis la source.
2. Crée un résumé dans `wiki/sources/`.
3. Mets à jour les pages concept/entity existantes.
4. Crée de nouvelles pages seulement si elles passent les seuils de `wiki/SCHEMA.md`.
5. Ajoute les pages à `wiki/index.md`.
6. Ajoute une entrée dans `wiki/log.md`.
7. Commit et push.

## Format d'une page wiki

```markdown
---
title: Titre
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [concept]
sources: [raw/texts/source.md]
confidence: medium
contested: false
---

# Titre

Résumé clair.

## Points clés

- ...

## Sources

- `raw/texts/source.md`

## Liens

- [[Autre Page]]
```


## Politique Git

```bash
git pull --rebase
git status --short
git add .
git commit -m "Ingest: sujet"
git push
```

Si conflit : préserver les modifications humaines et demander arbitrage si nécessaire.

## Ce qu'il ne faut pas faire

- Ne pas modifier les fichiers dans `raw/` après création.
- Ne pas écrire dans `inbox/processed/` sauf pour archivage technique.
- Ne pas créer des dizaines de pages pour des mentions mineures.
- Ne pas laisser une page nouvelle hors de `wiki/index.md`.
- Ne pas oublier `wiki/log.md`.

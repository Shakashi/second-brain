---
title: Ingestion Workflow
created: 2026-05-21
updated: 2026-05-21
type: meta
tags: [meta, inbox, source, automation]
sources: []
confidence: high
contested: false
---

# Ingestion Workflow

Cette page décrit le flux d'intégration des documents.

## Dépôt

Déposer les fichiers dans `inbox/` :

- `.pdf`
- `.txt`
- `.md`
- `.markdown`

## Préparation technique

Depuis la racine du repo :

```bash
python3 scripts/ingest_inbox.py
```

Le script :

- convertit les PDFs en markdown texte via `pdftotext` ;
- copie les textes/markdown ;
- ajoute un frontmatter raw avec hash ;
- place les fichiers préparés dans `raw/papers/` ou `raw/texts/` ;
- déplace les originaux traités dans `inbox/processed/`.

## Intégration cognitive par agent

Après préparation, un agent doit :

1. Lire la source créée dans `raw/`.
2. Chercher les pages existantes pertinentes.
3. Créer une page résumé dans `wiki/sources/`.
4. Mettre à jour les pages `wiki/entities/` et `wiki/concepts/` pertinentes.
5. Ajouter des wikilinks.
6. Mettre à jour `wiki/index.md`.
7. Ajouter une entrée dans `wiki/log.md`.
8. Commit + push.

## Important

Le script ne remplace pas l'analyse LLM. Il prépare les fichiers pour ingestion. La synthèse, les contradictions et les liens doivent être faits par l'agent.

## Pages liées

- [[second-brain-overview|Second Brain Overview]]

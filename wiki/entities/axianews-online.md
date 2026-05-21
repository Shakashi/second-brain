---
title: AxiaNews Online
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [project, axianews, ai, automation, business]
sources: []
confidence: medium
contested: false
---

# AxiaNews Online

AxiaNews est un projet de site visant à récupérer des news depuis de nombreuses plateformes, les agréger, produire des articles agnostiques et factuels, puis attribuer une note de pertinence basée sur la qualité, le nombre et la convergence des sources ainsi que la stabilité des détails.

## Objectif produit

- Collecter des sources multiples.
- Regrouper les événements similaires.
- Extraire des faits structurés.
- Rédiger des articles neutres.
- Vérifier la fiabilité et la cohérence.
- Publier des contenus en anglais.
- Optimiser la monétisation sans dégrader la qualité éditoriale.

## Infrastructure connue

- Repo local : `/home/shaka/axianews-online/repo`.
- Base de données : `axianews-pg`.
- Déploiement Hostinger via SSH sur `public_html`.
- Agent CEO : Marcus, profil `axianews-ceo`.
- Marcus est isolé avec son propre bot/profil/topic.

## Agents AxiaNews

La mémoire mentionne des compétences spécialisées :

- source discovery ;
- story clustering ;
- fact extraction ;
- neutral writer ;
- fact-check reviewer ;
- reliability scorer ;
- publisher ;
- monetization ;
- CEO v3.

## Règles opérationnelles connues

- Cycle propre de publication en anglais uniquement.
- Éviter OpenRouter pour le moment ; privilégier Codex/OAuth avec Ollama local en fallback.

## Liens

- [[user-profile|User Profile]]
- [[morpheus-agent-architecture|Morpheus Agent Architecture]]

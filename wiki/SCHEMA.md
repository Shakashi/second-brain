# Wiki Schema

## Domain

Second brain personnel généraliste : projets, apprentissages, recherche, décisions, stratégie, références, santé/psychologie si l'utilisateur choisit d'en ajouter, et toute connaissance utile à conserver durablement.

## Philosophy

Ce vault suit le pattern LLM Wiki : compiler la connaissance au fur et à mesure au lieu de la redécouvrir à chaque question.

- `raw/` = source de vérité immuable.
- `wiki/` = synthèse maintenue et interliée.
- `wiki/index.md` = carte de navigation.
- `wiki/log.md` = historique append-only.

## Conventions

- Fichiers en minuscules avec tirets : `nom-de-page.md`.
- Chaque page wiki contient un frontmatter YAML.
- Chaque page importante doit contenir au moins deux wikilinks sortants quand c'est possible.
- Chaque nouvelle page est ajoutée à `wiki/index.md`.
- Chaque action notable est ajoutée à `wiki/log.md`.
- Les paragraphes de synthèse doivent citer les sources avec `Sources` ou des références inline vers `raw/...`.
- Les sources brutes ne sont pas modifiées après ingestion.

## Frontmatter wiki

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | source-summary | meta
tags: [tag]
sources: [raw/path/source.md]
confidence: high | medium | low
contested: false
---
```

## Frontmatter raw

```yaml
---
title: Source Title
source_type: pdf | text | markdown | article | other
source_file: original-file-name.ext
source_url:
ingested: YYYY-MM-DD
sha256: body-hash
status: raw
---
```

## Tag taxonomy

Ajouter ici les nouveaux tags avant usage.

### Meta
- meta
- inbox
- source
- query
- synthesis
- contradiction
- decision
- daily

### Personal knowledge
- personal
- goals
- health
- psychology
- learning
- productivity
- finance

### Work/projects
- project
- business
- strategy
- technical
- architecture
- ai
- automation
- security
- trading
- axianews

### Research
- research
- paper
- book
- article
- concept
- entity
- comparison

## Page thresholds

Créer une page quand :

- une entité ou un concept est central dans une source ; ou
- il apparaît dans au moins deux sources ; ou
- l'utilisateur pose une question dont la réponse mérite d'être conservée ; ou
- la page servira de hub utile pour relier plusieurs notes.

Ne pas créer de page pour une simple mention passagère.

## Update policy

Quand une nouvelle source contredit une page existante :

1. Comparer les dates et la fiabilité des sources.
2. Garder les deux affirmations si le conflit est réel.
3. Marquer `contested: true`.
4. Ajouter une section `Contradictions / points à vérifier`.
5. Ajouter l'élément au prochain lint.

## Lint policy

Périodiquement vérifier :

- liens cassés ;
- pages orphelines ;
- pages absentes de l'index ;
- tags hors taxonomie ;
- sources raw modifiées après ingestion ;
- pages avec `confidence: low` ;
- pages trop longues ;
- contradictions non résolues.

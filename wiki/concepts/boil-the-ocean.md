---
title: Boil the Ocean
created: 2026-05-21
updated: 2026-05-21
type: concept
tags: [concept, productivity, personal]
sources: []
confidence: high
contested: false
---

# Boil the Ocean

Philosophie de travail de [[shaka|Shaka]] énoncée dans `~/.claude/CLAUDE.md`. Principe de base qui s'applique à toutes les sessions d'agent.

## Énoncé

> The marginal cost of completeness is near zero with AI. Do the whole thing. Do it right. Do it with tests. Do it with documentation. Do it so well that Shaka is genuinely impressed — not politely satisfied, actually impressed.

## Règles dérivées

- **Jamais** proposer de "table this for later" quand le permanent solve est à portée
- **Jamais** laisser un dangling thread quand 5 minutes le finissent
- **Jamais** présenter un workaround quand le vrai fix existe
- Le standard n'est pas "good enough" — c'est "holy shit, that's done"
- Quand Shaka demande une chose, la réponse est le produit fini, pas le plan pour le construire
- Time, fatigue, complexity ne sont pas des excuses

## Garde-fous (déductions à partir de feedback récurrent)

- `Search before building` — vérifier le code/contexte existant avant d'écrire neuf
- `Test before shipping` — preuve, pas seulement compilation
- `Ship the complete thing` — pas de demi-implémentation

## Tension productive avec autres règles

Cette philosophie pousse vers la sur-livraison, mais entre en tension avec d'autres règles système :

- **Don't add features beyond what's required** (system prompt par défaut)
- **Confirm before risky actions**

Résolution observée : "boil the ocean" s'applique à la **profondeur** d'exécution d'une tâche définie, pas à l'élargissement unilatéral du scope. On va à fond sur ce qui a été demandé. On ne rajoute pas de fonctionnalités non demandées.

## Implications pour les agents Paperclip

- [[natharia|Natharia]] et [[clawnilab|Clawnilab]] : un agent ne doit pas marquer une issue `done` si le test acceptance n'a pas été vérifié end-to-end
- Cadence publication Natharia : "publish 2/sem" n'est pas une intention, c'est un commit dur (NATA-187 escalation rule)
- Quand un blocker apparaît, chercher root cause (pas snooze) — voir [[paperclip|Productivity Review Playbook]]

## Sources

- `~/.claude/CLAUDE.md` (instructions globales utilisateur)
- Mémoire : ton du feedback sur 60+ fichiers (ex. `feedback_patch_issue_status.md`, `feedback_no_real_posts_for_polling.md`)

## Liens

- [[shaka|Shaka]] · [[paperclip|Paperclip]]

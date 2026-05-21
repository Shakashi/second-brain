---
title: Paperclip
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [entity, automation, ai, architecture]
sources: []
confidence: high
contested: false
---

# Paperclip

Plateforme d'orchestration multi-agents utilisée par [[shaka|Shaka]]. Connue commercialement comme "Claude Cowork". Backend des companies [[natharia|Natharia]] (namespace `NATA-XXX`) et [[clawnilab|Clawnilab]] (namespace `CLA-XXX`).

## Modèle conceptuel

- **Company** : conteneur racine (Natharia, Clawnilab)
- **Agent** : exécutant scoped à une company avec un `role_key` (`ceo`, `cmo`/Editor, `engineer`, `designer`/Visualist)
- **Issue** : unité de travail (todo / in_progress / in_review / blocked / done / cancelled)
- **Routine** : agent qui tourne sur cron (`* * * * *`)
- **Productivity Review** : issue auto-créée quand un trigger se déclenche (long_active_duration, no_comment_streak, high_churn)
- **Interaction** : `request_confirmation`, `wake_assignee` — pause d'agent attendant action board

## Localisation locale

- `~/Developpement/Paperclip/` (config + master files)
- Sessions Claude Code des instances : `~/.claude/projects/-Users-shakadaily--paperclip-instances-default-...`

## Règle critique : statut hygiène

> Après toute action d'agent sur une issue, **PATCHER le statut**. Un commentaire seul ne suffit pas.

Pattern fréquent observé : agent documente "blocked on X" en commentaire mais laisse `status: in_progress`. La review se déclenche correctement et c'est attendu. Voir [[#|Productivity Review Playbook]] ci-dessous.

## Productivity Review Playbook (CEO)

Quand une review est assignée :

1. Lire l'état réel de l'issue source via `/api/issues/{id}` — ne pas faire confiance au trigger aveuglément
2. Réconcilier commentaires vs statut
3. Vérifier si le blocker nommé existe encore (souvent résolu pendant que l'agent restait actif)
4. Action corrective **sur l'issue source**, pas juste sur la review :
   - Unblock + reroute (`status: todo` + commentaire next action)
   - OU marquer proprement `blocked` avec `blockedByIssueIds`
   - OU cancel si superseded
5. Fermer la review avec une décision manager : trigger validité, comportement agent, action prise, outcome attendu

**Faux positifs structurels** : si un child a un `request_confirmation` non résolu (board attendu), le parent est correctement `in_progress` et le `long_active_duration` est un artefact → close-productive sans toucher le statut.

## Routines actives connues

### Natharia
| Routine ID | Schedule | Assigné | Action |
|---|---|---|---|
| `a564924d-5524-463c-99a8-7c41313d19ab` | `2 6 * * *` UTC | Engineer | Call `/api/kpi/send-report` (safety net) |
| `c4183161-888f-47a7-981f-1d22af43201c` | `12 6 * * *` UTC | CEO | Lire `/api/kpi/latest` et poster sur NATA-67 |
| NATA-261 routine | hebdo lundi | CEO | Weekly snapshot |

### Clawnilab
| Routine | Schedule | Action |
|---|---|---|
| CLA-31 proposal send | Lundi 2026-05-25 06:00 UTC | Envoi proposal Phase 1 |

## Contraintes / pièges

- API `/api/companies/{id}/users` renvoie 404 → impossible de réassigner à un utilisateur humain via `assigneeUserId`
- Réutiliser un agent v1 terminé renvoie `Cannot assign work to terminated agents`
- KPI cloud routine `trig_01LKyYSfKgMfixH1sHj95WER` sur claude.ai retirée 2026-05-15
- Triggers de review peuvent boucler si le root cause est externe à Paperclip (ex. Codex API quota → NATA-67 a généré 5 recoveries successives avant fix 2026-05-11 = reassign au CEO)

## Mention "Cowork"

Quand l'utilisateur dit "Claude Cowork", lire "Paperclip". Les transcripts locaux des agents sont accessibles dans `~/.claude/projects/-Users-shakadaily--paperclip-instances-*`.

## Sources

- Auto-memory : `daily_kpi_routine.md`, `natharia_agent_ids.md`, `productivity_review_playbook.md`, `productivity_review_routine_parent.md`, `NATA-67_recovery_loop_root_cause.md`, `kpi_route_quirks.md`, `NATA-376_blocked_triage.md`
- Filesystem : `~/Developpement/Paperclip/`, `~/.claude/projects/-Users-shakadaily--paperclip-instances-*`

## Liens

- [[natharia|Natharia]] · [[clawnilab|Clawnilab]] · [[shaka|Shaka]]

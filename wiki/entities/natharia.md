---
title: Natharia
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [project, business, automation, ai]
sources: []
confidence: high
contested: false
---

# Natharia

Newsletter et site d'affiliation centrés sur les outils IA marketing, opérés par une équipe d'agents autonomes orchestrés via [[paperclip|Paperclip]]. Domaine : `natharia.com`. Propriétaire : [[shaka|Shaka]].

## Modèle économique

- **Revenu** : affiliation (Make.com, Notion, Beehiiv, Writesonic, AppSumo, Airtable, etc.)
- **Funnel** : trafic → popup newsletter → Beehiiv → email de nurture avec liens affiliés
- **Cible MRR** : $100/mois — initialement visé fin mai 2026, maintenant projeté **fin juillet 2026**
- **MRR actuel (2026-05-18)** : ~$3.15 (placeholder, traité <$25 comme pré-revenu)

## Équipe d'agents (v2 — depuis 2026-05-14)

| Rôle | Agent ID | Responsabilité |
|---|---|---|
| CEO | `0ce116ec-efee-48a1-9f02-72b93c9704fd` | Stratégie, weekly review, escalades |
| Editor | `3451dc89-9b3c-4ab1-a6d6-d82ac37206c5` | Articles, social, copy |
| Visualist | `1e8e277b-b4b2-4fc8-951e-3e1c813f1c47` | Visuels Instagram, illustrations |
| Engineer | `13ffdd3e-8ee2-474d-8b4a-f016d76827f5` | Code, infra, API, KPI cron |

L'équipe v1 (CMO, CTO, ContentDirector, ImageAgent) est **terminée** depuis le reset NATA-293 (2026-05-14) — l'API rejette toute assignation à ces IDs.

## Stack technique

- **Frontend / API** : Next.js sur Vercel
- **DB** : Supabase (table `daily_reports`, table abonnés)
- **Newsletter** : Beehiiv (free plan — seul `/subscribers` est exposé en API ; draft/send sont Enterprise)
- **Email transactionnel** : Resend (nécessite header `User-Agent` custom + `curl`, pas Python urllib — Cloudflare 1010)
- **Cron** : Vercel cron `2 6 * * *` UTC → `GET /api/kpi/send-report`
- **Node** : 22.x (upgrade obligatoire depuis 2026-05-15 — Supabase SDK 2.105.3 a drop Node 20)

## Cadence de publication

- **Standing rule (NATA-187)** : 2 articles par semaine, Lundi + Jeudi
- CEO escalade le jour même si gap > 3 jours sans contenu
- 29 articles publiés au 2026-05-18 (vérifié via `sitemap.xml`)

## Pipeline KPI quotidien

1. `2 6 * * *` UTC — Vercel cron appelle `/api/kpi/send-report` (gen + store + email)
2. `2 6 * * *` UTC — Routine Paperclip Engineer `a564924d-5524-463c-99a8-7c41313d19ab` (safety net)
3. `12 6 * * *` UTC — Routine Paperclip CEO `c4183161-888f-47a7-981f-1d22af43201c` poste le rapport sur NATA-67
4. Fallback manuel : `curl -sS "https://natharia.com/api/kpi/send-report?generate=true&password=natharia2026"`

Cloud routine `trig_01LKyYSfKgMfixH1sHj95WER` sur claude.ai **retirée** 2026-05-15 (redondante).

## Newsletter

- Plateforme : Beehiiv
- Workflow : Editor rédige → board copie-colle dans Beehiiv (pas d'API send sur le plan gratuit)
- Auth NATA-22/233 : Bearer token, send testé OK
- État funnel : opérationnel depuis 2026-05-11 (NATA-203/231/262/271)

## Distribution

- **Site / SEO** : 29 articles dans le sitemap ; `best-ai-project-management-tools-2026` = page non-home n°1 (5 vues/7j)
- **Twitter** : @Natharia2030, 5 followers — reads Composio bloqués (v3 API), focus posts standalone + follows
- **Instagram** : 2 followers — **bloqué app-level depuis 2026-05-08** (NATA-305, subcode 2207051), unblock = appel développeur côté board uniquement

## Contraintes connues

- Composio v3 : POST writes OK avec `x-user-api-key`, mais `TWITTER_USER_LOOKUP_ME` et autres reads renvoient 401 → fallback métriques connues
- Beehiiv free : send côté board, pas d'automation API
- Replies Twitter sur compte 0-follower : 403 systématiques (NATA-205) → stratégie pivotée sur engagement organique + threads communautaires

## Issues clés (Paperclip — namespace NATA)

- **NATA-67** : KPI log permanent (toujours ouvert par design)
- **NATA-22** : Newsletter Issue #1 — clos 2026-05-09
- **NATA-203 / 231 / 262 / 271** : funnel newsletter (clos)
- **NATA-293** : v2 team reset (clos 2026-05-14)
- **NATA-305** : Meta IG restriction — bloqué (board action requise)

## Snapshots récents

- [[#|Weekly 2026-05-18]] : funnel unlocked (0→6 subs), clics 7j en chute (34→11), traffic est le constraint
- Pré-snapshot 2026-05-11 : 15 articles, 54 clics lifetime, funnel encore fermé

## Sources

- Auto-memory : `natharia_agent_ids.md`, `weekly_snapshot_2026-05-18.md`, `daily_kpi_routine.md`, `NATA-293_v2_reset.md`, `NATA-305_meta_ig_restriction.md`, `newsletter_funnel_verified.md`, et ~30 autres dans `~/.claude/projects/-Users-shakadaily/memory/`
- Paperclip live : `https://natharia.com/NATA/issues/`

## Liens

- [[shaka|Shaka]] (propriétaire) · [[paperclip|Paperclip]] (plateforme) · [[composio|Composio]] (intégrations)
- Voisin business : [[clawnilab|Clawnilab]]

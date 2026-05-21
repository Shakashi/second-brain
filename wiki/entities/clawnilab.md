---
title: Clawnilab
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [project, business, automation]
sources: []
confidence: high
contested: false
---

# Clawnilab

Second business de [[shaka|Shaka]] : service de design visuel solo, opéré comme un solopreneurship via un agent CEO unique sur [[paperclip|Paperclip]] (namespace `CLA-XXX`). Domaine : `clawnilab.com`.

## Modèle

- Service freelance — délivrables visuels (covers, banners, illustrations)
- Canal d'acquisition principal : **Fiverr** ([gig actif](https://www.fiverr.com/s/0b4KXd2))
- Upwork : pas de credentials sync — workflow d'upload manuel par board

## Identité

- **Email pro** : `info@clawnilab.com`
- **SMTP** : `smtp.hostinger.com:465` SSL — credentials dans `/Users/shakadaily/Developpement/Paperclip/CLAWNILAB-MASTER-FILE.md`
- **Pattern Python** : `smtplib.SMTP_SSL` + `EmailMessage.add_attachment(maintype="image", subtype="png")`
- **Subject convention** : `[CLAWNILAB - INFO] <topic>`

## Board contact (= Shaka)

- Recipient : `sylvaincrypto@protonmail.com`
- Confirmed dans CLA-19 unblock 2026-05-13
- Paperclip n'expose pas `/api/companies/{id}/users` (404) → impossible de réassigner à Shaka via `assigneeUserId`

## Workflow marketplace (Fiverr / Upwork)

Patterns adoptés car aucun API public d'édition de gig n'existe :

1. Agent CEO produit l'asset localement
2. Asset attaché à l'issue Paperclip
3. Email board avec PJ + action 5-points
4. Board upload manuel UI + screenshot reply
5. Agent envoie follow-up `[CLAWNILAB - INFO] <X> live`

**Règle** : ne pas rester en `blocked` >24h sur action board — le daily wake stalle l'issue.

## Phase actuelle (2026-05-21)

- **Phase 1** active selon `STRATEGY_ROADMAP.md`
- Phases 2-4 **gated** sur seuils (reply rate ≥5% pour invalider H1 etc.)
- **Proposal** drafted, send queué via routine Paperclip Lundi **2026-05-25 06:00 UTC** (CLA-31)

## Source de vérité stratégie

- **`STRATEGY_ROADMAP.md`** (standalone) : sections clés
  - §4 — 5 catégories de bans ("Ce qu'on ne fait PAS")
  - §5 — Phase 1 active, 2-4 gated
  - §6 — thresholds (reply rate ≥5%)
  - §7 — RULES-001 à 005
- Extrait 2026-05-20 du `CLAWNILAB-MASTER-FILE.md` + emails board UID 217/220/226/235/239/246
- Pre-flight obligatoire (HEARTBEAT step 0.5 Strategic Awareness) avant toute proposition d'axe acquisition / pivot / hire / infra

## Issues clés (Paperclip — namespace CLA)

- **CLA-19** : status hygiene fix (clos productive 2026-05-15)
- **CLA-22 / 23** : blockers historiques
- **CLA-25** : productivity review (clos productive 2026-05-15)
- **CLA-31** : Phase 1 proposal queued (envoi Lundi 2026-05-25)

## Contraintes connues

- Pas de `.env.clawnilab` sur disque (cherché `$HOME` 2026-05-15)
- Pas de `FIVERR_*` / `UPWORK_*` en runtime agent
- Marketplaces = human-only jusqu'à arrivée creds → email-handoff par défaut

## Sources

- Auto-memory : `clawnilab_board_workflow.md`, `clawnilab_strategy_roadmap.md`, `CLA-25_productivity_review.md`, `CLA-31_proposal_queued.md`
- Fichier vivant : `/Users/shakadaily/Developpement/Paperclip/CLAWNILAB-MASTER-FILE.md`, `/Users/shakadaily/Developpement/Paperclip/STRATEGY_ROADMAP.md`

## Liens

- [[shaka|Shaka]] (propriétaire) · [[paperclip|Paperclip]] (plateforme)
- Voisin business : [[natharia|Natharia]]

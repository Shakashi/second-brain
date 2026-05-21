---
title: WhaleScope AI
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [project, ai, automation, trading]
sources: []
confidence: medium
contested: false
---

# WhaleScope AI

Projet de [[shaka|Shaka]] : alertes crypto whales sur Twitter avec analyse IA contextuelle ("WHY it matters, not just WHAT happened"). **Statut : spécification écrite, pas encore construit** (au 2026-05-21).

## Pitch

- **Tagline** : *Smart whale alerts that tell you WHY it matters, not just WHAT happened*
- **Différenciation** :
  - @whale_alert (1.5M followers) : alertes brutes, zéro contexte
  - @lookonchain (500K+) : analyse manuelle, pas scalable
  - WhaleScope : combine vitesse + profondeur via IA
- **Audience** : crypto traders actifs, DeFi users, memecoin traders, global anglophone

## Identité visuelle (spec)

- Couleurs : `#1DA1F2` (bleu Twitter), `#FFB81C` (or bearish), `#31A24C` (vert bullish)
- Logo : silhouette baleine + cerveau/circuit
- Tone : pro, data-driven, jamais hype

## Architecture cible

```
Blockchain Monitors (ETH/SOL/Base/BSC)
  → Transaction Classifier (exchange/whale/smart money)
  → Whale DB (SQLite ou Supabase) + Smart Money Tracker
  → AI Analysis Engine (Claude API primary, OpenAI fallback)
  → Tweet Formatter & Publisher (Twitter API v2)
  → Distribution : Twitter + Telegram premium + Analytics dashboard
```

### Stack envisagé

- ETH + Base : Alchemy RPC
- Solana : Helius webhook
- DB : SQLite local OU Supabase free tier
- IA : Claude API (primary), OpenAI (fallback)
- Twitter : API v2 free tier (1500 posts/mois)

## Roadmap monétisation (spec)

| Phase | Mois | Levier | Revenu cible |
|---|---|---|---|
| 1 | M1-M2 | Audience 5K–10K followers | $0 |
| 2 | M2-M3 | Telegram premium $49/mois × 50-100 | $2.4–4.9k/mois |
| 3 | M3-M6 | Affiliés + sponsorships | $1–3k/mois |
| 4 | M6+ | API premium $99-499/mois | $0.5–2k+/mois |

## Stratégie contenu (spec)

- Alertes 40% (immédiat si >$5M, batch 30 min sinon)
- Smart Money Monday 8%
- Whale Watch Wednesday 8%
- Friday Flows 8%
- Engagement 12% / Éducation 8% / Updates 8% / Tendances 8%
- Résumé daily 09:00 UTC

## Risques / questions ouvertes

- Compte Twitter dédié ? — ou réutiliser un existant comme @Natharia2030 (non recommandé : audience différente)
- Capacité free tier Twitter (1500 posts/mois) → ~50/jour, contraignant à hauteur d'audience cible
- Coûts Alchemy/Helius à scale ?
- Bootstrap audience initial : pas de stratégie spec écrite

## Sources

- Spec complète : `~/WhaleScope_AI_Specification.md` (volumineuse, ~35k tokens)

## Liens

- [[shaka|Shaka]] (propriétaire) · [[pm-trade|pm-trade]] (projet trading voisin)

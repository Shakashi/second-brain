---
title: Shaka
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [personal, entity]
sources: []
confidence: high
contested: false
---

# Shaka

Propriétaire de ce vault. Solopreneur, opérateur multi-projets, utilisateur intensif d'agents LLM (Claude Code, Claude Cowork/Paperclip, Codex). Profil orienté exécution autonome : on monte des systèmes qui tournent sans supervision continue.

## Identité opérationnelle

- **Email principal** : `sylvaincrypto@protonmail.com`
- **Compte X / Twitter** : [@Natharia2030](https://twitter.com/Natharia2030) (id `2047240750664925184`) — le seul compte Twitter relié à Composio
- **Machine** : macOS (Darwin 25.5.0), shell zsh
- **Email pro Clawnilab** : `info@clawnilab.com` (SMTP Hostinger)
- **Workspace Composio** : `sylvaincrypto_workspace` (`ok_gbe7HgdBzdvG`) — voir [[composio|Composio]]

## Projets actifs

| Projet | Page | État | Mode opératoire |
|---|---|---|---|
| Newsletter + affiliate AI marketing | [[natharia|Natharia]] | LIVE (6 subs, ~$3 MRR) | 4 agents Paperclip autonomes, Mon/Thu cadence |
| Service design solo (Fiverr) | [[clawnilab|Clawnilab]] | Phase 1 | 1 agent CEO, email-handoff vers board |
| Bot trading Polymarket | [[pm-trade|pm-trade]] | LIVE (~$272 portfolio) | Script Python quotidien 08:00 UTC |
| Crypto whale alerts (planifié) | [[whalescope-ai|WhaleScope AI]] | Spec écrite, pas construit | Solo, multi-chain |
| Coaching fitness IA | [[training-ai-app|training-ai-app]] | Early stage | Node + Prisma |

## Stack & outils

- **Orchestration agents** : [[paperclip|Paperclip / Claude Cowork]] pour Natharia et Clawnilab
- **Intégrations** : [[composio|Composio]] (Twitter, Instagram, Supabase, GitHub, Vercel, Canva)
- **Hébergement** : Vercel (Natharia), Hostinger (DNS + SMTP Clawnilab), Supabase (DB + auth)
- **Newsletter** : Beehiiv
- **Email transactionnel** : Resend
- **Trading on-chain** : Polymarket (Polygon), Hyperliquid, wallets Solana + Base + Polygon
- **IDE knowledge** : Obsidian + ce vault `second-brain`

## Principes de travail

- [[boil-the-ocean|Boil the ocean]] est la règle de base : finir, pas planifier. Pas de "on verra plus tard".
- Préfère les systèmes autonomes (routines cron + agents Paperclip) aux interventions manuelles répétées.
- Tolère 0 secret en clair dans le repo ; les clés sont en `.env` locaux ou variables Vercel.
- Recadrage rapide quand un agent dévie — feedback corrigés deviennent règles persistantes en mémoire.

## Cadence & rituels

- **Daily KPI Natharia** : routine Paperclip Engineer 06:02 UTC + CEO 06:12 UTC, posté sur NATA-67 (voir [[natharia|Natharia]])
- **Daily report trading** : 08:00 UTC, append dans `~/crypto-claude-config.md`
- **Weekly snapshot Natharia** : lundi (NATA-261 routine)
- **Weekly Clawnilab proposal review** : board valide via email

## Conventions appliquées par défaut

- Réponses concises sauf demande inverse.
- Ne jamais déclencher d'action publique (tweet, IG post, email) pendant une session de debug ou de polling — voir `feedback_no_real_posts_for_polling.md` en mémoire.
- Toujours PATCH le statut Paperclip après action (un commentaire seul ne suffit pas).
- En cas de productivity review Paperclip : appliquer le [[paperclip|playbook]] (corriger la source, fermer le review, jamais snooze sans raison structurelle).

## Hors-projets

- Crypto perso : ~$272 portefeuille actif (PM + Solana + Base + Hyperliquid locked) — détails dans `~/portfolio-tracker.md` et `~/crypto-claude-config.md`.
- Historique : appartement Rawai (Thaïlande), validators Ethereum, exploration Solana memecoins.

## Vue Morpheus (machine Linux `/home/shaka/`)

Le vault est aussi alimenté depuis une autre machine où l'orchestrateur s'appelle **Morpheus** (Linux). Cette perspective ajoute des projets complémentaires non couverts depuis le Mac :

- [[user-profile|User Profile]] — vue alternative du même utilisateur depuis Morpheus.
- [[axianews-online|AxiaNews Online]] — plateforme news agrégées, CEO = agent **Marcus**.
- [[morpheus-agent-architecture|Morpheus Agent Architecture]] — orchestrateur Morpheus + agents Apex (trading) + Marcus (news).
- [[freelance-strategy|Freelance Strategy]] — positionnement Codeur.com Pro, missions full-stack.
- [[trading-and-hyperliquid|Trading and HyperLiquid]] — agent Apex côté HL (distinct de [[pm-trade]] côté Polymarket).
- [[personal-finance-stack|Personal Finance Stack]] — Firefly III local + Kubera bridge.
- [[local-ai-and-tools|Local AI and Tools]] — Ollama (phi4-mini, qwen2.5:7b, deepseek-r1:7b), outils pentest.

Les deux machines convergent vers ce vault via Git. Quand les pages décrivent le même fait avec un écart, marquer `contested: true`.

## Sources

- Auto-memory Claude Code : `~/.claude/projects/-Users-shakadaily/memory/MEMORY.md` et 60+ fichiers dérivés
- Global CLAUDE.md : `~/.claude/CLAUDE.md`
- Fichiers locaux : `~/portfolio-tracker.md`, `~/crypto-claude-config.md`, `~/WhaleScope_AI_Specification.md`
- Session directe avec Shaka (2026-05-21)

## Liens

- [[natharia|Natharia]] · [[clawnilab|Clawnilab]] · [[pm-trade|pm-trade]] · [[whalescope-ai|WhaleScope AI]] · [[training-ai-app|training-ai-app]]
- [[paperclip|Paperclip]] · [[composio|Composio]]
- [[boil-the-ocean|Boil the ocean]]

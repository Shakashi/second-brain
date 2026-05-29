---
title: Morpheus Agent Architecture
created: 2026-05-21
updated: 2026-05-30
type: concept
tags: [ai, automation, architecture, technical]
sources: []
confidence: medium
contested: false
---

# Morpheus Agent Architecture

Morpheus est l'orchestrateur central de l'utilisateur. Les autres agents sont spécialisés et isolés par profil, bot et topic.

## Principes

- Morpheus = interface centrale et coordination.
- Apex = agent trading.
- Marcus = CEO AxiaNews.
- Chaque agent niveau 3 doit disposer de son propre bot Telegram, profil Hermes et topic dédié.
- L'utilisateur exige une isolation complète entre agents.
- Les cron jobs Hermes doivent hériter du modèle de base du profil, sauf consigne explicite de pin modèle/provider. Cela évite de corriger chaque job séparément quand le modèle de base change.
- Les `last_error` historiques d’un cron peuvent mentionner d’anciens modèles ; vérifier la configuration active avant de conclure qu’un job est encore mal configuré.

## Agents connus

### Morpheus

- Orchestrateur central.
- Répond directement à l'utilisateur dans cette conversation CLI ou dans le topic Morpheus.
- Doit coordonner les autres agents sans confondre leurs responsabilités.

### Apex

- Agent trading.
- Profil, bot et topic isolés.
- Workdir connu : `/home/shaka/.openclaw/workspace-apex`.
- Voir [[trading-and-hyperliquid|Trading and HyperLiquid]].

### Marcus

- CEO AxiaNews.
- Bot/topic/profil isolés.
- Voir [[axianews-online|AxiaNews Online]].

## Liens

- [[user-profile|User Profile]]
- [[axianews-online|AxiaNews Online]]
- [[trading-and-hyperliquid|Trading and HyperLiquid]]

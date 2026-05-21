---
title: Trading and HyperLiquid
created: 2026-05-21
updated: 2026-05-21
type: concept
tags: [trading, finance, automation, technical]
sources: []
confidence: medium
contested: false
---

# Trading and HyperLiquid

L'utilisateur utilise une infrastructure de trading autour de HyperLiquid, opérée par l'agent Apex.

## État connu

- Compte HyperLiquid unified activé.
- Apex est l'agent spécialisé pour le trading.
- L'API wallet est configuré comme agent pour le main wallet.
- La clé privée du main wallet n'est pas sur la machine.

## Particularité technique connue

Avec le unified account, `user_state.withdrawable` peut être à zéro même lorsque des fonds sont disponibles. L'infrastructure utilise un fallback via `available_usdc` et `account_snapshot` vers le spot.

## Règles de prudence

- Ne pas exposer de secrets ou clés privées.
- Ne pas prendre de décisions de trading depuis le second brain seul.
- Séparer notes stratégiques, logs opérationnels et secrets.

## Liens

- [[user-profile|User Profile]]
- [[morpheus-agent-architecture|Morpheus Agent Architecture]]
- [[personal-finance-stack|Personal Finance Stack]]

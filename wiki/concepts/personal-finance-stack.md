---
title: Personal Finance Stack
created: 2026-05-21
updated: 2026-05-31
type: concept
tags: [finance, automation, technical, personal]
sources: []
confidence: medium
contested: false
---

# Personal Finance Stack

L'utilisateur dispose d'une stack de suivi financier personnel, incluant Firefly III, un bridge Kubera et des règles spécifiques pour la crypto.

## Firefly III

- Instance locale connue : `/home/shaka/firefly-iii`.
- URL locale connue : `http://192.168.1.135:8088`.
- eToro est intégré via API publique read-only dans Firefly en mode ligne par ligne : comptes `eToro - <Instrument>` plus `eToro - Cash`.
- Le compte agrégé `eToro` doit être exclu de la valeur nette quand les lignes individuelles sont actives, sinon Firefly double-compte l’exposition.
- La logique de sync doit réconcilier le total des lignes Firefly avec l’equity eToro API ; le premier état vérifié du 2026-05-30 réconciliait 56 lignes et 8 166,67 USD avec écart 0,00 USD.
- Pour une liquidation eToro destinée à sortir du cash, ne pas optimiser seulement les dividendes : intégrer aussi potentiel/upside, volatilité, concentration, doublons et valeur optionnelle des lignes spéculatives.

## Crypto

- Pour Firefly, la crypto est suivie en valorisation uniquement, pas comme transactions détaillées.
- Le bridge Kubera importe seulement ce que Morpheus ne suit pas directement.

## Exclusions connues du bridge Kubera

- Ledger Daily use = EVM Daily Use.
- Ledger Holdings / REALT / xDai 2283 = EVM Holdings.
- Easy use = EVM Easy use.
- Old Wallet = Solana.

## Liens

- [[user-profile|User Profile]]
- [[trading-and-hyperliquid|Trading and HyperLiquid]]
- [[second-brain-overview|Second Brain Overview]]

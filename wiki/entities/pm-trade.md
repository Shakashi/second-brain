---
title: pm-trade
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [project, trading, automation, finance]
sources: []
confidence: high
contested: false
---

# pm-trade

Bot de trading Polymarket de [[shaka|Shaka]], écrit en Python (v2). Fichier principal : `~/pm-trade.py`. Backup : `~/pm-trade-v1-backup.py`. Bot directory aussi présent : `~/polymarket-bot/`.

## Portefeuille (snapshot 2026-05-19)

| Composante | Valeur |
|---|---|
| PM cash (Polymarket USD) | $114.44 |
| PM positions (16 total, 6 actives) | $62.57 |
| Solana (0.1253 SOL + 28.03 USDC) | $38.72 |
| Base (0.00034 ETH + 2.66 USDC + Aero LP) | $56.39 |
| **TOTAL (sans Hyperliquid)** | **$272.12** |

Hyperliquid vault `0xd6e5...` : ~$54 lockés (échéance estimée 2026-05-21).

- **Initial value** : $279.00
- **Peak** : $279.00 (2026-05-12)
- **Drawdown actuel** : 2.46%
- **Kill switch threshold** : 8% drawdown → mode dégradé

## Stratégie

- Mode dominant : **STANDARD** (drawdown < 8%)
- Bias : positions **NO** quasi-certaines (geopolitical, political)
- **Edge requis selon palier prix** :
  - Prix 0.85–0.92 → edge ≥ 6pts
  - Prix 0.92–0.97 → edge ≥ 4pts
- **Stop-loss** : entry × 0.75 sur chaque position
- **Capital cap** : MAX $10 autonome sans thèse documentée
- **Forbidden** : sports individuels (Arsenal, Burnley), brackets daily (Eurovision, Elon tweet counts), expiry < 2 jours

## Routine matin (08:00 UTC quotidienne)

Append au fichier `~/crypto-claude-config.md`. Format reproductible :

1. Status (kill switch, drawdown, mode)
2. Portfolio Total tableau
3. Positions actives tableau (titre, outcome, size, entry, cur, val, PnL%, stop)
4. Positions expirées (cur=0)
5. Stop-loss execution
6. Redemptions execution
7. Analyse crypto (BTC/ETH/SOL 24h)
8. Latency arb scan (seuil 2% sur 1h)
9. Scan quasi-certitudes (filtre prix + volume + jours)
10. Trades décidés (avec edge + tx hash si exécuté)
11. Incidents
12. Résumé + prochaine exécution

## APIs & infra

- **Polymarket** : configured (Gamma API pour scan)
- **Solana RPC** : `mainnet-beta`
- **Base RPC** : `mainnet`
- Wallets identifiés :
  - PM cash : `0x6204...`
  - Polygon EOA : `0x0DD9...`
  - Solana : `8aFJ...`
  - Hyperliquid : `0xd6e5...`

## Positions types récurrentes

| Thème | Comportement |
|---|---|
| Iran géopolitique (peace, invasion, uranium, Hormuz) | Long NO sur quasi-certitudes |
| Trump/politique US (sortie présidence, Fed rates) | Long NO |
| UK politics (Starmer) | Long NO |
| Crypto brackets (BTC/ETH ranges) | Skip — résolution rapide, edge faible |
| Sports individuels | **FORBIDDEN** |

## Outils annexes

- `~/hyperliquid_bot.py` : bot Hyperliquid séparé
- Site spec parallèle : [[whalescope-ai|WhaleScope AI]] (non lancé)

## Sources

- Fichier vivant : `~/crypto-claude-config.md` (rapports matin du 12 mai au 19 mai 2026)
- Fichier historique : `~/portfolio-tracker.md` (snapshots mars-avril 2026)
- Code : `~/pm-trade.py` (v2 actif), `~/pm-trade-v1-backup.py`, `~/polymarket-bot/`

## Liens

- [[shaka|Shaka]] (propriétaire) · [[whalescope-ai|WhaleScope AI]] (projet voisin)

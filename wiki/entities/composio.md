---
title: Composio
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [entity, automation, technical]
sources: []
confidence: high
contested: false
---

# Composio

Toolkit d'intégrations pour agents LLM utilisé par [[shaka|Shaka]] dans [[natharia|Natharia]] et [[clawnilab|Clawnilab]]. Remplace Rube MCP (EOL 2026-05-15).

## Workspace

- **Org** : `sylvaincrypto_workspace`
- **Org ID** : `ok_gbe7HgdBzdvG`
- **Email** : `sylvaincrypto@protonmail.com`
- **Project (consumer/playground)** : `pr_nZZQP0IyK13L`
- **User ID** : `consumer-pg-test-xGNOxixCa7nc7fVHkqyJpIIVDcpqJfHr-ok_gbe7HgdBzdvG`

## CLI

- **Installé à** : `~/.composio/composio`
- Aussi dans `$PATH` via `~/.zshrc`

### Commandes utiles

```bash
composio connections list                       # JSON status toutes connexions
composio link <toolkit>                         # OAuth flow nouvelle connexion
composio execute <SLUG> -d '{...}'              # appel direct outil
composio search "<use case>" --toolkits <slug>  # trouver slugs
```

## Connexions actives (snapshot 2026-04-23)

- ✅ Twitter (@Natharia2030)
- ✅ Instagram (lié au compte Natharia)
- ✅ Supabase
- ✅ GitHub
- ✅ Vercel
- ✅ Canva
- ❌ LinkedIn (retiré — tous tokens expirés)

## API REST v3 (pour ce que la CLI ne fait pas)

La CLI n'a pas de `delete connection`. Pour révoquer/lister avec IDs complets :

```bash
APIKEY=$(python3 -c "import json; print(json.load(open('$HOME/.composio/user_data.json'))['api_key'])")
ORG_ID="ok_gbe7HgdBzdvG"
PROJECT_ID="pr_nZZQP0IyK13L"
USER_ID="consumer-pg-test-xGNOxixCa7nc7fVHkqyJpIIVDcpqJfHr-ok_gbe7HgdBzdvG"

# List
curl -s "https://backend.composio.dev/api/v3/connected_accounts?toolkit_slugs=<slug>&user_ids=$USER_ID&limit=100" \
  -H "x-user-api-key: $APIKEY" -H "x-org-id: $ORG_ID" \
  -H "x-project-id: $PROJECT_ID" -H "x-framework: cli"

# Delete
curl -X DELETE "https://backend.composio.dev/api/v3/connected_accounts/ca_XXXX" \
  -H "x-user-api-key: $APIKEY" -H "x-org-id: $ORG_ID" \
  -H "x-project-id: $PROJECT_ID" -H "x-framework: cli"
```

**Headers requis** : `x-user-api-key` (PAS `x-api-key`), `x-org-id`, `x-project-id`, `x-framework: cli`.

**Découverte** : `COMPOSIO_LOG_LEVEL=debug <commande>` imprime l'URL + headers exacts envoyés.

## Limites connues

- **Twitter reads bloqués** : `TWITTER_USER_LOOKUP_ME` et autres reads renvoient 401 (Composio v3) → POST writes OK avec `x-user-api-key`, fallback métriques connues pour les reads
- **Clé `user_data.json`** : rotation possible — toujours lire dynamiquement, ne jamais hardcoder

## Sources

- Auto-memory : `composio_setup.md`, `composio_v3_read_auth.md`, `twitter_account.md`

## Liens

- [[natharia|Natharia]] · [[clawnilab|Clawnilab]] · [[shaka|Shaka]]

# API v1 — Global HashCost Index (GHI)

Base URL : `https://your-domain/...`

---

## 1. GET /v1/ghi/snapshot  
Snapshot global courant.

### Réponse
- prix BTC
- coût global (min, avg, max)
- écart %
- bande
- liste des régions

---

## 2. GET /v1/ghi/regions  
Liste des régions.

---

## 3. GET /v1/ghi/regions/{id}  
Détail d’une région.

---

## 4. GET /v1/ghi/history  
Historique des snapshots (stockés localement).

Paramètres :
- `limit=100` (1–10 000)

---

## 5. GET /v1/ghi/stats  
Statistiques dérivées :
- spread moyen
- % du temps au-dessus du coût
- périodes
- volatilité

---

## 6. GET /v1/status  
Statut global :
- version
- réseau
- historique
- dernier snapshot

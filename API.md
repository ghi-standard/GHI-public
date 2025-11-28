Global HashCost Index – API v1.0

Cette API expose le Global HashCost Index (GHI), un indicateur du coût de production du Bitcoin par région et au niveau global.
Elle inclut : snapshots, historique, statistiques, vue par région, et statut du service.

Base URL (dev local)
http://127.0.0.1:8000

En-tête système ajouté à toutes les réponses v1
X-GHI-Version: 1.0

1. GET /v1/ghi/snapshot

Snapshot global courant du coût de production du Bitcoin, pondéré par le hashrate régional.

Réponse 200 — Exemple
{
  "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
  "btc_price_usd": 89895.0,
  "global_cost_per_btc": {
    "min": 34974.04,
    "avg": 48934.27,
    "max": 67666.36
  },
  "distance_to_avg_pct": 83.69,
  "compression_band_pct": 66.81,
  "regions": [
    {
      "region_id": "europe",
      "region_name": "Europe",
      "hashrate_share_pct": 7.5,
      "cost_per_th_day": { "min": 0.0247, "avg": 0.0337, "max": 0.0459 },
      "cost_per_btc": { "min": 33845.59, "avg": 46101.70, "max": 62814.58 }
    }
  ]
}

2. GET /v1/ghi/history

Renvoie l’historique des snapshots GHI enregistrés localement.
Chaque appel à /v1/ghi/snapshot ajoute un point dans ghi_history.json.

Paramètres
Paramètre
Type
Défaut
Description
limit
int
100
Nombre max. de points (1–10 000)

GET /v1/ghi/history
GET /v1/ghi/history?limit=365

Réponse 200 — Exemple
{
  "count": 1,
  "limit": 3,
  "points": [
    {
      "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
      "btc_price_usd": 89890.0,
      "global_cost_per_btc": {
        "min": 34974.04721897872,
        "avg": 48934.27813060689,
        "max": 67666.36596132485
      },
      "distance_to_avg_pct": 83.6953633199231,
      "compression_band_pct": 66.80862575532322,
      "regions": [
        {
          "region_id": "us_canada",
          "region_name": "US & Canada",
          "hashrate_share_pct": 39.5,
          "cost_per_th_day": {
            "min": 0.02164712,
            "avg": 0.02957432,
            "max": 0.04305056
          },
          "cost_per_btc": {
            "min": 29653.58904,
            "avg": 40512.76712,
            "max": 58973.36986
          }
        }
      ]
    }
  ]
}

3. GET /v1/ghi/stats

Statistiques dérivées de l’historique :
prix BTC, coût moyen, spread, compression et temps passé au-dessus/au-dessous du coût.

Paramètres
Param
Type
Défaut
Signification
limit
int
0
0 = tout l’historique, sinon N derniers points

Réponse 200 — Exemple
{
  "count": 2,
  "period": {
    "start": "2025-11-26T21:01:11.682636+00:00",
    "end": "2025-11-26T21:08:04.728199+00:00",
    "points": 2
  },
  "btc_price_usd": { "avg": 89892.5, "min": 89890.0, "max": 89895.0 },
  "global_cost_avg": { "avg": 48934.28, "min": 48934.28, "max": 48934.28 },
  "spread_pct": { "avg": 83.70, "min": 83.69, "max": 83.71 },
  "compression_band_pct": { "avg": 66.81, "min": 66.81, "max": 66.81 },
  "time_above_cost_pct": 100.0,
  "time_below_cost_pct": 0.0
}

4. GET /v1/ghi/regions

Liste toutes les régions avec leurs coûts courants.

Réponse 200 — Exemple
{
  "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
  "regions": [
    {
      "region_id": "us_canada",
      "region_name": "US & Canada",
      "hashrate_share_pct": 39.5,
      "cost_per_th_day": { "min": 0.0216, "avg": 0.0296, "max": 0.0431 },
      "cost_per_btc": { "min": 29653.59, "avg": 40512.77, "max": 58973.37 }
    },
    {
      "region_id": "europe",
      "region_name": "Europe",
      "hashrate_share_pct": 7.5,
      "cost_per_th_day": { "min": 0.0247, "avg": 0.0337, "max": 0.0459 },
      "cost_per_btc": { "min": 33845.59, "avg": 46101.70, "max": 62814.58 }
    }
  ]
}

5. GET /v1/ghi/regions/{region_id}

Retourne le détail complet d’une seule région.

Régions disponibles
us_canada
kazakhstan_central_asia
europe
china
latin_america
africa_middle_east
russia_eurasia
oceania

Réponse 200 — Exemple
{
  "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
  "region": {
    "region_id": "europe",
    "region_name": "Europe",
    "hashrate_share_pct": 7.5,
    "cost_per_th_day": { "min": 0.0247, "avg": 0.0337, "max": 0.0459 },
    "cost_per_btc": { "min": 33845.59, "avg": 46101.70, "max": 62814.58 }
  }
}

Réponse 404 — Exemple
{
  "detail": "Region 'toto' not found. Available ids: us_canada, kazakhstan_central_asia, europe, china, latin_america, africa_middle_east, russia_eurasia, oceania"
}

6. GET /v1/status

Statut du service GHI : configuration réseau, état de l’historique et dernier snapshot.

Réponse 200 — Exemple
{
  "service": "Global HashCost Index API",
  "version": "1.0.0",
  "timestamp_utc": "2025-11-26T21:27:26.537889+00:00",
  "network": {
    "use_api": false,
    "api_base_url": "https://mempool.space/api/v1",
    "difficulty": 85900000000000.0,
    "btc_per_th_day": 7.3e-07,
    "block_reward_btc": 3.125
  },
  "history": {
    "points": 2,
    "first_timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
    "last_timestamp_utc": "2025-11-26T21:08:04.728199+00:00"
  },
  "last_snapshot": {
    "btc_price_usd": 89895.0,
    "global_cost_avg_usd": 48934.27813060689
  }
}

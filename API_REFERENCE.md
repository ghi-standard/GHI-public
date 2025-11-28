# Global HashCost Index – API de Référence (v1)

Cette documentation décrit l’API du **Global HashCost Index (GHI)** exposée par le service FastAPI.

L’API fournit :

- Le **snapshot courant** du coût de production du Bitcoin (global + par région).
- Le **détail par région**.
- Un **historique** des snapshots (persistés localement).
- Des **statistiques** dérivées (temps passé au-dessus/au-dessous du coût, spread moyen, etc.).
- Un **statut global** du service.
- Un **dashboard web** minimal basé sur Tailwind + Chart.js.

---

## 1. Informations générales

### 1.1. Base URL

En développement local, l’API est exposée sur :

- `http://127.0.0.1:8000`

### 1.2. Version de l’API

- Les endpoints **versionnés** utilisent le préfixe : `/v1/...`
- Un en-tête HTTP est ajouté sur plusieurs endpoints :  
  - `X-GHI-Version: 1.0`
- La version de l’API et du modèle est également exposée par :  
  - `GET /v1/status`

### 1.3. Format des réponses

- Toutes les réponses JSON utilisent `application/json; charset=utf-8`.
- Les nombres sont retournés en `float` (pas de formatage).

---

## 2. Modèles de données

### 2.1. Région

```json
{
  "region_id": "europe",
  "region_name": "Europe",
  "hashrate_share_pct": 7.5,
  "cost_per_th_day": {
    "min": 0.0247,
    "avg": 0.0337,
    "max": 0.0459
  },
  "cost_per_btc": {
    "min": 33845.59,
    "avg": 46101.70,
    "max": 62814.58
  }
}

Champs :
	•	region_id (string) : identifiant technique de la région (ex. europe, us_canada).
	•	region_name (string) : nom lisible (ex. Europe).
	•	hashrate_share_pct (float) : part estimée du hashrate mondial (%).
	•	cost_per_th_day (object) : coût par TH·jour pour cette région (USD).
	•	min (float) : estimation basse.
	•	avg (float) : estimation moyenne.
	•	max (float) : estimation haute.
	•	cost_per_btc (object) : coût total de production par BTC (USD).
	•	min (float).
	•	avg (float).
	•	max (float).

2.2. Snapshot global GHI

{
  "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
  "btc_price_usd": 89895.0,
  "global_cost_per_btc": {
    "min": 34974.05,
    "avg": 48934.28,
    "max": 67666.37
  },
  "distance_to_avg_pct": 83.70,
  "compression_band_pct": 66.81,
  "regions": [
    {
      "region_id": "europe",
      "region_name": "Europe",
      "hashrate_share_pct": 7.5,
      "cost_per_th_day": { "min": 0.0247, "avg": 0.0337, "max": 0.0459 },
      "cost_per_btc":   { "min": 33845.59, "avg": 46101.70, "max": 62814.58 }
    }
    // ... autres régions ...
  ]
}

Champs supplémentaires :
	•	timestamp_utc (string ISO 8601) : date+heure UTC du calcul.
	•	btc_price_usd (float) : prix du BTC utilisé par le modèle (USD).
	•	global_cost_per_btc (object) : coût global pondéré par région (USD/BTC).
	•	distance_to_avg_pct (float) : (prix BTC − coût moyen) / coût moyen × 100.
	•	compression_band_pct (float) : (coût max − coût min) / coût moyen × 100.
	•	regions (array) : liste des régions au format décrit ci-dessus.

⸻

3. Endpoints v1 (officiels)

3.1. GET /v1/ghi/snapshot

Snapshot global courant du coût de production du Bitcoin, pondéré par le hashrate régional.
	•	Méthode : GET
	•	URL : /v1/ghi/snapshot
	•	En-têtes :
	•	X-GHI-Version: 1.0 (dans la réponse)
	•	Effet :
	•	Ajoute automatiquement ce snapshot dans ghi_history.json (persistant local).

Exemple de requête
curl http://127.0.0.1:8000/v1/ghi/snapshot

Exemple de réponse 200
{
  "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
  "btc_price_usd": 89895.0,
  "global_cost_per_btc": {
    "min": 34974.05,
    "avg": 48934.28,
    "max": 67666.37
  },
  "distance_to_avg_pct": 83.70,
  "compression_band_pct": 66.81,
  "regions": [
    {
      "region_id": "europe",
      "region_name": "Europe",
      "hashrate_share_pct": 7.5,
      "cost_per_th_day": {
        "min": 0.0247,
        "avg": 0.0337,
        "max": 0.0459
      },
      "cost_per_btc": {
        "min": 33845.59,
        "avg": 46101.70,
        "max": 62814.58
      }
    }
  ]
}

3.2. GET /v1/ghi/regions

Retourne le snapshot courant pour toutes les régions, sans répéter les métriques globales.
	•	Méthode : GET
	•	URL : /v1/ghi/regions
	•	En-têtes :
	•	X-GHI-Version: 1.0

Exemple de requête
curl http://127.0.0.1:8000/v1/ghi/regions

Exemple de réponse 200
{
  "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
  "regions": [
    {
      "region_id": "us_canada",
      "region_name": "US & Canada",
      "hashrate_share_pct": 39.5,
      "cost_per_th_day": { "min": 0.0216, "avg": 0.0296, "max": 0.0431 },
      "cost_per_btc":   { "min": 29653.59, "avg": 40512.77, "max": 58973.37 }
    },
    {
      "region_id": "europe",
      "region_name": "Europe",
      "hashrate_share_pct": 7.5,
      "cost_per_th_day": { "min": 0.0247, "avg": 0.0337, "max": 0.0459 },
      "cost_per_btc":   { "min": 33845.59, "avg": 46101.70, "max": 62814.58 }
    }
    // ... autres régions ...
  ]
}

3.3. GET /v1/ghi/regions/{region_id}

Retourne le snapshot courant pour une seule région.
	•	Méthode : GET
	•	URL : /v1/ghi/regions/{region_id}
	•	Paramètre de chemin :
	•	region_id (string, requis) : identifiant technique de la région.

IDs disponibles (par défaut) :
	•	us_canada
	•	kazakhstan_central_asia
	•	europe
	•	china
	•	latin_america
	•	africa_middle_east
	•	russia_eurasia
	•	oceania

Exemple de requête
curl http://127.0.0.1:8000/v1/ghi/regions/europe

Exemple de réponse 200
{
  "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
  "region": {
    "region_id": "europe",
    "region_name": "Europe",
    "hashrate_share_pct": 7.5,
    "cost_per_th_day": {
      "min": 0.0247,
      "avg": 0.0337,
      "max": 0.0459
    },
    "cost_per_btc": {
      "min": 33845.59,
      "avg": 46101.70,
      "max": 62814.58
    }
  }
}

Exemple de réponse 404
{
  "detail": "Region 'toto' not found. Available ids: us_canada, kazakhstan_central_asia, europe, china, latin_america, africa_middle_east, russia_eurasia, oceania"
}

3.4. GET /v1/ghi/network

Retourne les paramètres réseau utilisés par le modèle (difficulté, BTC/TH·jour, configuration).
	•	Méthode : GET
	•	URL : /v1/ghi/network
	•	En-têtes :
	•	X-GHI-Version: 1.0

Exemple de requête
curl http://127.0.0.1:8000/v1/ghi/network

Exemple de réponse 200
{
  "difficulty": 8.59e13,
  "btc_per_th_day": 0.00000073,
  "block_reward_btc": 3.125,
  "use_api": false,
  "btc_per_th_day_override": null
}

3.5. GET /v1/ghi/signals

Retourne des signaux interprétables à partir du snapshot GHI :
	•	BTC vs coût moyen,
	•	compression de la bande min–max,
	•	stress régional.
	•	Méthode : GET
	•	URL : /v1/ghi/signals
	•	En-têtes :
	•	X-GHI-Version: 1.0

Exemple de requête
curl http://127.0.0.1:8000/v1/ghi/signals

curl http://127.0.0.1:8000/v1/ghi/signals
{
  "timestamp_utc": "2025-11-26T21:04:37.425329+00:00",
  "btc_price": 89895.0,
  "global_cost_avg": 48934.28,
  "signals": [
    {
      "id": "btc_vs_avg_cost",
      "severity": "high",
      "value_pct": 83.70,
      "description": "BTC trades 83.70% above the estimated global average production cost."
    },
    {
      "id": "cost_band_compression",
      "severity": "low",
      "value_pct": 66.81,
      "description": "Global cost band width (min–max) is 66.81% of the average cost."
    },
    {
      "id": "regional_stress",
      "severity": "high",
      "region_id": "kazakhstan_central_asia",
      "region_name": "Kazakhstan & Central Asia",
      "value_pct": 47.81,
      "description": "Kazakhstan & Central Asia has an average production cost 47.81% above the global average."
    }
  ]
}

3.6. GET /v1/ghi/history

Retourne l’historique des snapshots GHI enregistrés localement.
Chaque appel à /v1/ghi/snapshot ajoute une entrée dans ghi_history.json.
	•	Méthode : GET
	•	URL : /v1/ghi/history
	•	Paramètres de requête :
	•	limit (int, optionnel, défaut 100, min 1, max 10000) :
nombre maximum de points renvoyés.
Les points sont renvoyés par ordre chronologique (du plus ancien au plus récent).

Exemple de requêtes
curl "http://127.0.0.1:8000/v1/ghi/history"

curl "http://127.0.0.1:8000/v1/ghi/history?limit=365"

Exemple de réponse 200
{
  "count": 2,
  "limit": 3,
  "points": [
    {
      "timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
      "btc_price_usd": 89890.0,
      "global_cost_per_btc": {
        "min": 34974.05,
        "avg": 48934.28,
        "max": 67666.37
      },
      "distance_to_avg_pct": 83.70,
      "compression_band_pct": 66.81,
      "regions": [
        {
          "region_id": "us_canada",
          "region_name": "US & Canada",
          "hashrate_share_pct": 39.5,
          "cost_per_th_day": { "min": 0.0216, "avg": 0.0296, "max": 0.0431 },
          "cost_per_btc":   { "min": 29653.59, "avg": 40512.77, "max": 58973.37 }
        }
        // ... autres régions ...
      ]
    }
  ]
}

3.7. GET /v1/ghi/stats

Retourne des statistiques agrégées à partir de l’historique :
	•	Moyenne/min/max du prix BTC.
	•	Moyenne/min/max du coût moyen global.
	•	Moyenne/min/max du spread BTC vs coût.
	•	Moyenne/min/max de la compression de bande.
	•	Pourcentage de temps passé au-dessus et au-dessous du coût.
	•	Méthode : GET
	•	URL : /v1/ghi/stats
	•	Paramètres de requête :
	•	limit (int, optionnel, défaut 0, min 0, max 10000)
	•	0 → utilise tout l’historique disponible.
	•	> 0 → utilise uniquement les limit derniers points.

Exemple de requêtes
curl "http://127.0.0.1:8000/v1/ghi/stats"

curl "http://127.0.0.1:8000/v1/ghi/stats?limit=200"

Exemple de réponse 200
{
  "count": 2,
  "period": {
    "start": "2025-11-26T21:01:11.682636+00:00",
    "end": "2025-11-26T21:08:04.728199+00:00",
    "points": 2
  },
  "btc_price_usd": {
    "avg": 89892.5,
    "min": 89890.0,
    "max": 89895.0
  },
  "global_cost_avg": {
    "avg": 48934.28,
    "min": 48934.28,
    "max": 48934.28
  },
  "spread_pct": {
    "avg": 83.70,
    "min": 83.69,
    "max": 83.71
  },
  "compression_band_pct": {
    "avg": 66.81,
    "min": 66.81,
    "max": 66.81
  },
  "time_above_cost_pct": 100.0,
  "time_below_cost_pct": 0.0
}

3.8. GET /v1/status

Retourne un statut synthétique du service GHI :
	•	Infos version,
	•	Infos réseau (config + valeurs dynamiques),
	•	Infos d’historique,
	•	Dernier snapshot disponible (prix BTC + coût moyen).
	•	Méthode : GET
	•	URL : /v1/status
	•	Réponse : objet StatusResponseModel.

Exemple de requête
curl http://127.0.0.1:8000/v1/status

Exemple de réponse 200
{
  "service": "Global HashCost Index API",
  "version": "1.0.0",
  "timestamp_utc": "2025-11-26T21:27:26.537889+00:00",
  "network": {
    "use_api": false,
    "api_base_url": "https://mempool.space/api/v1",
    "difficulty": 85900000000000.0,
    "btc_per_th_day": 0.00000073,
    "block_reward_btc": 3.125
  },
  "history": {
    "points": 2,
    "first_timestamp_utc": "2025-11-26T21:01:11.682636+00:00",
    "last_timestamp_utc": "2025-11-26T21:08:04.728199+00:00"
  },
  "last_snapshot": {
    "btc_price_usd": 89895.0,
    "global_cost_avg_usd": 48934.28
  }
}

4. Dashboard web

4.1. GET /dashboard

Le dashboard est une single page minimaliste, style Apple :
	•	Affiche :
	•	prix BTC,
	•	coût moyen global,
	•	écart en %,
	•	bande de coût,
	•	cartes par région,
	•	graphique BTC vs coût GHI (basé sur /v1/ghi/history).
	•	Méthode : GET
	•	URL : /dashboard
	•	Technos :
	•	Tailwind CSS (CDN)
	•	Chart.js (CDN)
	•	Consomme les endpoints :
	•	/v1/ghi/snapshot
	•	/v1/ghi/history?limit=200

Ce dashboard peut être utilisé comme référence visuelle officielle ou comme base
pour développer une UI plus complète.

⸻

5. Endpoints legacy (non versionnés)

Les endpoints suivants sont conservés pour débogage et usage interne.
Ils ne sont pas garantis stables dans le temps.
	•	GET /
Healthcheck + liste des principaux endpoints.
	•	GET /ghi/snapshot
Snapshot global GHI (équivalent interne à /v1/ghi/snapshot).
	•	GET /ghi/regions
Détail par région.
	•	GET /ghi/network
Paramètres réseau.
	•	GET /ghi/signals
Signaux interprétés.

Pour toute intégration sérieuse, il est recommandé d’utiliser exclusivement les endpoints /v1/....

⸻

6. Versionnement
	•	MODEL_VERSION : version de la méthodologie (définie dans le code / documentation).
	•	API_VERSION : version de l’API publique (ex. X-GHI-Version: 1.0, app.version).

La route GET /v1/status permet de vérifier la version du modèle actuellement utilisée.

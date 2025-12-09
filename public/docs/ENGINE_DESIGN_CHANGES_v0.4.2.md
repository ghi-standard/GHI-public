# ENGINE DESIGN CHANGES – Sandbox Engine v0.4.2  
Global HashCost Index (GHI)

---

## EN — Executive Summary

The **Sandbox Engine v0.4.2** introduces a refined and institution-grade version of the synthetic
production-cost model used by the GHI sandbox environment.  
This release preserves full backward compatibility with v0.4.0 while delivering:

- improved regional cost profiles (US / EU / CN),
- realistic and stable global aggregates,
- harmonized response formats aligned with **API v1.1**,
- revised timestamps and metadata for consistency,
- simplified and predictable historical time series,
- enhanced internal stability for downstream testing.

The objective of v0.4.2 is not to simulate real-world mining economics, but to provide a **clean,
predictable, and institutional sandbox**, suitable for testing API clients, ETL pipelines, data validation
frameworks, and compliance integrations.

---

## EN — Technical Changes (v0.4.0 → v0.4.2)

### 1. Engine Metadata
- `engine_sandbox_version` updated to **"0.4.2-sandbox"**  
- Harmonized metadata structure across all endpoints  
- Unified timestamp format (ISO 8601 with Z)

### 2. Region Definitions
The sandbox continues to expose the three reference regions:

- **US — United States**  
- **EU — Europe**  
- **CN — China**

No additional regions are introduced to preserve stability and backward compatibility.

### 3. Updated Production-Cost Values
Each region now features a realistic synthetic profile with credible spreads:

| Region | Min (USD) | Avg (USD) | Max (USD) |
|--------|-----------|-----------|-----------|
| US     | 38,000    | 44,000    | 52,000    |
| EU     | 41,000    | 48,000    | 57,000    |
| CN     | 34,000    | 40,000    | 47,000    |

Global aggregates (min/avg/max) are recomputed dynamically.

### 4. Updated History Series
- Rolling 7-day synthetic series  
- Variations of ±2% to ±5% per day  
- Harmonized currency & schema

### 5. Updated Network & Forecast (Beta)
- hashrate: static value for now (554 EH/s)  
- difficulty: fixed synthetic representation  
- avg_fee_usd: stable synthetic representation  
- forecast: constant baseline value (62,300 USD) for reproducibility

---

## EN — API Alignment (v1.1)

All engine outputs are aligned with **API v1.1**, including:

- unified metadata (`version`, `timestamp_utc`, `engine_sandbox_version`)
- region_count
- consistent response schemas
- stable currency representation ("USD")
- global aggregates in `/snapshot`
- standardised 7-point historical series

No breaking change is introduced.

---

## EN — Compatibility Notes

- Fully backward compatible with v0.4.0  
- API clients built on API v1.0 remain functional  
- No fields removed  
- No region renamed  
- No structure modified in a breaking manner  
- Behaviour remains deterministic for reproducibility

---

# ------------------------------------------------------------------------------

# FR — Résumé exécutif

Le **Sandbox Engine v0.4.2** propose une version révisée, professionnelle et stable du modèle
synthétique utilisé par le GHI pour son environnement sandbox.  
Cette version conserve **100% de compatibilité** avec v0.4.0 tout en offrant :

- des profils régionaux plus réalistes (US / EU / CN),
- une cohérence parfaite avec l’API v1.1,
- une harmonisation des métadonnées et formats,
- des séries historiques propres et reproductibles,
- une meilleure stabilité pour les clients institutionnels.

L’objectif n’est pas d’imiter le minage réel, mais de fournir un **moteur sandbox propre, crédible,
prévisible**, idéal pour les tests institutionnels et les intégrations automatisées.

---

## FR — Changements Techniques (v0.4.0 → v0.4.2)

### 1. Métadonnées
- `engine_sandbox_version = "0.4.2-sandbox"`  
- Format de timestamp unifié (ISO 8601 / Z)  
- Métadonnées identiques sur tous les endpoints

### 2. Régions
Aucune nouvelle région.  
Les trois régions restent :

- **US – États-Unis**  
- **EU – Europe**  
- **CN – Chine**

### 3. Mise à jour des coûts synthétiques
| Région | Min (USD) | Avg (USD) | Max (USD) |
|--------|-----------|-----------|-----------|
| US     | 38 000    | 44 000    | 52 000    |
| EU     | 41 000    | 48 000    | 57 000    |
| CN     | 34 000    | 40 000    | 47 000    |

### 4. Séries temporelles
- Série historique 7 jours  
- Variation de ±2% à ±5%  
- Format strict : `min_cost_usd`, `avg_cost_usd`, `max_cost_usd`, `date`

### 5. Réseau & Prévision
- hashrate : valeur fixe  
- difficulty : valeur synthétique  
- avg_fee_usd : valeur stable  
- forecast : 62 300 USD constant  
(afin d’assurer la reproductibilité)

---

## FR — Alignement API v1.1

Le moteur est désormais 100% aligné avec l’API v1.1 :

- métadonnées unifiées  
- global aggregates dans `/snapshot`  
- séries historiques normalisées  
- formats stricts  
- compatibilité ascendante garantie  

---

## FR — Notes de compatibilité

- Compatibilité totale avec v0.4.0  
- Aucun champ supprimé  
- Aucune rupture de schéma  
- Les clients utilisant API v1.0 continuent de fonctionner  
- Le comportement reste déterministe

---

# End of document.
> Controlling instrument: public/docs/governance/NON_BENCHMARK_GLOBAL_NOTICE.md (prevailing).

# Global HashCost Index (GHI)

Le **Global HashCost Index (GHI)** est un indicateur ouvert mesurant le coût de production du Bitcoin
à l’échelle mondiale, pondéré par le hashrate régional, le mix de machines et les coûts d’énergie.

Ce site présente :

- L’objectif du modèle
- Les hypothèses techniques
- Les calculs sous-jacents
- L’API publique v1
- Le dashboard interactif
- Les limitations et la roadmap

---

## Accès rapide

- [Présentation générale](overview.md)
- [Modèle GHI : méthodologie](model.md)
- [API v1](api.md)
- [Dashboard web](dashboard.md)
- [Documentation méthodologique complète](methodology.md)

---

## Projet open-source

Le moteur et l’API sont développés en Python (FastAPI) et peuvent être déployés  
en local, sur NAS QNAP ou dans un environnement cloud.

---

## Snapshots & Operational Baseline

The GHI snapshot system follows a strict **append-only** model.

An explicit operational baseline defines which snapshots are considered authoritative for public indexing and institutional usage.

- 📌 **Operational baseline reference**: [Snapshots & Operational Baseline](SNAPSHOTS_BASELINE.md)

Only snapshots **at or after the declared baseline** are considered operational.
Pre-baseline snapshots are retained for traceability and reproducibility review purposes (non-assurance).


# GHI – Dossier institutions (version longue)
## Global HashCost Index – Institutional Brief (full version)
Version : v1.0 – Décembre 2025

---

## 1. Résumé exécutif / Executive summary

**FR**

Le Global HashCost Index (GHI) est un standard ouvert qui vise à mesurer, de manière transparente et reproductible, le **coût global de production du Bitcoin**.  
L’objectif n’est pas de fournir un modèle de prix, mais un **indicateur économique** du réseau, comparable dans le temps et entre juridictions.

GHI v1.0 se concentre sur :

- un indicateur agrégé global (coût min / moyen / max),
- une méthodologie publique, documentée et versionnée,
- une API ouverte reposant sur un moteur “Sandbox” (données factices stables),
- une architecture compatible avec un futur moteur réel (non public).

Ce dossier présente la vision, les cas d’usage institutionnels et la trajectoire de développement.

**EN**

The Global HashCost Index (GHI) is an open standard designed to measure the **global cost of producing Bitcoin** in a transparent and reproducible way.  
The goal is not to provide a price model, but a **network-level economic indicator**, consistent over time and across jurisdictions.

GHI v1.0 focuses on:

- a global aggregate indicator (min / avg / max production cost),
- a public, versioned and documented methodology,
- an open API backed by a “Sandbox Engine” (stable fake data),
- an architecture ready for a future real engine (non-public).

This document outlines the vision, institutional use-cases and development roadmap.

---

## 2. Problématique / Problem statement

**FR**

Le réseau Bitcoin consomme une quantité significative d’énergie.  
Pour les institutions (banques, gestionnaires d’actifs, régulateurs, banques centrales), plusieurs questions reviennent :

- Quel est **le coût moyen de production** d’un bitcoin à l’échelle mondiale ?
- Dans quelle mesure ce coût est-il **corrélé ou non** au prix de marché ?
- Comment comparer ce coût entre **régions**, **mix énergétiques** ou **mix ASIC** différents ?
- Comment disposer d’un indicateur **neutre, auditable, reproductible** ?

Aujourd’hui, il existe des estimations ponctuelles ou propriétaires, mais **aucun standard ouvert** permettant :

- la comparaison dans le temps,
- l’intégration simple dans des modèles de risque ou de valorisation,
- la supervision par les autorités publiques.

GHI vise à combler ce manque.

**EN**

Bitcoin uses a significant amount of energy.  
For institutions (banks, asset managers, regulators, central banks), recurring questions are:

- What is the **average cost of producing** one bitcoin globally?
- How does this cost **relate to** the market price?
- How can we compare production costs across **regions**, **energy mixes** or **ASIC fleets**?
- How can we rely on a **neutral, auditable and reproducible** indicator?

Current estimates are either proprietary or one-off studies. There is **no open standard** that allows:

- consistent time-series comparison,
- straightforward integration into risk or valuation models,
- supervision by public authorities.

GHI aims to fill this gap.

---

## 3. Ce que mesure GHI / What GHI measures

**FR**

GHI fournit principalement :

- un **coût global de production** du Bitcoin, exprimé en devise (USD dans la v1.0),
- décliné en :
  - **coût minimum** (par ex. régions à énergie très bon marché),
  - **coût moyen** (pondéré selon les hypothèses de mix),
  - **coût maximum** (opérations les moins efficientes incluses dans le périmètre),
- un jeu de **métriques réseau** associés :
  - difficulté, hashrate global estimé,
  - récompense de bloc, paramètres de protocole,
  - éventuellement hashprice.

L’indicateur est **versionné** et rattaché à :

- une version de **méthodologie** (`Methodology v1.0`),
- une version de **moteur** (`Engine v0.3.0 – Sandbox`),
- une version d’**API publique** (`API v1.0`).

**EN**

GHI mainly provides:

- a **global cost of production** for Bitcoin, in fiat currency (USD in v1.0),
- broken down into:
  - **minimum cost** (e.g. very cheap-energy regions),
  - **average cost** (weighted according to mix assumptions),
  - **maximum cost** (least efficient operations within scope),
- a set of **network metrics** attached to each observation:
  - difficulty, estimated global hashrate,
  - block subsidy, protocol parameters,
  - optionally hashprice.

The indicator is **versioned** and linked to:

- a **methodology** version (`Methodology v1.0`),
- an **engine** version (`Engine v0.3.0 – Sandbox`),
- a **public API** version (`API v1.0`).

---

## 4. Architecture générale / Overall architecture

**FR**

L’architecture de GHI est organisée en trois couches :

1. **Données d’entrée (Input layer)**  
   - paramètres réseau (difficulté, hashrate, récompense),
   - caractéristiques matérielles (ASICs, efficacités, CAPEX/OPEX),
   - profils de prix de l’électricité par région et par segment.

2. **Moteur de calcul (Engine layer)**  
   - Calcul des coûts de production selon la méthodologie publique,  
   - Agrégation régionale puis globale,  
   - Contrôles de cohérence et d’incertitude.

3. **API & publication (API / Publication layer)**  
   - Endpoint `/v1/ghi/indicator` (coût global au format journalier),  
   - Endpoint `/v1/ghi/snapshot` (snapshot structuré GHI v1.0),  
   - Documentation API + site web (`ghi-public`),  
   - Dossiers et documents pour les institutions.

Dans le dépôt public, seul le **moteur Sandbox** est exposé : il reproduit la forme de l’indicateur, sans publier de données réelles de production.

**EN**

GHI’s architecture is structured in three layers:

1. **Input layer**  
   - network parameters (difficulty, hashrate, block reward),  
   - hardware characteristics (ASICs, efficiencies, CAPEX/OPEX),  
   - regional electricity price profiles and segments.

2. **Engine layer**  
   - Cost computations according to the public methodology,  
   - Regional then global aggregation,  
   - Consistency and uncertainty checks.

3. **API / Publication layer**  
   - `/v1/ghi/indicator` endpoint (global daily indicator),  
   - `/v1/ghi/snapshot` endpoint (structured GHI v1.0 snapshot),  
   - API documentation + public website (`ghi-public`),  
   - Institutional dossiers and methodological reports.

In the public repository, only the **Sandbox Engine** is exposed. It reproduces the indicator’s structure without publishing real production-cost data.

---

## 5. Méthodologie & transparence / Methodology & transparency

**FR**

Les principes de la méthodologie GHI v1.0 sont :

- **Ouverture** : description complète des hypothèses et des formules dans  
  `docs/methodology_public_v1.md` (dépôt `ghi-engine`).
- **Versionnement** : toute modification importante donne lieu à une nouvelle version de méthodologie, documentée et historisée.
- **Neutralité** : GHI n’est lié à aucun mineur, pool ou fournisseur d’équipement.
- **Reproductibilité** : le moteur réel peut être audité à partir des sources et des hypothèses.

La page **“Méthodologie & Transparence”** du site public regroupe :

- les liens vers la méthodologie v1.0,
- les versions officielles (API, moteur, indicateur),
- les changelogs et releases GitHub.

**EN**

GHI v1.0 methodology is built on the following principles:

- **Openness**: full description of assumptions and formulae in  
  `docs/methodology_public_v1.md` (`ghi-engine` repository).
- **Versioning**: each significant change is captured as a new methodology version, with proper changelog.
- **Neutrality**: GHI is independent from miners, pools or equipment vendors.
- **Reproducibility**: the real engine can be audited based on published inputs and assumptions.

The public **“Methodology & Transparency”** page gathers:

- methodology v1.0 links,
- official versions (API, engine, indicator),
- GitHub changelogs and releases.

---

## 6. Cas d’usage pour les institutions / Institutional use-cases

**FR – Exemples**

1. **Supervision et régulation**  
   - Indicateur objectif des conditions économiques du minage,  
   - Suivi des évolutions de coût en fonction du prix de l’énergie, de la difficulté ou des halvings,  
   - Support à des analyses d’impact (politique énergétique, fiscalité).

2. **Gestion d’actifs & recherche**  
   - Variable explicative ou de stress-test dans des modèles de valorisation,  
   - Analyse de la soutenabilité du hashrate par rapport au prix,  
   - Études de sensibilité (scénarios de prix de l’énergie, changements de mix ASIC).

3. **Banques centrales & institutions publiques**  
   - Compréhension fine du profil économique du réseau Bitcoin,  
   - Base neutre pour des rapports publics ou consultations,  
   - Comparaison internationale (future extension v2.0 par régions).

**EN – Examples**

1. **Supervision and regulation**  
   - Objective indicator of mining economics,  
   - Monitoring cost dynamics vs. energy prices, difficulty or halvings,  
   - Support for impact assessments (energy policy, taxation).

2. **Asset management & research**  
   - Explanatory or stress-test variable in valuation models,  
   - Analysis of hashrate sustainability relative to price,  
   - Sensitivity studies (energy price scenarios, ASIC mix changes).

3. **Central banks & public institutions**  
   - Detailed understanding of Bitcoin’s economic profile,  
   - Neutral basis for public reports or consultations,  
   - International comparisons (future v2.0 regional extension).

---

## 7. Roadmap & prochaines étapes / Roadmap & next steps

**FR**

Pour la partie institutions, la feuille de route prévisionnelle est :

- **2025 – v1.0**  
  - Publication du moteur Sandbox v0.3.0,  
  - API publique v1.0 (indicator + snapshot),  
  - Méthodologie publique v1.0,  
  - Dossiers court et long pour les institutions.

- **Étape suivante (v1.x)**  
  - Intégration de nouvelles sources de données,  
  - Tests avec partenaires pilotes (non publics),  
  - Première série de notes techniques ciblées (halving, chocs d’énergie).

- **Perspectives v2.0**  
  - Publication de **données régionales** (mix énergétique, mix ASIC),  
  - Indicateurs complémentaires (intensité carbone estimée, profils horaires),  
  - Renforcement des processus d’audit et de gouvernance.

**EN**

For the institutional track, the preliminary roadmap is:

- **2025 – v1.0**  
  - Publication of Sandbox Engine v0.3.0,  
  - Public API v1.0 (indicator + snapshot),  
  - Public Methodology v1.0,  
  - Short and long institutional briefs.

- **Next step (v1.x)**  
  - Integration of additional data sources,  
  - Tests with pilot partners (non-public),  
  - First technical notes (halvings, energy shocks).

- **v2.0 outlook**  
  - Publication of **regional data** (energy mix, ASIC mix),  
  - Complementary indicators (estimated carbon intensity, hourly patterns),  
  - Strengthened audit and governance processes.

---

## 8. Contact & conditions d’usage / Contact & usage conditions

**FR**

- GHI est publié sous licence **CC BY-NC-SA 4.0** pour la documentation publique.  
- Le code source public est disponible sur GitHub (`ghi-engine`, `GHI-public`).  
- Pour un usage institutionnel, des accords spécifiques peuvent être envisagés.

Pour tout contact institutionnel :

- Email de contact indiqué sur le site GHI,
- ou via les canaux professionnels (LinkedIn, etc.).

**EN**

- GHI public documentation is released under **CC BY-NC-SA 4.0**.  
- Public source code is available on GitHub (`ghi-engine`, `GHI-public`).  
- Specific agreements can be discussed for institutional-grade usage.

For institutional contact:

- Use the email address displayed on the GHI website,
- or professional channels (LinkedIn, etc.).
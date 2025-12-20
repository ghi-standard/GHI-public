# Validation Framework — Global HashCost Index (GHI)

## 1. Purpose

**FR**  
Ce document décrit le cadre de validation du standard **Global HashCost Index (GHI)**.  
L’objectif est de permettre à des tiers indépendants (chercheurs, analystes, institutions)
d’évaluer la cohérence, la robustesse et la reproductibilité du standard, sans accès aux données privées.

**EN**  
This document defines the validation framework of the **Global HashCost Index (GHI)** standard.  
Its purpose is to enable independent third parties (researchers, analysts, institutions)
to assess consistency, robustness, and reproducibility without access to private data.

---

## 2. Scope of validation

La validation porte exclusivement sur les éléments **publics** du standard GHI :

- Méthodologie publiée
- Modèle conceptuel et hypothèses
- Structure des données publiques
- Processus de génération des snapshots
- Mécanismes de traçabilité et d’intégrité (hash, index)

Les **données sources privées**, les pipelines internes et les jeux de données bruts
ne font pas partie du périmètre de validation publique.

---

## 3. Public validation artifacts

Les validateurs disposent des artefacts suivants :

- Documentation méthodologique (repository `GHI-public`)
- Spécifications de versioning
- Index public des snapshots :
data/index/snapshots_index.jsonl

- Métadonnées associées à chaque snapshot :
- `snapshot_id`
- `sha256`
- `indexed_at`
- `schema_version`

Ces éléments permettent de vérifier :
- La continuité temporelle
- L’absence de réécriture a posteriori
- La stabilité des formats publiés

---

## 4. Validation dimensions

Les travaux de validation peuvent couvrir, sans s’y limiter :

### 4.1 Methodological consistency
- Cohérence interne des hypothèses
- Stabilité des définitions dans le temps
- Alignement entre documentation et structure des données

### 4.2 Temporal integrity
- Vérification de la séquence des `snapshot_id`
- Absence de modification rétroactive non déclarée
- Correspondance entre date, hash et index

### 4.3 Reproducibility (conceptual)
- Capacité à reproduire la logique du modèle à partir de la méthodologie
- Vérification que les règles publiées sont suffisantes pour comprendre les résultats

### 4.4 Versioning discipline
- Respect du versioning annoncé
- Identification claire des changements majeurs / mineurs
- Absence de rupture silencieuse de série

---

## 5. Validation process

1. Le validateur s’appuie exclusivement sur les ressources publiques.
2. Les observations sont formulées sous forme :
 - d’issues GitHub, ou
 - de commentaires écrits transmis au maintainer.
3. Les retours peuvent concerner :
 - la méthodologie,
 - la documentation,
 - la gouvernance,
 - ou le cadre de publication.

Aucune validation ne constitue une approbation commerciale ou un endorsement.

---

## 6. Publication of validation feedback

Les retours de validation peuvent être :
- Résumés dans la documentation publique (avec accord explicite du validateur)
- Référencés de manière anonymisée
- Utilisés pour améliorer le standard dans les versions ultérieures

Le standard GHI ne revendique **aucune certification externe** à ce stade.

---

## 7. Independence and limitations

- Les validateurs restent entièrement indépendants.
- Le GHI ne fournit aucune donnée privée dans le cadre de la validation publique.
- Les conclusions relèvent de la responsabilité exclusive des validateurs.

---

## 8. Status

Ce cadre de validation est volontairement minimal et évolutif.  
Il pourra être enrichi à mesure que le standard GHI atteindra des niveaux
d’adoption institutionnelle plus avancés.

---

## 9. License

Ce document fait partie du standard ouvert GHI  
et est publié sous licence **MIT**, conformément au fichier `LICENSE.md` du dépôt.
> Source of truth — GHI Methodology  
> Generated PDFs are derived artefacts.

# Méthodologie & Transparence du GHI  
## Document méthodologique complet — Version française

---

## 1. Objectif

L’objectif de ce document est d’assurer une **auditabilité complète** du Global HashCost Index (GHI),  
de **garantir la reproductibilité** du modèle sous-jacent, et de permettre une **revue indépendante** par des tiers.

---

## 2. Modèle mathématique

Pour chaque région *r* :

### 2.1 Consommation énergétique
- **E** = Consommation électrique  
  *(TH/s × W/TH)*

### 2.2 Ajustement du refroidissement
Le facteur de refroidissement **C** dépend de la température extérieure :

\[
C = 1 + \alpha \times (T_{ext} - T_{ref})
\]

Où :
- *T<sub>ext</sub>* = température moyenne extérieure  
- *T<sub>ref</sub>* = température de référence  
- *α* = coefficient de sensibilité du refroidissement

### 2.3 Coût de l’électricité
\[
Coût\ électricité = Prix_{kWh} \times \left(\frac{E \times 24}{1000}\right)
\]

### 2.4 Amortissement du matériel
\[
Amortissement = \frac{Prix\ ASIC}{Durée\ d’amortissement}
\]

### 2.5 Coût total régional
\[
Coût\ total_r = Refroidissement + Électricité + Amortissement
\]

### 2.6 Agrégation globale
\[
GHI = \sum (Coût\ total_r \times Hashrate_r)
\]

---

## 3. Hypothèses fondamentales

- Les températures régionales sont basées sur des **moyennes NOAA sur 10 ans**.
- Les facteurs de refroidissement sont ajustés selon les **conditions climatiques régionales**.
- L’amortissement du matériel varie entre **18 et 36 mois**, selon la génération d’ASIC.
- Le mix énergétique et les prix de l’électricité reposent exclusivement sur des **sources officielles et vérifiables**.

---

## 4. Sources de données numériques

Le modèle intègre des jeux de données complets et auditables, incluant :

- Jeux de données sur les prix de l’électricité  
- Séries météorologiques historiques NOAA  
- Répartition régionale du hashrate Bitcoin  
- Spécifications et prix des fabricants d’ASIC  
- Données de prix du Bitcoin via **Kaiko** et **CoinMetrics**

---

## 5. Processus de mise à jour et de publication

- Ingestion quotidienne des données  
- Contrôles automatiques de cohérence et de plausibilité  
- Validation manuelle par le mainteneur du projet  
- Publication automatique via l’API publique GHI

---

## 6. Auditabilité & reproductibilité

Afin de garantir une reproductibilité complète :

- Le moteur de calcul Python est **public**
- Des instructions détaillées de recalcul sont fournies
- Des exemples de recalcul historique sont documentés
- Des scripts d’analyse et de vérification sont inclus

---

## 7. Transparence institutionnelle

- Registre public des versions  
- Publication explicite de toute modification méthodologique  
- Documentation complète des hypothèses et paramètres utilisés

---

## Licence & droits

© 2025 **GHI – Global HashCost Index**

Ce document est publié sous licence  
**Creative Commons Attribution – Non Commercial – Partage dans les mêmes conditions 4.0 International**  
(**CC BY-NC-SA 4.0**).
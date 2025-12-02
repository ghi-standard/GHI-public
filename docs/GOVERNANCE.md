# Governance Model — Global HashCost Index (GHI)

This document defines how the GHI standard evolves, who decides changes, and how new versions are validated.

---

## 1. Governance Principles

- Scientific neutrality  
- Transparency  
- Reproducibility  
- Independence from political or commercial influence  
- Stability required for institutional adoption  

---

## 2. Governance Structure

### 2.1 Technical Committee (TC)
Responsible for:
- methodology decisions,
- validation of formulas,
- versioning,
- reviewing PRs with technical impact.

Members (initial):
- Maintainer of GHI public standard
- Maintainer of GHI engine

### 2.2 Data & Research Committee (DRC)
Responsible for:
- evaluation of energy datasets,
- integration of new regions,
- ensuring methodological consistency.

### 2.3 Institutional Advisory Board (IAB)
Non-technical oversight:
- ensures suitability for institutional and regulatory usage,
- approves major revisions (X or Y in semantic versioning).

---

## 3. Decision Process

### Minor changes (patch version)
Examples:
- wording corrections,
- small documentation fixes.

Approved by: **1 reviewer from TC**.

### Methodology updates (minor version)
Examples:
- new region assumptions,
- updated formula,
- new energy-mix datasets.

Approved by:
- **Technical Committee majority**
- DRC notified

### Major changes (major version)
Examples:
- change to cost structure definition,
- change to global methodology.

Approved by:
- **TC**
- **DRC**
- **IAB**

---

## 4. Versioning

We use **Semantic Versioning adapted for standards**:


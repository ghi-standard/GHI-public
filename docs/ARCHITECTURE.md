# Repository Architecture — Global HashCost Index (GHI)

This document describes the structure of all GHI-related repositories and their roles.

---

## 1. Overview

The GHI standard is composed of three repositories:

### 1. `GHI-public`
Purpose:
- public documentation
- methodology and transparency
- governance documents
- API reference
- release notes and changelog
- institutional material

Visibility: **Public**

### 2. `ghi-engine`
Purpose:
- public-facing engine
- sandbox computations
- reference implementation
- CI pipeline and examples

Visibility: **Public**

### 3. `ghi-engine-private`
Purpose:
- private engine for institutional partners
- advanced datasets
- experiments before standardization

Visibility: **Private**

---

## 2. Release Flow
engine-private ──→ engine ──→ GHI-public
(experimental)     (reference)    (standard)

### Stage 1 – Experimental  
Updates tested in `engine-private`.

### Stage 2 – Reference  
Stable updates moved to `ghi-engine`.

### Stage 3 – Standard  
Validated methodology becomes part of `GHI-public`.

---

## 3. Branching Model

main          → stable
feature/*     → new features
docs/*        → documentation updates
sandbox/*     → temporary experimental regions or tests

---

## 4. Version Synchronization

| Repository           | Versioning              | Notes                                      |
|----------------------|--------------------------|--------------------------------------------|
| GHI-public           | Semantic versioning      | Drives institutional communication          |
| ghi-engine           | Matches GHI-public       | Example: engine v0.2.x = public v0.2.x      |
| ghi-engine-private   | Free versioning scheme   | Internal and experimental                   |

---

## 5. API Architecture (preview v0.2)

- REST-like schema  
- `/regions`  
- `/cost/<timestamp>`  
- `/methodology`  

Full API spec will be added in release v0.2.0.

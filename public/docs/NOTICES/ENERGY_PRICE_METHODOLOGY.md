# GHI Energy Price Methodology
**Document:** ENERGY_PRICE_METHODOLOGY  
**Version:** 1.0  
**Status:** Normative (Methodology Reference)  
**Applies to:** GHI Phase 3 — Snapshot Pipeline, External Enrichment Layer  
**Date:** 2026-01-11  

---

## 1. Purpose

This document defines the methodology used by GHI to obtain, normalize, and apply
**energy price signals** within the GHI computation framework.

The objectives are to:
- Ensure methodological consistency across regions and time.
- Preserve baseline independence and snapshot immutability.
- Enable auditable, low-cost, and resilient energy pricing inputs.
- Prevent retroactive distortion of historical outputs.

This methodology applies to **energy price signals only** and does not activate
any external data ingestion by itself.

---

## 2. Scope

### 2.1 In scope
- Electricity price signals (USD/kWh or equivalent).
- Regional and national energy price proxies.
- Public, freemium, and optional premium sources.
- Conversion and normalization rules.
- Timestamp alignment and smoothing logic.

### 2.2 Out of scope
- Carbon pricing or CO₂ adjustments.
- Taxes, subsidies, or regulatory incentives.
- Site-specific industrial contracts.
- Any modification of historical snapshots.

---

## 3. Foundational Principles (Non-Negotiable)

1. **Baseline Independence**  
   Energy prices MUST NOT redefine or rewrite the declared baseline.

2. **No Retroactive Adjustment**  
   Energy prices are applied only at snapshot creation time.

3. **Append-Only Usage**  
   All applied values must be traceable to an immutable snapshot context.

4. **Optional Enrichment**  
   External energy prices are never mandatory for index computation.

5. **Low-Cost First**  
   Preference is given to public and free sources.

---

## 4. Energy Price Signal Definition

An **energy price signal** is defined as:

- A scalar value expressed in **USD per kWh**.
- Applicable to a **region-level** abstraction.
- Representative of a **time window**, not an instant tick.

GHI does **not** attempt to model:
- intra-day spot volatility,
- contract-level heterogeneity,
- site-specific tariffs.

---

## 5. Source Selection Strategy

### 5.1 Priority order

1. **Public / Open Data**
   - National grid operators
   - Energy ministries
   - Statistical offices
   - Multilateral institutions

2. **Freemium APIs**
   - Cacheable
   - Non-lock-in
   - Disable-able without impact

3. **Premium Sources (Exception)**
   Allowed only if:
   - Public alternatives are insufficient
   - Costs are documented and bounded
   - Used strictly as non-authoritative enrichment

### 5.2 Source redundancy
Where feasible, two independent sources MAY be ingested in parallel for:
- sanity checks,
- anomaly detection,
- shadow comparison.

---

## 6. Temporal Treatment

### 6.1 Snapshot alignment
Energy prices are aligned to the **snapshot timestamp**, not to real-time.

### 6.2 Smoothing rule (Normative)
GHI uses a **rolling average window** rather than spot prices.

Default reference:
- **7-day rolling average** (preferred)
- **30-day rolling average** (acceptable for low-frequency sources)

The chosen window MUST be documented.

Unless explicitly stated otherwise, the 7-day rolling average is the normative
default for Phase 3 snapshots.

### 6.3 Missing data
If no valid energy price is available at snapshot time:
- the snapshot proceeds without external enrichment,
- the absence is explicitly recorded.

---

## 7. Currency and Normalization

### 7.1 Canonical unit
All prices are normalized to:
USD / kWh
### 7.2 FX conversion
- FX rates MUST be sourced independently from energy providers.
- Daily FX reference is sufficient.
- FX source and timestamp MUST be recorded.
FX conversion rules follow the Price and FX Methodology (Phase 3).

### 7.3 No forward filling
Energy prices are never extrapolated beyond their valid window.

---

## 8. Regional Mapping

Energy prices are mapped at the **GHI region level**, not country or site level.

Rules:
- Large countries MAY be aggregated into a single regional proxy.
- Sub-regional splits are deferred unless formally activated.
- Mapping rules are versioned and documented.

---

## 9. Audit and Traceability

Each applied energy price signal MUST carry:

- Source identifier
- Acquisition timestamp (UTC)
- Provider timestamp (if any)
- Rolling window definition
- FX source (if applicable)
- Mapping version

Absence of any field MUST be explicit.

---

## 10. Failure and Degradation Modes

If an energy source fails:
- ingestion stops gracefully,
- snapshots continue without enrichment,
- no placeholder or synthetic value is injected.

Energy pricing enrichment is **fail-open**, never fail-stop.

---

## 11. Relationship to EVKWH

EVKWH, if used, is treated as:
- optional,
- non-authoritative,
- enrichment-only.

EVKWH MUST comply with:
- rolling average rules,
- explicit tagging,
- instant deactivation capability.

---

## 12. Compliance Statement

This methodology ensures:
- no historical rewrite,
- consistent regional treatment,
- cost-controlled sourcing,
- explicit provenance,
- institutional audit readiness.

---

## 13. Changelog

- **v1.0 (2026-01-11):** Initial Phase 3 methodology reference.
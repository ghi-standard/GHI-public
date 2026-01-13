# GHI Price and FX Methodology (Phase 3)

**Document type:** Methodology Notice  
**Status:** Normative (Public Reference)  
**Applies to:** GHI Snapshot Pipeline — Price & FX Layer  
**Phase:** Phase 3 (Production – Price normalization only)  
**Version:** 1.0  
**Date:** 2026-01-11  

---

## 1. Purpose

This document defines the **methodology used by the GHI project to normalize prices and currency conversions (FX)** within Phase 3 snapshots.

The objectives are to:

- ensure **consistent, auditable, and reproducible price normalization**;
- preserve **snapshot independence** from market data providers;
- avoid retroactive modification of historical publications;
- clearly separate **price normalization** from **economic interpretation**.

This document specifies methodology only.  
It does **not** activate live pricing ingestion nor alter any existing snapshot.

---

## 2. Scope

### 2.1 In scope
- Bitcoin price reference used for unit normalization.
- Fiat currency conversion (FX) rules.
- Timestamp alignment and publication conventions.

### 2.2 Out of scope
- Trading, forecasting, or market analysis.
- Any valuation claim or investment guidance.
- Retroactive recalculation of historical snapshots.
- Mandatory reliance on any single price provider.

---

## 3. Design Principles

The Price & FX layer adheres to the following principles:

1. **Normalization, not valuation**  
   Prices are used solely for unit conversion and comparability.

2. **Source independence**  
   No single external price or FX provider is authoritative.

3. **Determinism**  
   Given the same inputs, outputs MUST be reproducible.

4. **Auditability**  
   All sources, timestamps, and conversion steps MUST be traceable.

5. **Non-retroactivity**  
   Historical snapshots MUST remain immutable.

---

## 4. Reference Currency

### 4.1 Canonical currency

- The canonical reference currency for GHI snapshots is **USD**.
- All published cost values are normalized to USD.

Other currencies, if displayed, are derived via explicit FX conversion.

---

## 5. Bitcoin Price Methodology

### 5.1 Role of BTC price

The Bitcoin price is used exclusively to:
- express cost outputs in fiat terms;
- enable cross-snapshot comparability.

It is **not** used to infer profitability, valuation, or market trends.

---

### 5.2 Source selection (Policy-level)

- Price data MAY originate from public, liquid market references.
- Multiple sources are preferred over a single provider.
- Sources MUST be documented and replaceable.

Price sources are treated as **inputs**, never as baseline truth.

At Phase 3, price normalization MAY rely on a single reference source for
operational simplicity, provided that the source remains replaceable and documented.

Multi-source aggregation, if introduced, will be explicitly versioned.
---

### 5.3 Daily Reference Price Rule (Normative)

For each GHI snapshot, the Bitcoin price reference is defined as:

- the **daily reference price of the previous UTC day (J-1)**;
- derived from the **Coinbase BTC-USD daily candle**;
- using the **daily close price** as the canonical value.

The price window is therefore fully closed at snapshot time.

No intraday price, forward-looking value, or interpolation is permitted.
---

## 6. FX Conversion Methodology

### 6.1 Conversion scope

FX conversion applies only when:
- a snapshot includes non-USD reference data; or
- auxiliary displays require local currency views.

USD remains the canonical publication currency.

---

### 6.2 FX source policy

- FX rates SHOULD come from public or widely auditable references.
- Central bank or institutional-grade FX feeds are preferred.
- No proprietary FX dependency is permitted for baseline continuity.

---

### 6.3 Conversion rule

- FX conversion uses the **rate valid at snapshot timestamp**.
- Rates are applied directly without smoothing or averaging.
- Conversion steps MUST be explicit and reversible.

---

## 7. Timestamp Alignment

### 7.1 Snapshot alignment

- All price and FX values are aligned to the snapshot `indexed_at` timestamp.
- All timestamps are expressed in **UTC**.

---

### 7.2 Window tolerance

- A short tolerance window MAY be used to select the nearest available price.
- The window size MUST be documented if applied.
- No extrapolation beyond the window is allowed.

---

## 8. Averaging and Smoothing Policy

### 8.1 Default behavior

- No moving average is applied by default.
- Each snapshot uses a discrete reference value.

---

### 8.2 Optional smoothing (future)

If smoothing is introduced:
- the method MUST be versioned;
- raw values MUST remain accessible;
- historical snapshots MUST remain unchanged.

---

## 9. Failure and Fallback Rules

- If price or FX data is unavailable:
  - snapshot generation MUST fail explicitly, or
  - the snapshot MUST be published without fiat normalization.

Silent substitution is forbidden.

---

## 10. Independence from External Providers

- External price providers MUST be considered replaceable.
- Loss of a provider MUST NOT compromise snapshot continuity.
- External data ingestion MUST remain optional and disable-able.

---

## 11. Audit and Reproducibility Guarantees

For each snapshot, it MUST be possible to reconstruct:

- price source(s) used;
- FX rate source(s) used;
- timestamps applied;
- conversion formulae;
- resulting normalized values.

Recomputation from archived inputs MUST yield identical results.

---

## 12. Change Control

- Any modification to this methodology requires:
  - a versioned update of this document;
  - explicit publication;
  - no retroactive application.

---

## 13. Compliance Statement

This methodology ensures that:

- price data is used strictly for normalization;
- FX conversion is transparent and auditable;
- the snapshot pipeline remains independent;
- historical publications remain immutable.

---

**End of document — Price and FX Methodology v1.0**
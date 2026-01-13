# PHASE 3 — Data Source Decision Matrix

**Document type:** Governance / Decision Matrix  
**Status:** Normative (Phase 3 — Pre-Activation)  
**Applies to:** GHI Phase 3 Snapshot Pipeline  
**Version:** 1.0  
**Date:** 2026-01-11  

---

## 1. Purpose

This document formalizes the **explicit, auditable decisions** regarding:

- which data signals are used in Phase 3,
- which sources are selected,
- under which dependency and cost constraints,
- and under what activation status.

This matrix exists to ensure that **no data collection is activated implicitly** and that all Phase 3 inputs are **deliberate, bounded, and reversible**.

This document **does not activate** any data ingestion.

---

## 2. Decision Principles (Binding)

All decisions in this matrix comply with the following non-negotiable rules:

- Baseline independence is preserved.
- Historical snapshots are immutable.
- External sources are optional and disable-able.
- Costs are documented and bounded.
- Shadow mode precedes any enrichment use.
- No silent dependency is permitted.

---

## 3. Signal-Level Decisions

---

## 3.1 Network Signal (Hashrate)

| Aspect | Decision |
|------|---------|
| Signal | Bitcoin network hashrate |
| Primary source | Protocol-derived (difficulty-based computation) |
| Secondary source | None |
| External dependency | None |
| Cost | $0 |
| Update frequency | Per snapshot |
| Activation status | **Active (Baseline)** |

**Rationale:**  
The Bitcoin difficulty is a protocol-level, consensus-defined parameter.  
Deriving hashrate from difficulty ensures determinism, zero cost, and long-term resilience without any third-party dependency.

---

## 3.2 Bitcoin Price (Normalization Only)

| Aspect | Decision |
|------|---------|
| Signal | BTC/USD reference price |
| Primary source | Coinbase — daily candle (J-1 close, UTC) |
| Secondary source | Independent public reference (audit only) |
| External dependency | Optional |
| Cost | $0 |
| Update frequency | Daily |
| Activation status | **Active (Normalization only)** |

**Rationale:**  
Price data is used strictly for unit normalization.  
Using a closed daily price (J-1) eliminates real-time dependency and allows delayed snapshot production without historical distortion.

---

## 3.3 FX Rates (Fiat Conversion)

| Aspect | Decision |
|------|---------|
| Signal | Fiat FX rates (to USD) |
| Primary source | Public institutional FX reference |
| Secondary source | Independent public FX feed |
| External dependency | Optional |
| Cost | $0 |
| Update frequency | Daily |
| Activation status | **Active (Normalization only)** |

**Rationale:**  
FX rates are required only for normalization.  
Daily granularity is sufficient and minimizes operational complexity.

---

## 3.4 Energy Price Signal (Regional)

| Aspect | Decision |
|------|---------|
| Signal | Regional electricity price (USD/kWh) |
| Primary source | Public national / institutional energy statistics |
| Secondary source | EVKWH (shadow ingestion only) |
| External dependency | Optional |
| Estimated cost | $0 – $50/month |
| Update frequency | Daily or weekly |
| Activation status | **Shadow mode only** |

**Rationale:**  
Public sources provide baseline continuity at low cost.  
EVKWH is treated strictly as a non-authoritative enrichment candidate, used only for validation and comparison.

---

## 4. Summary Table

| Signal | External Dependency | Cost | Activation |
|------|-------------------|------|------------|
| Network | None | $0 | Baseline |
| BTC Price | Optional | $0 | Normalization |
| FX | Optional | $0 | Normalization |
| Energy | Optional | $0–50 | Shadow only |

---

## 5. Explicit Non-Decisions

The following are **explicitly deferred**:

- Sub-regional energy price splits (e.g. US by state).
- Real-time or intraday pricing.
- Mandatory premium data providers.
- Any retroactive recalculation.
- Any predictive or forward-looking signals.

Deferral does not imply rejection.

---

## 6. Activation Gate (Mandatory)

No data ingestion may be activated unless:

- this matrix is published,
- activation status is explicitly updated,
- governance review is completed,
- and a dated activation notice is issued.

---

## 7. Change Control

Any modification to this matrix requires:

- a version bump,
- a documented rationale,
- no retroactive effect on published snapshots.

---

## 8. Compliance Statement

This decision matrix ensures that Phase 3 data usage is:

- intentional,
- transparent,
- cost-controlled,
- reversible,
- and institutionally auditable.

---

**End of document — Phase 3 Data Source Decision Matrix v1.0**
# GHI Network Signal Methodology (Phase 3)

**Document type:** Methodology Notice  
**Status:** Normative (Public Reference)  
**Applies to:** GHI Snapshot Pipeline — Network Signal Layer  
**Phase:** Phase 3 (Production – Network signal only)  
**Version:** 1.0  
**Date:** 2026-01-11  

---

## 1. Purpose

This document defines the **methodology used by the GHI project to derive the Bitcoin network hashrate signal** used in Phase 3 snapshots.

The objective is to ensure that:

- the network signal is **deterministic, reproducible, and auditable**;
- the snapshot pipeline remains **independent of any external live hashrate provider**;
- the method is stable over time and resilient to provider disappearance;
- the resulting signal can serve as a **baseline-compatible technical input**, not as a market assertion.

This document describes a **methodology only**.  
It does **not** activate, modify, or retroactively affect any published snapshot.

---

## 2. Scope

### 2.1 In scope
- Bitcoin network hashrate signal used in GHI snapshots.
- Derivation of hashrate from protocol-level parameters.
- Timestamp alignment and averaging rules.

### 2.2 Out of scope
- Published hashrate estimates from third-party providers.
- Mining pool–reported hashrate.
- Any predictive or forward-looking network metrics.
- Any modification of historical snapshots.

---

## 3. Design Principles

The network signal methodology follows these non-negotiable principles:

1. **Protocol primacy**  
   Only Bitcoin protocol-level data may be used as authoritative input.

2. **No external dependency**  
   The computation MUST NOT rely on any third-party hashrate API.

3. **Deterministic computation**  
   Given the same inputs, the output MUST be reproducible byte-for-byte.

4. **Auditability**  
   All inputs and formulas MUST be explicitly documented.

5. **Stability over precision**  
   The method favors robustness and continuity over short-term precision.

---

## 4. Source of Truth

### 4.1 Primary signal source

The GHI network hashrate signal is **derived exclusively from Bitcoin network difficulty**.

- Difficulty is a protocol-defined, consensus-level value.
- Difficulty is publicly observable and verifiable.
- Difficulty changes only at known adjustment intervals.

No external hashrate publication is considered authoritative.

---

## 5. Hashrate Derivation Method

### 5.1 Formula

The estimated network hashrate is computed using the standard protocol-based relationship:
Hashrate (H/s) = Difficulty × 2³² / Target_Block_Time

Where:
- **Difficulty** is the Bitcoin network difficulty at snapshot time.
- **2³²** is the protocol constant.
- **Target_Block_Time** is fixed at **600 seconds**.

### 5.2 Unit normalization

- Raw result is computed in **hashes per second (H/s)**.
- The canonical GHI unit for publication is:
  - **terahashes per second (TH/s)**, and
  - **exahashes per second (EH/s)** for reporting.

---

## 6. Timestamp and Alignment Rules

### 6.1 Snapshot timestamp

- The network signal timestamp is aligned to the **snapshot indexed_at timestamp**.
- All computations are performed in **UTC**.

### 6.2 Difficulty reference

- The difficulty value used is the **latest known difficulty** at snapshot time.
- No interpolation or forward adjustment is applied.

---

## 7. Averaging and Smoothing Policy

### 7.1 Default behavior

- **No moving average** is applied by default.
- Each snapshot reflects the instantaneous difficulty-derived estimate.

### 7.2 Optional smoothing (future)

If smoothing is introduced in a future version:
- the window size MUST be explicitly documented;
- raw values MUST remain available for audit;
- smoothing MUST NOT affect historical snapshots retroactively.

---

## 8. Independence from External Sources

- Published hashrate values from explorers, mining pools, or analytics firms
  are **explicitly excluded** from this methodology.
- Such sources may be ingested only in **shadow or enrichment modes**, under
  separate policies, and never as baseline inputs.

---

## 9. Failure and Fallback Behavior

- If difficulty data is unavailable at snapshot time:
  - snapshot production MUST fail explicitly;
  - no inferred or substituted value is permitted.

Silent fallback or estimation is forbidden.

---

## 10. Audit and Reproducibility Guarantees

For each snapshot, the following MUST be reconstructible:

- difficulty value used;
- formula applied;
- constants and units;
- resulting hashrate value.

Recomputation using archived snapshot inputs MUST yield identical results.

---

## 11. Change Control

- Any change to this methodology requires:
  - a versioned update of this document;
  - explicit publication of the new version;
  - no retroactive application.

---

## 12. Compliance Statement

This methodology guarantees that:

- the GHI network signal is protocol-derived;
- the snapshot pipeline remains independent and resilient;
- historical publications are immutable;
- the system is auditable by design.

---

**End of document — Network Signal Methodology v1.0**
# GHI — External Data Phase 3 Activation Notice

**Document type:** Non-Normative Notice  
**Status:** Informational / Transparency  
**Applies to:** GHI Phase 3 Operational Pipeline  
**Date:** 2026-01-11  
**Reference policy:** External Live Data Integration Policy v1.0 (Phase 2.3)

---

## 1. Purpose of This Notice

This document formally acknowledges the transition from **policy definition** to **operational readiness** regarding external data handling in GHI Phase 3.

It provides transparency on the **activation status**, **operational boundaries**, and **non-authoritative nature** of external data ingestion, without publishing any production values or exposing live endpoints.

This notice does **not** modify, override, or supersede any normative governance or policy document.

---

## 2. Policy Reference (Authoritative)

All external data handling in Phase 3 is governed exclusively by:

> **GHI External Live Data Integration Policy v1.0**  
> (Phase 2.3 — Institutional Reference)

This notice is a downstream operational acknowledgment only.

---

## 3. Activation Scope (Phase 3)

As of Phase 3:

- External data ingestion pipelines are **operationally enabled**
- Ingestion operates in **Shadow Mode only**
- No external data is required for index computation
- No external data modifies baseline snapshots
- No external data is published as authoritative

The canonical GHI index remains **snapshot-only and baseline-driven**.

---

## 4. Ingestion Mode

### 4.1 Active Mode

- **Mode A — Shadow Ingestion**
  - External data collected in append-only logs
  - Used for validation, comparison, and robustness analysis
  - No impact on public index output

### 4.2 Disabled Modes

- No authoritative dependency
- No enrichment views published
- No retroactive computation
- No coupling to availability of external providers

---

## 5. Operational Characteristics

### 5.1 Frequency
- External data collection: **daily**
- Timestamping: **UTC**
- Snapshot pipeline remains autonomous

### 5.2 Cost Strategy
- Public and open sources prioritized
- Zero or near-zero marginal cost
- No lock-in or mandatory paid provider

### 5.3 Resilience
- External ingestion can be disabled instantly
- Snapshot continuity remains unaffected

---

## 6. Source Transparency (High-Level)

At Phase 3 activation:

- Hashrate and network signals remain derived from **protocol-native metrics**
- Energy and cost signals may be shadow-ingested from:
  - public datasets
  - national statistics
  - open institutional portals
- EVKWH is treated strictly as a **candidate, non-authoritative source**

No source listed here is required for index continuity.

---

## 7. Data Publication Status

- ❌ No external raw data published
- ❌ No enriched index values published
- ❌ No external dataset exposed publicly
- ✅ Auditability preserved internally
- ✅ Append-only guarantees enforced

---

## 8. Audit and Verification

Internal mechanisms ensure:

- Content-addressable storage
- Immutable ingestion logs
- Daily continuity checks
- Independent snapshot validation
- Separable audit trails for external vs baseline data

These mechanisms are operational but **not exposed**.

---

## 9. Governance Boundary Statement

This notice:

- Does not activate any new governance rule
- Does not redefine baseline assumptions
- Does not authorize economic interpretation of external data
- Does not constitute a data publication

All normative authority remains with existing governance and policy documents.

---

## 10. Closing Statement

Phase 3 confirms that GHI is capable of handling external live data **without dependency, without lock-in, and without compromising baseline integrity**.

External data remains:
- optional
- non-authoritative
- disable-able
- auditable
- explicitly separated

---

**End of document**
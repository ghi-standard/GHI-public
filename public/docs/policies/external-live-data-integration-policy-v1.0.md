# GHI External Live Data Integration Policy (Phase 2.3)
**Version:** 1.0  
**Status:** Normative (Institutional Reference)  
**Applies to:** GHI Public Index, Snapshot Pipeline, External Live Sources Layer  
**Date:** 2026-01-06  
**Authoring context:** GHI Phase 2.3 (preparatory; no live ingestion activation)

---

## 1. Purpose

This policy defines how the GHI project may integrate external LIVE data sources (including EVKWH as a candidate) **after** the internal live ingestion pipeline has been fully stabilized (Phase 2.2).

The objectives are:

- Preserve the integrity and independence of the existing snapshot pipeline and declared baseline.
- Keep the public index stable and computable without any external dependency.
- Enable progressive, auditable, append-only ingestion of optional live signals.
- Enforce a “low-cost first” sourcing strategy.

This document is a reference policy. It does **not** activate ingestion of any external source.

---

## 2. Scope and Definitions

### 2.1 In scope
- External LIVE data providers (energy pricing, grid metrics, network signals, cost proxies).
- Public APIs, open data portals, freemium feeds, lightweight partnerships.
- Source availability and disappearance handling (fallback and disable modes).
- Traceability, tagging, audit requirements for external data.

### 2.2 Out of scope
- Any retroactive modification of existing snapshots.
- Any rewrite of historical publications.
- Any mandatory coupling of the index computation to a single external provider.
- Any refactor of the existing internal snapshot pipeline.

### 2.3 Definitions
- **Baseline:** The officially declared institutional reference dataset and assumptions used for the GHI snapshot pipeline.
- **Snapshot pipeline:** The internal GHI pipeline producing immutable, append-only snapshot artifacts.
- **External LIVE sources layer:** A separate ingestion and logging layer for optional external signals.
- **Enrichment:** Non-authoritative, optional use of external signals to provide additional views; never required for the index to exist.

---

## 3. Non-Negotiable Principles

### 3.1 Baseline integrity
External sources MUST NOT change baseline meaning, baseline declarations, or historical snapshot content.

### 3.2 No historical rewrite
External sources MUST NOT trigger any modification, replacement, or recalculation of previously published snapshots.

### 3.3 Append-only everywhere
All external ingestion logs MUST be append-only and content-addressable or otherwise verifiably immutable.

### 3.4 Non-dependency by design
The public index MUST remain computable and stable without any external provider. External sources are strictly optional.

### 3.5 Strict separation
Internal datasets and external datasets MUST remain clearly separated in storage, schemas, documentation, and publication paths.

---

## 4. Target Architecture (Conceptual)

### 4.1 Layers
1. **Internal Snapshot Pipeline (Authoritative)**
   - Produces append-only snapshots
   - Declared baseline
   - Stable publication

2. **Index Engine (Stable)**
   - Computes public index from snapshots alone
   - May optionally read external enrichment datasets

3. **External LIVE Sources Layer (Non-Critical)**
   - Ingests external signals in append-only logs
   - Tags sources explicitly
   - Can be disabled at any time without affecting baseline or index continuity

### 4.2 Direction of dependency
- Index Engine may read External LIVE datasets.
- External LIVE ingestion MUST NOT depend on, modify, or block the snapshot pipeline.

---

## 5. External Data Lifecycle (Policy)

### 5.1 Ingestion modes
External sources MAY be introduced only through progressive modes:

- **Mode A — Shadow Ingestion (Required first)**
  - Data is collected and stored as append-only logs
  - No impact on public index output
  - Used only for validation, comparison, and robustness checks

- **Mode B — Non-Authoritative Enrichment (Optional)**
  - External data may be used to produce supplementary “views”
  - Views must be explicitly labeled as non-authoritative
  - The canonical index remains unchanged and snapshot-only

### 5.2 Publication rules
- External datasets MUST be published in a clearly separated namespace/path.
- External datasets MUST include source metadata and licensing notes.
- External datasets MUST never be presented as baseline or authoritative.

### 5.3 Deactivation rules
External sources MUST be disable-able instantly without breaking index computation, publication, or continuity.

---

## 6. Source Tagging and Traceability (Mandatory)

Every external data record MUST be accompanied by:

- **Source identifier** (stable provider ID)
- **Acquisition timestamp** (UTC)
- **Provider timestamp** (if provided)
- **Retrieval method** (API, open portal, partner feed)
- **License / access terms reference** (as available)
- **Integrity fields** (hashes or signed receipts if available)
- **Versioned mapping rules** (if transformation is applied)

If any of these fields are unavailable, the ingestion MUST store the absence explicitly (e.g., null or “unknown”), not infer.

---

## 7. EVKWH Status (Candidate Source)

### 7.1 Role
EVKWH is a candidate external LIVE provider intended to supply optional energy cost signals.

### 7.2 Non-authoritative position (strict)
EVKWH is not a source of truth for GHI baseline, snapshots, or historical publications.

EVKWH MUST be treated as:
- Optional
- Non-critical
- Disable-able
- Explicitly tagged
- Restricted to enrichment modes only

### 7.3 No structural reliance
The index computation MUST never require EVKWH availability.

### 7.4 Limitations
- Provider availability may change
- Pricing terms may evolve
- Coverage and methodology may vary over time

These limitations MUST be documented whenever EVKWH is enabled in enrichment mode.

---

## 8. Low-Cost First Strategy (Normative)

### 8.1 Priority order
External sourcing MUST follow this priority order:

1. **Free / Open Access**
   - Official grid operators and public energy portals
   - National statistics feeds
   - Public research datasets
   - Public network metrics where legally permissible

2. **Freemium / Soft-Quota APIs**
   - Acceptable only if cacheable and non-lock-in
   - Must not become required for continuity

3. **Premium Providers (Exception only)**
   Allowed only if:
   - No viable free alternative exists
   - Institutional value is clearly demonstrated
   - The provider is optional and disable-able
   - Costs are explicitly documented and bounded

### 8.2 Cost documentation
For each external source, the project MUST document:
- Expected monthly cost at current usage
- Marginal cost per additional unit of usage
- Quotas, throttling behavior, and fallback plan

If cost terms are unknown, the source MUST remain in “candidate” status.

---

## 9. Fallback and Resilience (Mandatory)

### 9.1 Source disappearance
If an external source becomes unavailable:
- Ingestion MUST stop gracefully
- Index computation MUST remain unaffected
- The system MUST fall back to:
  - alternative open sources, or
  - “no enrichment” mode

### 9.2 Multi-source preference
Where possible, prefer redundant sourcing:
- Two independent sources for the same signal class
- Cross-checking and anomaly detection in shadow mode

---

## 10. Auditability Requirements

### 10.1 Reproducibility
External ingestion MUST be reproducible from:
- raw append-only logs
- documented mapping rules and versions
- explicit source metadata

### 10.2 Separation of evidence
Audit trails for external data MUST be separable from baseline audit trails.

### 10.3 Explicit labeling
All outputs influenced by external data MUST state:
- which source(s) were used
- what version of mapping rules
- that the result is non-authoritative enrichment

---

## 11. Security and Operational Constraints

- External ingestion endpoints MUST be isolated from baseline and snapshot production systems.
- Credentials, if any, MUST be stored outside the repository and rotated.
- Rate limits and retries MUST not compromise append-only guarantees.
- No external source may introduce a write path into historical snapshot storage.

---

## 12. Activation Checklist (Gated)

External sources MAY NOT be ingested or published until Phase 2.2 is fully validated.

Minimum activation gates:

- Internal live ingestion pipeline validated as autonomous
- Public index stable without enrichment
- Append-only logging mechanisms verified
- Source tagging implemented and tested
- Deactivation and fallback tested end-to-end

EVKWH-specific gates (in addition):
- Cost terms documented and bounded
- Licensing/access constraints documented
- Shadow ingestion completed with anomaly review
- Clear public statement: non-authoritative enrichment only

---

## 13. Governance and Change Control

- Any new external source MUST be added via a versioned policy update or an approved addendum.
- Changes MUST be documented in a changelog entry.
- External integration MUST never silently change the canonical index definition.

---

## 14. Compliance Statement (Policy-Level)

This policy enforces:
- Baseline independence
- Append-only data handling
- Non-rewrite of historical publications
- Explicit provenance and tagging
- Low-cost sourcing priority
- Optional enrichment only

---

## 15. Changelog

- **v1.0 (2026-01-06):** Initial institutional reference for Phase 2.3.


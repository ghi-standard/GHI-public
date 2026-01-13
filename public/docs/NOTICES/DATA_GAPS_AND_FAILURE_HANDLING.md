# GHI Data Gaps and Failure Handling Policy (Phase 3)

**Document type:** Policy & Methodology Notice  
**Status:** Normative (Public Reference)  
**Applies to:** GHI Phase 3 — Snapshot Pipeline, External Enrichment Layers  
**Version:** 1.0  
**Date:** 2026-01-11  

---

## 1. Purpose

This document defines how the GHI project handles **data gaps, operational failures, and temporary unavailability of inputs** during Phase 3 operations.

Its objectives are to:

- ensure continuity of the snapshot pipeline under adverse conditions;
- prevent retroactive modification of historical data;
- provide explicit, auditable rules for missing or incomplete inputs;
- formalize acceptable degradation modes (fail-open design);
- protect the project against operational, legal, and reputational risks.

This document is **normative** and applies to all Phase 3 snapshots.

---

## 2. Scope

### 2.1 In scope
- Temporary unavailability of external data sources.
- Operational bugs in ingestion, enrichment, or validation layers.
- Infrastructure downtime or maintenance windows.
- Human unavailability (holidays, illness, delayed intervention).
- Partial snapshot enrichment failures.

### 2.2 Out of scope
- Retrospective correction of historical snapshots.
- Manual backfilling or reconstruction of missed enrichments.
- Economic interpretation of missing data.
- Any alteration of baseline definitions.

---

## 3. Foundational Principles (Non-Negotiable)

1. **Snapshot Immutability**  
   Once indexed, a snapshot is final and MUST NOT be modified.

2. **No Retroactive Repair**  
   Missed data or failures are never repaired ex post.

3. **Fail-Open Architecture**  
   Absence of optional data MUST NOT stop snapshot production.

4. **Explicit Absence Over Silent Substitution**  
   Missing data is recorded as missing, never inferred.

5. **Operational Realism**  
   Temporary failures and human constraints are expected and tolerated.

---

## 4. Classification of Failures

### 4.1 External data unavailability
Examples:
- API outage
- Public data portal offline
- Rate limit exhaustion
- Provider suspension or shutdown

### 4.2 Internal processing failures
Examples:
- Script error
- Data validation failure
- Storage write failure
- Scheduler malfunction

### 4.3 Human or operational delay
Examples:
- Project maintainers unavailable
- Bug discovered during vacation period
- Delayed intervention exceeding one or more snapshot cycles

---

## 5. Mandatory Behavior by Failure Type

### 5.1 Authoritative snapshot inputs (baseline)
If a required baseline input is unavailable:
- snapshot generation MUST fail explicitly;
- no snapshot is published for that cycle;
- no inferred or substituted value is permitted.

### 5.2 External enrichment inputs (non-authoritative)
If an external enrichment input is unavailable:
- snapshot generation MUST proceed;
- the enrichment field MUST be omitted or marked as unavailable;
- the absence MUST be traceable in snapshot metadata.

External enrichment is **fail-open**.

---

## 6. Handling of Prolonged Outages

### 6.1 Duration neutrality
There is **no maximum tolerated outage duration** for external enrichment.

Whether the outage lasts:
- one hour,
- several days,
- or multiple weeks,

the behavior remains unchanged.

### 6.2 No catch-up mechanism
After service restoration:
- enrichment resumes from that point forward only;
- missed periods remain permanently unfilled.

No backfill, replay, or reconstruction is allowed.

---

## 7. Human Unavailability Scenarios

The GHI system explicitly assumes that:

- maintainers may be unavailable for extended periods;
- immediate intervention is not always possible;
- operational continuity MUST NOT rely on constant human presence.

As a consequence:
- snapshots MAY be published without enrichment for extended periods;
- this state is considered **normal and compliant**;
- no explanatory justification is required beyond recorded metadata.

---

## 8. Publication and Disclosure Rules

### 8.1 Public transparency
Missing data does NOT require:
- public incident reports,
- operational announcements,
- corrective disclosures.

The snapshot artifacts themselves constitute sufficient disclosure.

### 8.2 Labeling requirements
If enrichment is absent:
- the snapshot MUST remain valid;
- outputs MUST NOT imply completeness where data is missing;
- no synthetic placeholder values are permitted.

---

## 9. Audit and Review Implications

From an audit perspective:

- absence of enrichment is not a failure;
- absence is an explicit state, not an error;
- historical gaps are expected and acceptable;
- snapshot continuity is evaluated independently of enrichment completeness.

Auditors MUST evaluate:
- adherence to declared rules,
- immutability guarantees,
- traceability of absence.

---

## 10. Relationship to Other Documents

This document complements:
- Network Signal Methodology (Phase 3)
- Price and FX Methodology (Phase 3)
- Energy Price Methodology (Phase 3)
- External Live Data Integration Policy

In case of conflict, **immutability and non-retroactivity prevail**.

---

## 11. Change Control

- Any change to this policy requires a versioned update.
- Changes apply only to future snapshots.
- Historical behavior remains frozen and valid.

---

## 12. Compliance Statement

This policy ensures that:

- operational imperfections do not compromise integrity;
- historical data remains immutable;
- enrichment remains optional and non-authoritative;
- the system is robust to real-world constraints;
- GHI remains institutionally defensible under prolonged disruption.

---

**End of document — Data Gaps and Failure Handling Policy v1.0**
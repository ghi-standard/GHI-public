# Proof of Regularity — Phase 3 Production (Public, No Data)

This document is a non-normative public disclosure intended to demonstrate
operational regularity and audit readiness of the GHI Phase 3 production pipeline.
It does not publish production numerical outputs.

## 1. Scope

This notice covers:
- the existence of a scheduled Phase 3 snapshot production process,
- the audit trail properties (immutability, traceability),
- the retention policy for production artifacts.

This notice does not:
- disclose regional or global production values,
- grant data access,
- modify or interpret frozen governance documents.

## 2. Production cadence (Geneva time)

Phase 3 snapshots are generated on a daily schedule during the following window:
- 00:00–04:00 (Europe/Zurich / Geneva)

This window is chosen to:
- reduce operational impact,
- allow same-day remediation if an incident occurs.

## 3. Snapshot identity & index format

Each produced snapshot is referenced by an index entry with the following structure:

```json
{"snapshot_id":"2026-01-02-from20251215r20260102233003","sha256":"c5db3975c519578b36bde4ebe74190b08d442f0e1e5a6367022fa89905cfda5d","indexed_at":"2026-01-02T23:30:03Z","schema_version":"1.0"}

Properties:
	•	snapshot_id is a unique identifier for the produced artifact,
	•	sha256 is a cryptographic digest of the snapshot payload,
	•	indexed_at is the UTC timestamp at indexing time,
	•	schema_version declares the structural schema of the snapshot.

4. Audit trail properties

Phase 3 production is designed to be audit-ready through:
	•	append-only indexing,
	•	cryptographic hashing per snapshot,
	•	versioned publication of operational metadata (without releasing private values).

These properties support:
	•	integrity checks,
	•	reproducibility verification under controlled access,
	•	third-party audit procedures when applicable.

5. Retention policy

Phase 3 production artifacts are retained for:
	•	30 rolling days (default)

Older artifacts may be retained under controlled regimes for:
	•	institutional audits,
	•	reproducibility replays,
	•	contractual delivery (licensed access),
subject to governance decisions and access terms.

6. Relationship to Phase 2 (Sandbox)

Phase 2 remains available for public integration and demonstration using synthetic data.
Phase 3 operates under a private production regime using real inputs, with controlled disclosure.

For the formal transition notice, see:
	•	public/docs/governance/PHASE_2_TO_PHASE_3_TRANSITION.md

End of document.
GHI — Phase Transition Notice

Phase 2 (Sandbox) → Phase 3 (Production)

Document status: Normative transition notice
Audience: Institutional reviewers, partners, auditors
Scope: Methodology, data regime, operational continuity

⸻

1. Purpose of this document

This document formally defines and documents the transition of the Global HashCost Index (GHI) from Phase 2 (Sandbox) to Phase 3 (Production).

Its purpose is to:
	•	prevent misinterpretation between synthetic and real datasets,
	•	ensure methodological continuity,
	•	provide a clear audit trail for institutional reviewers,
	•	establish a clean separation between pedagogical validation and production-grade operation.

This document does not introduce any methodological change.

⸻

2. Phase 2 — Sandbox (Completed)

2.1 Role of Phase 2

Phase 2 was designed as a public sandbox with the following objectives:
	•	validate the GHI data model,
	•	validate the API contracts,
	•	validate institutional readability,
	•	provide integration and demonstration material.

2.2 Nature of Phase 2 data

All data exposed during Phase 2:
	•	was synthetic,
	•	was non-economic,
	•	was non-actionable,
	•	was explicitly labeled as fake / illustrative.

No real-world assumptions, calibrated parameters, or production data were used.

2.3 Status

Phase 2 is completed, frozen, and remains available for educational and integration purposes only.

⸻

3. Phase 3 — Production (Active)

3.1 Role of Phase 3

Phase 3 activates the real GHI engine under a controlled, private, and auditable regime.

Its objectives are:
	•	continuous production of real snapshots,
	•	internal validation and stability testing,
	•	preparation for institutional-grade access.

3.2 Nature of Phase 3 data

Phase 3 data:
	•	is real, derived from controlled internal sources,
	•	is versioned, timestamped, and cryptographically hashed,
	•	is produced under a private operational regime,
	•	is not publicly exposed by default.

No Phase 3 numerical data is made public unless explicitly decided under a dedicated access framework.

⸻

4. Methodology Continuity (Critical Statement)

The GHI methodology is unchanged between Phase 2 and Phase 3.

Specifically:
	•	the data model remains identical,
	•	the structural definitions of costs, regions, and aggregation are preserved,
	•	only the data origin and execution context differ.

This guarantees:
	•	comparability,
	•	reproducibility,
	•	auditability.

There is no methodological reset, fork, or reinterpretation between phases.

⸻

5. Operational Separation
| Aspect            | Phase 2 — Sandbox        | Phase 3 — Production            |
|------------------|--------------------------|---------------------------------|
| Data             | Synthetic                | Real                             |
| Exposure         | Public                   | Private (controlled)             |
| Purpose          | Validation & demos       | Production & audit               |
| Actionability    | None                     | Potential (restricted)           |
| Economic meaning | None                     | Real                             |
| Update frequency | Ad hoc                   | Scheduled (daily)                |

The two phases coexist but serve distinct roles.

⸻

6. Snapshot Production & Audit Trail

Phase 3 snapshots:
	•	are produced on a daily schedule,
	•	follow a fixed snapshot schema (v1.0),
	•	are indexed in an append-only registry,
	•	include:
	•	snapshot identifier,
	•	SHA-256 hash,
	•	indexing timestamp,
	•	schema version.

This ensures:
	•	immutability,
	•	traceability,
	•	external audit readiness.

⸻

7. Public Communication Policy

At the time of this document:
	•	Phase 3 numerical results are not publicly published,
	•	public communication may reference:
	•	existence of production,
	•	continuity of operation,
	•	snapshot counts,
	•	structural integrity.

Any publication of Phase 3 data will require:
	•	explicit governance decision,
	•	controlled disclosure format,
	•	documented scope.

⸻

8. Forward Compatibility

This transition explicitly preserves compatibility with:
	•	future regional refinements,
	•	additional dimensions (e.g. energy-normalized metrics),
	•	extensions such as NVkWh, when activated.

Such extensions will be introduced without retroactive modification of Phase 3 historical data.

⸻

9. Conclusion

Phase 2 and Phase 3 are not competing states, but successive and complementary layers of the GHI project.

Phase 2 validated the structure.
Phase 3 validates reality.

This transition is:
	•	deliberate,
	•	controlled,
	•	documented,
	•	institution-ready.

⸻

End of document
Global HashCost Index (GHI)
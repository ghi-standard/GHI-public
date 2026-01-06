# Snapshots — Baseline (Operational)

## TL;DR (institutional)
- The snapshots directory is **append-only**: snapshots are never edited or deleted.
- There is a **pre-baseline** period (historical / non-operational) and a **post-baseline** period (operational).
- **Only post-baseline snapshots are eligible for public publication** (index / website).
- Pre-baseline snapshots are kept for traceability and reproducibility, but are **out of scope** for official publication.
- Multiple snapshots may exist from identical RAW inputs: differences reflect **pipeline run / versioning**, not source-data changes.

## Operational baseline (institutional anchor)

- BASELINE_SNAPSHOT_ID: `2026-01-05-from20251215r20260105233002`
- BASELINE_SHA256: `8fb3bf4355b6ace3723cc750108889b3ba297a3a94e73141b99532975eaf2ae6`
- BASELINE_INDEXED_AT: `2026-01-05T23:30:02Z`
- Operational rule: **Only snapshots indexed at or after the baseline are operational for public use.**  
  Pre-baseline snapshots are retained for traceability/debugging only and are **non-operational**.

## Operational rule
Any snapshot with `snapshot_id` strictly **older than BASELINE_SNAPSHOT_ID** is considered **pre-baseline** and must not be used for official/public publication.

# Snapshots Baseline & Historical Context

## Purpose of this document

This document defines the baseline and historical context of the snapshot system used by the Global HashCost Index (GHI).

It provides a clear distinction between:
- early experimental snapshots created during system design and validation,
- and the operational snapshot process currently in use.

No snapshot data has been removed or altered retroactively.

---

## Snapshot concept (high level)

A **snapshot** represents a deterministic, validated state of the private GHI dataset at a given point in time.

Each snapshot:
- is built from a complete set of RAW inputs,
- is validated against internal contracts,
- is cryptographically hashed (SHA-256),
- is indexed for traceability and reproducibility.

Snapshots are immutable once created.

---

## Historical phase (pre-baseline)

### Period
**Before 2025-12-27**

### Characteristics
During this phase:
- multiple snapshot identifier formats were used,
- some snapshots were generated for testing, iteration, or validation purposes,
- the snapshot system itself was evolving (naming, scheduling, orchestration).

These snapshots:
- may reference identical RAW inputs,
- may differ only by execution context or validation cycle,
- remain valid artifacts of the development process.

They have been intentionally preserved for transparency and auditability.

---

## Baseline declaration (operational phase)

### Baseline date
**2025-12-27 (UTC)**

### From this date forward:
- snapshot identifiers follow a stable and documented format,
- snapshot creation is automated and scheduled,
- the snapshot pipeline is considered operational,
- snapshot indexing follows a consistent schema.

All snapshots created on or after this date conform to the current production rules.

---

## RAW data considerations

RAW input datasets are **versioned and time-stamped independently** from snapshot creation.

As a result:
- multiple snapshots may reference the same RAW date,
- identical RAW hashes across snapshots are expected and normal,
- this does not indicate duplication or data inconsistency.

Snapshots capture **state**, not novelty.

---

## Immutability & publication policy

- No snapshots are deleted or rewritten after creation.
- No historical snapshot identifiers are altered.
- The public snapshot index is append-only.
- Corrections or changes are introduced only through new snapshots.

This approach ensures:
- full traceability,
- audit compatibility,
- long-term institutional trust.

---

## Status

The snapshot system is **operational** and **stable**.

This document serves as the authoritative reference for interpreting historical snapshot entries and understanding the current baseline.
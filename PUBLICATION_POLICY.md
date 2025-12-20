# GHI Snapshot Publication Policy

## 1. Purpose

This document defines the official publication policy for
**Global HashCost Index (GHI) snapshots**.

It clarifies:
- how snapshots are produced,
- how they are indexed,
- how and when they are publicly released.

This policy applies to the `GHI-public` repository.

---

## 2. Snapshot lifecycle

Each GHI snapshot follows a strict, ordered lifecycle:

1. **Raw data collection** (private)
2. **Normalization & validation** (private)
3. **Snapshot build** (private, deterministic)
4. **Cryptographic hashing (SHA-256)** (private)
5. **Private indexing** (append-only)
6. **Public index export** (metadata only)
7. **Public publication** (controlled)

At no point is raw or proprietary data exposed publicly.

---

## 3. Production frequency

- Snapshots are **generated daily** when sufficient input data is available.
- If daily raw inputs are incomplete, snapshot generation may be deferred
  or use the latest validated dataset.

Snapshot generation is automated but **not equivalent to publication**.

---

## 4. Immutability guarantees

- Once built, a snapshot is **immutable**.
- The snapshot identifier and its SHA-256 hash are permanent.
- Snapshots are never altered, overwritten or deleted.

If an error is discovered:
- a **new snapshot** is generated,
- the previous snapshot remains publicly referenced.

This ensures full historical traceability.

---

## 5. Public publication policy

Public publication follows these principles:

- Publication is **intentional and controlled**.
- Snapshots are published via updates to:
data/index/snapshots_index.jsonl

- Each publication is:
- versioned,
- committed,
- traceable via Git history.

Publication may be:
- **periodic** (e.g. weekly or monthly),
- **event-driven** (methodology milestone, audit step),
- **manual or semi-automated**, depending on governance stage.

At early stages, publication is not strictly daily by design.

---

## 6. Separation of concerns

| Layer | Visibility | Purpose |
|------|-----------|---------|
| Raw data | Private | Data ingestion |
| Normalized data | Private | Model consistency |
| Snapshots | Private | Deterministic computation |
| Snapshot index (metadata) | Public | Transparency & audit |
| Full datasets | Not public | Intellectual property |

---

## 7. Governance alignment

This publication policy is governed by:

- `GOVERNANCE.md`
- `changelog.md`
- Git commit history

Any change to this policy requires:
- a public Pull Request,
- maintainer review,
- versioned publication.

---

## 8. Status

Current status: **Active – early public phase**

This policy may evolve as:
- independent validation increases,
- institutional users onboard,
- audit requirements mature.
# Terminology Charter

**Governance Layer:** v1.0  
**Effective Date:** 2026-01-08  
**Status:** Governance — Binding (Terminology Control)

---

## 1. Purpose

This charter defines canonical terms used across the GHI governance corpus.

It prevents synonym drift, interpretive requalification, and inconsistent usage.
Where a term in a lower-ranked document deviates from this charter, this charter controls the meaning.

---

## 2. Canonical Terms

### 2.1 Governance Instrument
A document designated as part of the governance corpus and intended to control interpretation, scope, precedence, exclusions, or change procedures.

### 2.2 Frozen Document
A governance instrument declared intangible.
A frozen document MUST NOT be edited, amended, corrected, restated, or reformatted.
Any weakness detected in a frozen document may only be addressed through a higher-ranked new governance instrument.

### 2.3 Governance Layer
A published governance version identifier (e.g., v1.0) that groups controlling governance instruments under a single effective layer.

### 2.4 Effective Date
The publication date on which a governance instrument becomes controlling for interpretation, as stated within the instrument.

### 2.5 Normative
A statement or instrument intended to control interpretation and governance behavior within the project’s internal governance framework.

### 2.6 Non-Normative
A statement intended to inform only (e.g., pointers, explanations, summaries) and which carries no independent controlling force.

### 2.7 Binding (Internal)
“Binding” means controlling for interpretation within the internal governance framework of the GHI project only.
It does not assert legal enforceability, jurisdiction, regulatory authority, or external coercive effect.

### 2.8 Interpretive Constraint
A rule that limits how language may be read, including prohibitions on implied obligations, implied scope re-inclusions, or future-capability inferences.

### 2.9 Precedence
The controlling order between governance instruments, defined exclusively by the designated precedence instrument(s).
Where a hierarchy is defined, no other document may restate or redefine it unless explicitly authorized by a higher-ranked governance act.

### 2.10 Scope Exclusion
A governance-level rule that removes a topic, capability, activity, or system class from project scope prospectively.
Re-inclusion requires an explicit governance act stating boundaries and effective date.

### 2.11 Re-Inclusion
A standalone governance act that explicitly reverses a scope exclusion.
Re-inclusion SHALL NOT occur by implication, adjacency, evolution, roadmap language, or interpretive requalification.

### 2.12 Notice
A governance instrument that applies interpretive constraints, exclusions, or limitations prospectively, without amending or restating prior publications.

---

## 3. Prohibited Practices (Interpretive Lock)

The following are prohibited unless expressly defined here:
- introducing synonyms for canonical terms without definition,
- using “binding” to imply external enforceability,
- using “authority” or “supremacy” to imply jurisdiction,
- inferring scope re-inclusion from non-normative documents (including roadmaps),
- treating pointers, summaries, or archives as normative unless explicitly designated.

---

## 4. Canonical References

- Frozen metadata register: `FROZEN_DOCS_METADATA.md`
- Normative precedence (exclusive source): `NORMATIVE_PRECEDENCE_ORDER.md`
- Interpretation constraints notice: `NORMATIVE_PRECEDENCE_AND_INTERPRETATION.md`
- Scope exclusion (external live ingestion): `SCOPE_EXCLUSION_EXTERNAL_LIVE_INGESTION.md`
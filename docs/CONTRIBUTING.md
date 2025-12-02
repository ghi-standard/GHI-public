# Contributing to the Global HashCost Index (GHI)

Thank you for your interest in contributing to the Global HashCost Index (GHI).
This repository defines the **public documentation**, **methodologies**, and **governance rules** of the GHI standard.

All contributions follow a strict review process to ensure:
- methodological consistency,
- scientific neutrality,
- reproducibility of the standard,
- transparency for institutions and researchers.

---

## 1. Branch Naming Convention

All contributions must use the following branch format:
feature/
fix/
docs/

Examples:
- `feature/new-region-energy-model`
- `fix/typo-methodology`
- `docs/add-governance-section`

---

## 2. Workflow
main          → protected (no direct commits)
feature/*     → open for contributions
docs/*        → documentation-only changes

Steps:

1. Fork or clone the repository.
2. Create a new branch following naming rules.
3. Make your changes.
4. Open a Pull Request into `main`.
5. Wait for automated checks to pass.
6. Your PR will be reviewed by the **GHI Technical Committee**.
7. Once approved, it is merged via **Squash & Merge**.

Direct pushes to `main` are blocked.

---

## 3. Pull Request Requirements

Every PR must include:

- A clear explanation of the change.
- A justification of methodological impact (if any).
- Links to scientific sources or energy-mix datasets (when relevant).
- Consistency with the GHI core definitions (`/standard/`, `/docs/`).
- No breaking modification of the public API without discussion.

---

## 4. Documentation Standards

When modifying documentation:

- Follow Markdown best practices.
- Keep formulas readable and consistent.
- Keep the tone neutral, scientific, and institution-oriented.
- All methodology updates must be reflected in `/docs/`.

---

## 5. Change Categorization

Every PR must be labeled with **exactly one**:

- `enhancement`
- `bug`
- `documentation`
- `methodology`
- `governance`
- `breaking-change`

The GHI Technical Committee reserves the right to reclassify contributions.

---

## 6. Licensing

By contributing, you agree that your contributions are published under the repository license and may be incorporated into future versions of the GHI standard.

---

## 7. Contact

For questions related to contributions:
- Email: ghi-standard@protonmail.ch
- Official website: https://github.com/ghi-standard


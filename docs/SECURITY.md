# Security Policy — Global HashCost Index (GHI)

This document explains how to report vulnerabilities concerning:

- the GHI public standard,
- documentation or formulas,
- the GHI engine (sandbox or private versions),
- the public API documentation.

---

## 1. Reporting a Security Issue

Do **not** open a public GitHub issue.

Instead, report privately to:

**security@ghi-standard.org**  
(PGP key to be added in v0.2.0)

Include:

- description of the vulnerability  
- impact assessment  
- steps to reproduce  
- affected modules or documents  
- your contact information  

We commit to acknowledge reports within **72 hours**.

---

## 2. Scope

### In scope
- methodological vulnerabilities (leading to incorrect cost estimation),
- data integrity issues,
- risks of misinterpretation in documentation,
- exposure of sensitive dataset assumptions,
- sandbox engine execution issues.

### Out of scope
- third-party datasets,
- unmaintained forks,
- external API misuse.

---

## 3. Disclosure Policy

We follow a **responsible disclosure** model:

1. Researcher reports privately  
2. We analyze and reproduce  
3. Fix prepared  
4. Researcher is informed  
5. Public disclosure coordinated  
6. Patch included in next tagged release  

---

## 4. Security Updates

Security-relevant releases use the format:
vX.Y.Z-security.N

Example:
`v0.1.1-security.1`

> Source of truth — GHI Methodology  
> Generated PDFs are derived artefacts.
# GHI Methodology & Transparency  
## Full Methodological Document — English Version

---

## 1. Objective

The objective of this document is to ensure **full auditability** of the Global HashCost Index (GHI),  
to **guarantee reproducibility** of the underlying model, and to allow **independent review** by third parties.

---

## 2. Mathematical Model

For each region *r*:

### 2.1 Energy Consumption
- **E** = Power consumption  
  *(TH/s × W/TH)*

### 2.2 Cooling Adjustment
Cooling factor **C** depends on the external temperature:

\[
C = 1 + \alpha \times (T_{ext} - T_{ref})
\]

Where:
- *T<sub>ext</sub>* = external average temperature  
- *T<sub>ref</sub>* = reference temperature  
- *α* = cooling sensitivity coefficient

### 2.3 Electricity Cost
\[
Electricity\ Cost = Price_{kWh} \times \left(\frac{E \times 24}{1000}\right)
\]

### 2.4 Hardware Depreciation
\[
Depreciation = \frac{ASIC\_price}{Depreciation\_duration}
\]

### 2.5 Regional Total Cost
\[
Total\ Cost_r = Cooling + Electricity + Depreciation
\]

### 2.6 Global Aggregation
\[
GHI = \sum (Total\ Cost_r \times Hashrate_r)
\]

---

## 3. Core Assumptions

- Regional temperatures are based on **10-year NOAA averages**.
- Cooling factors are adjusted according to **regional climate conditions**.
- Hardware depreciation ranges between **18 and 36 months**, depending on ASIC generation.
- Regional energy mix and electricity prices rely exclusively on **official and verifiable sources**.

---

## 4. Digital Data Sources

The model integrates complete and auditable datasets, including:

- Electricity price datasets  
- NOAA historical weather series  
- Regional Bitcoin hashrate distribution  
- ASIC manufacturer specifications and pricing  
- Bitcoin market price data via **Kaiko** and **CoinMetrics**

---

## 5. Update & Publication Process

- Daily data ingestion  
- Automated consistency and sanity checks  
- Manual validation by the project maintainer  
- Automatic publication via the GHI public API

---

## 6. Auditability & Reproducibility

To guarantee full reproducibility:

- The Python computation engine is **publicly available**
- Step-by-step recalculation instructions are provided
- Historical recalculation examples are documented
- Dedicated analysis and verification scripts are included

---

## 7. Institutional Transparency

- Public version registry  
- Explicit publication of methodological adjustments  
- Full documentation of all assumptions and parameter changes

---

## License & Copyright

© 2025 **GHI – Global HashCost Index**

This document is published under the  
**Creative Commons Attribution – Non Commercial – Share Alike 4.0 International**  
(**CC BY-NC-SA 4.0**) license.
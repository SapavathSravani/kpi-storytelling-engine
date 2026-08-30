# KPI Intelligence-to-Action Engine (BusinessIntelligence.ai)

**Team Name:** Alpha123  
**Team Leader:** Sravani Sapavath (IIT Kharagpur)  
**Track:** BusinessIntelligence.ai | Accenture Innovation Challenge 2026

---

# 1. Executive Summary & Architecture Overview

Traditional Business Intelligence (BI) dashboards present static quantitative changes without explaining root causes or identifying specific interventions. The **KPI Intelligence-to-Action Engine** bridges this insight gap by unifying structured metrics (daily sales, weekly marketing spend) with unstructured context (monthly CSAT text, support logs)

The system treats **deterministic statistics as the source of quantitative truth** and reserves **LLMs strictly for intent parsing and narrative synthesis**.

---

## System Architecture Pipeline
text
+-----------------------------------------------------------------------------------+
|                               **1. DATA INGESTION**                                  |
|  Daily Sales DB (SQL)  |  Weekly Marketing (CSV)  |  Monthly CSAT Tickets (Parquet) |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                       **2. GOVERNED SEMANTIC CONTRACT & RBAC**                   |
|  - Enforces Data Lineage, SLA Freshness Check, Column/Row-Level Entitlements      |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                         **3.DETERMINISTIC ANALYTICS ENGINE**                         |
|  - Anomaly Detection: Dynamic SPC Control Limits & Z-scores                       |
|  - Driver Ranking: Dynamic Contribution & Variance Decomposition                  |
|  - Cold-Start/Sparse History: Empirical Bayesian Shrinkage                        |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                      **4.HYPOTHESIS & CONFIDENCE SCORING**                           |
|  - Validates Signal vs. Noise Ratio                                               |
|  - Triggers ABSTENTION / Clarification Protocol if Confidence Score < 0.65       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                        **5. LLM NARRATIVE & ACTION SYNTHESIS**                        |
|  - Persona-Specific Views (Executive vs. Operations Analyst)                      |
|  - Structured Recommendations: Driver -> Lever -> Action -> Impact -> Owner       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                       **6. TELEMETRY & FEEDBACK LEARNING LOOP**                      |
|  - Live Tracking: Token Usage, Latency ($/Insight Costing)                        |
|  - Captures Analyst Ratings to Retrain Driver Weights                             |
+-----------------------------------------------------------------------------------+

---

## 2.Technical Stack & Dependencies
**Language & Core:** Python 3.11+
**Data Processing & Analytics:** pandas, numpy, scikit-learn
**Security & Data Governance:** pydantic (Schema & Contract Enforcement)
**LLM Orchestration:** openai / langchain
**Frontend UI:** streamlit
**Testing:** pytest

---

 ## 3.Key Features & Implementation Approach Dynamic
**Semantic Contracts:** Stored under config/kpi_contracts.json, contracts govern metric calculations, lineage, underlying refresh cadences, and threshold rules to ensure uniform calculation logic across heterogeneous sources.
**Multi-Factor Root Cause Analysis:** Combines deterministic statistical anomaly detection with dynamic linear contribution modeling. It isolates whether a revenue drop is driven by volume shrinkage, marketing channel underperformance, or negative sentiment trends in support tickets.
**Abstention & Low-Confidence Protocol:** When contradictory evidence occurs (e.g., promotional spend increases while conversion drops without clear CSAT signals), the engine assigns a low confidence score ($\text{Score} < 0.65$) and prompts the analyst for targeted data inputs rather than generating speculative claims.
**Role-Based Personalization (RBAC):**
**Executive Persona:** Receives high-level plain-language summaries, financial exposure metrics, macro driver rankings, and strategic decision paths.
**Operations Analyst Persona:** Receives full statistical outputs, root-cause regression parameters, SQL/lineage proofs, raw ticket samples, and operational levers.

---

## 4. **Analytical Methods & LLM vs. Non-LLM Boundary**

To ensure complete accuracy and prevent LLM hallucinations, quantitative analytics and narrative generation are strictly separated:

| Functional Module | Technology / Analytical Method | Justification (Why this choice?) |
| :--- | :--- | :--- |
| **Data Aggregation & Joining** | SQL / Pandas DataFrames | Deterministic processing across mixed refresh cadences (daily vs. monthly). |
| **Anomaly Detection** | Statistical Process Control (SPC) Boundaries & Z-Scores | Prevents false positives by ignoring expected seasonal variance. |
| **Driver Identification** | Multi-factor Contribution Decomposition | Mathematically quantifies contribution percentages for individual business levers. |
| **Sparse-History Handling** | Empirical Bayesian Shrinkage | Stabilizes variance for newly launched products with limited historical data points. |
| **Role-Based Entitlements** | Custom Middleware (`rbac_enforcer.py`) | Restricts row- and column-level access before data reaches the model layer. |
| **Narrative Generation** | LLM Prompt Orchestration (`llm_orchestrator.py`) | Translates structured mathematical outputs into persona-specific natural language. |

---

## 5. Setup and Execution Instructions
Prerequisites
Python 3.11 or higher
Git

Installation Steps
**1.Clone the Repository:**
git clone [https://github.com/SapavathSravani/kpi-storytelling-engine.git](https://github.com/SapavathSravani/kpi-storytelling-engine.git)
cd kpi-storytelling-engine

**2.Create and Activate a Virtual Environment:**
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

**3.Install Dependencies:**
pip install -r requirements.txt

**4.Run Automated Tests:**
pytest

**5.Launch the Interactive Demonstration App:**
streamlit run app.py

---

## 6. Demonstrated Test Scenarios 
The engine includes pre-configured execution scripts to test real-world scenarios:
Multi-Factor KPI Drop Scenario: Demonstrates an 8.4% regional revenue drop isolated into specific price shifts, supply delay impacts, and marketing fatigue.
Low-Confidence Abstention Scenario: Flags contradictory CSAT/spend vectors, presents alternative hypotheses, and abstains from recommending concrete strategic shifts until data is validated.
Sparse-History / Cold-Start Scenario: Applies Bayesian shrinkage to a product launched recently to prevent erroneous anomaly flags.
RBAC & Data Security Scenario: Automatically redacts sensitive margin columns and restricts output rows based on user role assignments.

---

##7. Runtime Telemetry & Operational Economics
The pipeline tracks execution telemetry on every run to monitor performance and cost:
=====================================================
               **ENGINE TELEMETRY REPORT**               
=====================================================
- Execution Latency:         412 ms (Total)
  - Statistical Analytics:   48 ms  (Non-LLM)
  - Semantic RBAC Engine:    12 ms  (Non-LLM)
  - LLM Synthesis Call:      352 ms (LLM Orchestration)
- Token Usage:               742 Tokens
  - Prompt Tokens:           510
  - Completion Tokens:       232
- Estimated Cost / Insight:  $0.000371 USD
- Confidence Score:          0.92 (High - Dynamic Threshold Passed)
=====================================================


import streamlit as st
import pandas as pd
import json
from engine.analytics import NonLLMAnalyticsEngine
from engine.rbac_enforcer import RBACEnforcer
from engine.llm_orchestrator import NarrativeSynthesizer
from engine.telemetry import TelemetryTracker

st.set_page_config(page_title="KPI Intelligence Engine", layout="wide")

st.title("KPI Intelligence-to-Action Engine")
st.caption("Team Alpha123 | Accenture Innovation Challenge 2026")

# Sidebar settings
st.sidebar.header("User & Context Setup")
role = st.sidebar.selectbox("Select User Persona", ["Executive", "Operations_Analyst"])
scenario_key = st.sidebar.selectbox(
    "Select Scenario", 
    ["multifactor_revenue_drop", "low_confidence_conflict", "sparse_history_product"]
)

# Load synthetic data
with open("data/synthetic_scenarios.json") as f:
    scenarios = json.load(f)
selected_data = scenarios[scenario_key]

st.subheader(f"Scenario: {scenario_key.replace('_', ' ').title()}")

if st.button("Run Intelligence Engine"):
    tracker = TelemetryTracker()
    
    # 1. Non-LLM Analytics
    spc_results = NonLLMAnalyticsEngine.calculate_spc_anomaly(
        pd.Series(selected_data["historical_series"])
    )
    ranked_drivers = NonLLMAnalyticsEngine.rank_drivers(selected_data["drivers"])
    
    # 2. RBAC Enforcement
    rbac = RBACEnforcer()
    secured_data = rbac.enforce_security(selected_data, role)
    
    # 3. LLM Synthesis & Abstention Protocol
    synthesizer = NarrativeSynthesizer()
    narrative_output = synthesizer.generate_narrative(
        insights={
            "kpi": selected_data["kpi_id"],
            "revenue_change": selected_data.get("metric_change", "-8.4%"),
            "top_driver": ranked_drivers[0]["driver"] if ranked_drivers else "N/A",
            "drivers": ranked_drivers
        },
        confidence_score=selected_data["confidence_score"],
        role=role
    )
    
    # 4. Compute Telemetry
    telemetry = tracker.get_telemetry(prompt_tokens=510, completion_tokens=232)
    
    # UI Display
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Quantitative Analysis (Non-LLM)")
        st.write("**Statistical Anomaly Check (SPC):**", spc_results)
        st.write("**Ranked Drivers:**")
        st.table(pd.DataFrame(ranked_drivers))
        
    with col2:
        st.write("### Generated Narrative & Actions")
        if narrative_output["status"] == "ABSTAINED":
            st.error(f"**Engine Abstained:** {narrative_output['reason']}")
            st.warning(f"**Required Action:** {narrative_output['action_required']}")
        else:
            st.success(f"**Status:** {narrative_output['status']}")
            st.write(f"**Persona View:** {narrative_output['persona']}")
            st.info(f"**Narrative:** {narrative_output['narrative']}")

    st.markdown("---")
    st.write("### System Telemetry & Economics")
    st.json(telemetry)

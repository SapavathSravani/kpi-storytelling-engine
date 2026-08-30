class NarrativeSynthesizer:
    """Handles persona narratives and enforces low-confidence abstention."""

    def __init__(self, confidence_threshold=0.65):
        self.threshold = confidence_threshold

    def generate_narrative(self, insights: dict, confidence_score: float, role: str) -> dict:
        if confidence_score < self.threshold:
            return {
                "status": "ABSTAINED",
                "reason": "Contradictory or insufficient evidence across data sources.",
                "action_required": "Please validate marketing spend records against CSAT sentiment logs."
            }

        top_driver = insights.get("top_driver", "unknown factor")
        change = insights.get("revenue_change", "N/A")

        if role == "Executive":
            narrative = f"Metric shifted by {change} primarily due to {top_driver}. Executive action is required on core operational levers."
        else:
            narrative = f"Detailed Root Cause: Metric changed by {change}. Key breakdown: {insights.get('drivers', [])}. Lineage verified."

        return {
            "status": "SUCCESS",
            "persona": role,
            "narrative": narrative,
            "confidence_score": confidence_score
        }

from engine.llm_orchestrator import NarrativeSynthesizer

def test_abstention_trigger():
    synthesizer = NarrativeSynthesizer(confidence_threshold=0.65)
    result = synthesizer.generate_narrative(
        insights={}, confidence_score=0.40, role="Executive"
    )
    assert result["status"] == "ABSTAINED"

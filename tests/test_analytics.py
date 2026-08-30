import pandas as pd
from engine.analytics import NonLLMAnalyticsEngine

def test_spc_anomaly_detection():
    data = pd.Series([10.0, 10.0, 10.0, 10.0, 10.0, 50.0])
    result = NonLLMAnalyticsEngine.calculate_spc_anomaly(data)
    assert result["is_anomaly"] is True

def test_driver_ranking():
    drivers = {"price": -5.0, "volume": -10.0}
    ranked = NonLLMAnalyticsEngine.rank_drivers(drivers)
    assert ranked[0]["driver"] == "volume"

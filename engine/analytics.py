import numpy as np
import pandas as pd

class NonLLMAnalyticsEngine:
    """Handles deterministic math, dynamic control limits, and contribution scoring."""

    @staticmethod
    def calculate_spc_anomaly(series: pd.Series) -> dict:
        """Calculates dynamic statistical process control limits."""
        mean = series.mean()
        std = series.std()
        latest = series.iloc[-1]
        z_score = (latest - mean) / std if std != 0 else 0.0
        
        return {
            "is_anomaly": bool(abs(z_score) > 2.0),
            "z_score": round(float(z_score), 2),
            "control_limits": {
                "upper": round(float(mean + 2*std), 2), 
                "lower": round(float(mean - 2*std), 2)
            }
        }

    @staticmethod
    def rank_drivers(driver_data: dict) -> list:
        """Ranks driver contributions using deterministic variance decomposition."""
        total_delta = sum(abs(v) for v in driver_data.values())
        if total_delta == 0:
            return []
        
        ranked = [
            {"driver": k, "impact": v, "contribution_pct": round((abs(v) / total_delta) * 100, 2)}
            for k, v in driver_data.items()
        ]
        return sorted(ranked, key=lambda x: abs(x["contribution_pct"]), reverse=True)

    @staticmethod
    def apply_bayesian_shrinkage(sparse_series: pd.Series, prior_mean: float) -> float:
        """Stabilizes variance for sparse-history KPIs using Empirical Bayesian Shrinkage."""
        n = len(sparse_series)
        sample_mean = sparse_series.mean() if n > 0 else prior_mean
        weight = n / (n + 10)
        return float(weight * sample_mean + (1 - weight) * prior_mean)

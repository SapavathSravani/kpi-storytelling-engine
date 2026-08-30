import time

class TelemetryTracker:
    """Tracks latency, token usage, and cost per insight execution."""

    def __init__(self):
        self.start_time = time.time()

    def get_telemetry(self, prompt_tokens: int, completion_tokens: int) -> dict:
        latency_ms = round((time.time() - self.start_time) * 1000, 2)
        cost = ((prompt_tokens * 0.00000015) + (completion_tokens * 0.00000060))
        
        return {
            "latency_ms": latency_ms,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
            "estimated_cost_usd": f"${cost:.6f}"
        }

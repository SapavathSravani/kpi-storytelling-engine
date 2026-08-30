import json

class RBACEnforcer:
    """Applies row/column level security before data reaches the model layer."""
    
    def __init__(self, entitlements_path="config/role_entitlements.json"):
        with open(entitlements_path, "r") as f:
            self.rules = json.load(f)["roles"]

    def enforce_security(self, data: dict, role: str) -> dict:
        if role not in self.rules:
            raise PermissionError("Unauthorized role access.")
        
        allowed_cols = self.rules[role]["allowed_columns"]
        filtered_data = {k: v for k, v in data.items() if k in allowed_cols}
        return filtered_data

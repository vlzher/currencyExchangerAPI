def historical_utils(data):
    if not isinstance(data, dict):
        raise TypeError("Input data must be a dictionary.")
    required_keys = {"success", "quotes"}
    missing_keys = required_keys - set(data.keys())
    if missing_keys:
        raise ValueError(f"Missing required key(s) in data: {missing_keys}")
    if not isinstance(data["success"], bool):
        raise TypeError("Key 'success' must be a boolean value.")
    if not isinstance(data["quotes"], dict):
        raise TypeError("Key 'quotes' must be a dictionary.")
    if not data["success"]:
        return {"success": False}
    else:
        return {
            "success": True,
            "data": data["quotes"]
        }

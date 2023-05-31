def change_utils(data):
    if not isinstance(data, dict):
        raise TypeError("Input data must be a dictionary.")
    required_keys = {"change", "quotes"}
    missing_keys = required_keys - set(data.keys())
    if missing_keys:
        raise ValueError(f"Missing required key(s) in data: {missing_keys}")
    if not isinstance(data["change"], bool):
        raise TypeError("Key 'change' must be a boolean value.")
    if not isinstance(data["quotes"], dict):
        raise TypeError("Key 'quotes' must be a dictionary.")
    if not data["change"]:
        return {"success": False}
    else:
        first_key = next(iter(data["quotes"]))
        return {
            "success": True,
            "data": data["quotes"][first_key]
        }

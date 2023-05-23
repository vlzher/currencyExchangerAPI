def list_utils(data):
    if not isinstance(data, dict):
        raise TypeError("Input data must be a dictionary.")
    if "success" not in data or not isinstance(data["success"], bool):
        raise ValueError("Key 'success' must be present and have a boolean value.")
    return data

from datetime import datetime


def timeframe_utils(data):
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
    if not isinstance(data["quotes"], dict):
        raise TypeError("Key 'quotes' must be a dictionary.")
    if not data["success"]:
        return {"success": False}
    else:
        data_return = []
        start_date = datetime.strptime(data['start_date'],
                                                '%Y-%m-%d')

        for i, (date_str, quote) in enumerate(data['quotes'].items()):
            date = datetime.strptime(date_str, '%Y-%m-%d')
            num_days = (date - start_date).days
            currency_pair = list(quote.keys())[0]
            data_return.append({'x': num_days, 'y': quote[currency_pair]})
        return {
            "success": True,
            "data": data_return
        }

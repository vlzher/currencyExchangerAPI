import pytest

from app.routes.utils import change_utils


def test_change_utils_with_valid_data():
    data = {"change": True,
            "quotes": {"USDJPY": {"change": 0.0123, "change_pct": 0.4567, "end_rate": 110.123, "start_rate": 109.876}}}
    result = change_utils(data)
    assert result["success"] == True
    assert result["data"] == data["quotes"]


def test_change_utils_with_invalid_data_type():
    data = "invalid"
    with pytest.raises(TypeError):
        change_utils(data)


def test_change_utils_with_missing_required_keys():
    data = {"quotes": {"USDJPY": {"change": 0.0123, "change_pct": 0.4567, "end_rate": 110.123, "start_rate": 109.876}}}
    with pytest.raises(ValueError) as exc_info:
        change_utils(data)
    assert "Missing required key(s) in data" in str(exc_info.value)


def test_change_utils_with_invalid_change_value():
    data = {"change": "invalid",
            "quotes": {"USDJPY": {"change": 0.0123, "change_pct": 0.4567, "end_rate": 110.123, "start_rate": 109.876}}}
    with pytest.raises(TypeError) as exc_info:
        change_utils(data)
    assert "Key 'change' must be a boolean value" in str(exc_info.value)


def test_change_utils_with_invalid_quotes_value():
    data = {"change": True, "quotes": "invalid"}
    with pytest.raises(TypeError) as exc_info:
        change_utils(data)
    assert "Key 'quotes' must be a dictionary" in str(exc_info.value)


def test_change_utils_with_change_set_to_false():
    data = {"change": False,
            "quotes": {"USDJPY": {"change": 0.0123, "change_pct": 0.4567, "end_rate": 110.123, "start_rate": 109.876}}}
    result = change_utils(data)
    assert result["success"] == False

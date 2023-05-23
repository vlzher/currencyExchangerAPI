import pytest

from app.routes.utils import timeframe_utils


def test_timeframe_utils_valid_data():
    data = {
        "success": True,
        "quotes": {
            "2023-05-23": {
                "USDBYN": 2.518648,
                "USDEUR": 0.919904,
                "USDPLN": 4.316148
            }
        }
    }
    result = timeframe_utils(data)
    assert result == {"success": True, "data": data["quotes"]}


def test_timeframe_utils_invalid_data_type():
    data = "invalid_data"
    with pytest.raises(TypeError):
        timeframe_utils(data)


def test_timeframe_utils_missing_keys():
    data = {
        "quotes": {
            "2023-05-23": {
                "USDBYN": 2.518648,
                "USDEUR": 0.919904,
                "USDPLN": 4.316148
            }
        }
    }
    with pytest.raises(ValueError):
        timeframe_utils(data)


def test_timeframe_utils_invalid_success_value():
    data = {
        "success": "invalid",
        "quotes": {
            "2023-05-23": {
                "USDBYN": 2.518648,
                "USDEUR": 0.919904,
                "USDPLN": 4.316148
            }
        }
    }
    with pytest.raises(TypeError):
        timeframe_utils(data)


def test_timeframe_utils_invalid_quotes_type():
    data = {
        "success": True,
        "quotes": "invalid_quotes"
    }
    with pytest.raises(TypeError):
        timeframe_utils(data)


def test_timeframe_utils_not_success():
    data = {
        "success": False,
        "quotes": {}
    }

    result = timeframe_utils(data)

    assert result == {"success": False}

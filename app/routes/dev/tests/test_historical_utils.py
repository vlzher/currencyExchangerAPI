import pytest

from app.routes.utils import historical_utils


def test_historical_utils_success():
    data = {
        "success": True,
        "quotes": {
            "USDBYN": 2.523211,
            "USDEUR": 0.928462,
            "USDPLN": 4.177944
        }
    }

    result = historical_utils(data)

    assert result == {
        "success": True,
        "data": {
            "USDBYN": 2.523211,
            "USDEUR": 0.928462,
            "USDPLN": 4.177944
        }
    }


def test_historical_utils_missing_key():
    data = {"success": True}

    with pytest.raises(ValueError):
        historical_utils(data)


def test_historical_utils_wrong_type():
    data = {
        "success": "True",
        "quotes": {
            "USDBYN": 2.523211,
            "USDEUR": 0.928462,
            "USDPLN": 4.177944
        }
    }
    with pytest.raises(TypeError):
        historical_utils(data)


def test_historical_utils_not_dict():
    data = "this is not a dictionary"
    with pytest.raises(TypeError):
        historical_utils(data)


def test_historical_utils_not_successful():
    data = {
        "success": False,
        "quotes": {
            "USDBYN": 2.523211,
            "USDEUR": 0.928462,
            "USDPLN": 4.177944
        }
    }
    assert historical_utils(data) == {"success": False}
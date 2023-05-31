import pytest

from app.routes.utils import historical_utils

import pytest


def test_historical_utils_with_empty_data():
    with pytest.raises(ValueError, match="Missing required key"):
        historical_utils({})


def test_historical_utils_with_missing_success_key():
    with pytest.raises(ValueError, match="Missing required key"):
        historical_utils({"quotes": {}})


def test_historical_utils_with_missing_quotes_key():
    with pytest.raises(ValueError, match="Missing required key"):
        historical_utils({"success": True})


def test_historical_utils_with_non_dict_data():
    with pytest.raises(TypeError, match="Input data must be a dictionary"):
        historical_utils("not a dict")


def test_historical_utils_with_non_boolean_success_key():
    with pytest.raises(TypeError, match="Key 'success' must be a boolean value"):
        historical_utils({"success": 0, "quotes": {}})


def test_historical_utils_with_non_dict_quotes_key():
    with pytest.raises(TypeError, match="Key 'quotes' must be a dictionary"):
        historical_utils({"success": True, "quotes": "not a dict"})


def test_historical_utils_with_success_false():
    assert historical_utils({"success": False, "quotes": {}}) == {"success": False}


def test_historical_utils_with_success_true_and_empty_quotes():
    result = historical_utils({"success": True, "quotes": {}})
    assert result["success"] == True
    assert result["data"] == {}


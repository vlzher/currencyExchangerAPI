import pytest

from app.routes.utils import change_utils

import pytest


def test_change_utils_with_empty_data():
    with pytest.raises(ValueError, match="Missing required key"):
        change_utils({})


def test_change_utils_with_missing_change_key():
    with pytest.raises(ValueError, match="Missing required key"):
        change_utils({"quotes": {}})


def test_change_utils_with_missing_quotes_key():
    with pytest.raises(ValueError, match="Missing required key"):
        change_utils({"change": True})


def test_change_utils_with_non_dict_data():
    with pytest.raises(TypeError, match="Input data must be a dictionary"):
        change_utils("not a dict")


def test_change_utils_with_non_boolean_change_key():
    with pytest.raises(TypeError, match="Key 'change' must be a boolean value"):
        change_utils({"change": 0, "quotes": {}})


def test_change_utils_with_non_dict_quotes_key():
    with pytest.raises(TypeError, match="Key 'quotes' must be a dictionary"):
        change_utils({"change": True, "quotes": "not a dict"})


def test_change_utils_with_change_false():
    assert change_utils({"change": False, "quotes": {}}) == {"success": False}


def test_change_utils_with_change_true_and_empty_quotes():
    with pytest.raises(StopIteration):
        change_utils({"change": True, "quotes": {}})


def test_change_utils_with_change_true_and_nonempty_quotes():
    result = change_utils({"change": True, "quotes": {"USDJPY": 110.0, "EURUSD": 1.2}})
    assert result["success"] == True
    assert result["data"] == 110.0

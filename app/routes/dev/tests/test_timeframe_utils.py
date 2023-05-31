import pytest

from app.routes.utils import timeframe_utils

import pytest
from datetime import datetime


def test_timeframe_utils_with_empty_data():
    with pytest.raises(ValueError, match="Missing required key"):
        timeframe_utils({})


def test_timeframe_utils_with_missing_success_key():
    with pytest.raises(ValueError, match="Missing required key"):
        timeframe_utils({"quotes": {}, "start_date": "2023-01-01"})


def test_timeframe_utils_with_missing_quotes_key():
    with pytest.raises(ValueError, match="Missing required key"):
        timeframe_utils({"success": True, "start_date": "2023-01-01"})


def test_timeframe_utils_with_missing_start_date_key():
    with pytest.raises(KeyError, match="'start_date'"):
        timeframe_utils({"success": True, "quotes": {}})


def test_timeframe_utils_with_non_dict_data():
    with pytest.raises(TypeError, match="Input data must be a dictionary"):
        timeframe_utils("not a dict")


def test_timeframe_utils_with_non_boolean_success_key():
    with pytest.raises(TypeError, match="Key 'success' must be a boolean value"):
        timeframe_utils({"success": 0, "quotes": {}, "start_date": "2023-01-01"})


def test_timeframe_utils_with_non_dict_quotes_key():
    with pytest.raises(TypeError, match="Key 'quotes' must be a dictionary"):
        timeframe_utils({"success": True, "quotes": "not a dict", "start_date": "2023-01-01"})


def test_timeframe_utils_with_invalid_start_date():
    with pytest.raises(ValueError, match="time data 'not a date' does not match format"):
        timeframe_utils({"success": True, "quotes": {}, "start_date": "not a date"})


def test_timeframe_utils_with_success_false():
    assert timeframe_utils({"success": False, "quotes": {}, "start_date": "2023-01-01"}) == {"success": False}


def test_timeframe_utils_with_valid_data():
    input_data = {
        "success": True,
        "quotes": {
            "2023-01-01": {"USDJPY": 110.0},
            "2023-01-02": {"USDJPY": 111.0},
            "2023-01-03": {"USDJPY": 112.0}
        },
        "start_date": "2023-01-01"
    }
    expected_output = {
        "success": True,
        "data": [
            {"x": 0, "y": 110.0},
            {"x": 1, "y": 111.0},
            {"x": 2, "y": 112.0}
        ]
    }
    assert timeframe_utils(input_data) == expected_output

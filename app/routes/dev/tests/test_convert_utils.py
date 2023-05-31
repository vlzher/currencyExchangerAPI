import pytest

from app.routes.utils import convert_utils

import pytest


def test_convert_utils_with_empty_data():
    with pytest.raises(ValueError, match="Missing required key"):
        convert_utils({})


def test_convert_utils_with_missing_success_key():
    with pytest.raises(ValueError, match="Missing required key"):
        convert_utils({"result": 100.0})


def test_convert_utils_with_missing_result_key():
    with pytest.raises(ValueError, match="Missing required key"):
        convert_utils({"success": True})


def test_convert_utils_with_non_dict_data():
    with pytest.raises(TypeError, match="Input data must be a dictionary"):
        convert_utils("not a dict")


def test_convert_utils_with_non_boolean_success_key():
    with pytest.raises(TypeError, match="Key 'success' must be a boolean value"):
        convert_utils({"success": "true", "result": 100.0})


def test_convert_utils_with_non_numeric_result_key():
    with pytest.raises(TypeError, match="Key 'result' must be a float or integer value"):
        convert_utils({"success": True, "result": "100.0"})


def test_convert_utils_with_success_true_and_float_result():
    result = convert_utils({"success": True, "result": 123.45})
    assert result["success"] == True
    assert result["result"] == 123.45


def test_convert_utils_with_success_true_and_int_result():
    result = convert_utils({"success": True, "result": 100})
    assert result["success"] == True
    assert result["result"] == 100

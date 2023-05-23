import pytest

from app.routes.utils import convert_utils


def test_convert_utils_with_valid_data():
    data = {"success": True, "result": 20.0}
    result = convert_utils(data)
    assert result["success"] == True
    assert result["result"] == 20.0


def test_convert_utils_with_invalid_data_type():
    data = "invalid"
    with pytest.raises(TypeError):
        convert_utils(data)


def test_convert_utils_with_missing_required_keys():
    data = {"success": True}
    with pytest.raises(ValueError) as exc_info:
        convert_utils(data)
    assert "Missing required key(s) in data" in str(exc_info.value)


def test_convert_utils_with_invalid_success_value():
    data = {"success": "invalid", "result": 20.0}
    with pytest.raises(TypeError) as exc_info:
        convert_utils(data)
    assert "Key 'success' must be a boolean value" in str(exc_info.value)


def test_convert_utils_with_invalid_result_value():
    data = {"success": True, "result": "invalid"}
    with pytest.raises(TypeError) as exc_info:
        convert_utils(data)
    assert "Key 'result' must be a float or integer value" in str(exc_info.value)


def test_convert_utils_with_success_set_to_false():
    data = {"success": False, "result": 20.0}
    result = convert_utils(data)
    assert result["success"] == False

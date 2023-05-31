from app.routes.utils import list_utils

import pytest


def test_list_utils_with_empty_data():
    with pytest.raises(TypeError, match="Input data must be a dictionary"):
        list_utils([])


def test_list_utils_with_missing_success_key():
    with pytest.raises(ValueError, match="Key 'success' must be present"):
        list_utils({"result": 100.0})


def test_list_utils_with_non_bool_success_key():
    with pytest.raises(ValueError, match="Key 'success' must be present and have a boolean value"):
        list_utils({"success": "true"})


def test_list_utils_with_valid_data():
    assert list_utils({"success": True}) == {"success": True}


def test_list_utils_with_other_keys():
    assert list_utils({"success": False, "other_key": 123}) == {"success": False, "other_key": 123}

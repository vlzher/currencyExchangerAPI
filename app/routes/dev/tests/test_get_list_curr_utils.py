import pytest

from app.routes.utils import list_utils


def test_list_utils_with_valid_data():
    data = {
        "currencies": {
            "AED": "United Arab Emirates Dirham",
            "AFN": "Afghan Afghani",
            "ALL": "Albanian Lek",
            "AMD": "Armenian Dram",
            "BOB": "Bolivian Boliviano",
            "BRL": "Brazilian Real",
            "BSD": "Bahamian Dollar",
            "BTC": "Bitcoin",
            "BTN": "Bhutanese Ngultrum",
            "BWP": "Botswanan Pula",
            "BYN": "New Belarusian Ruble",
            "BYR": "Belarusian Ruble",
            "BZD": "Belize Dollar",
            "CAD": "Canadian Dollar",
            "ZAR": "South African Rand",
            "ZMK": "Zambian Kwacha (pre-2013)",
            "ZMW": "Zambian Kwacha",
            "ZWL": "Zimbabwean Dollar"
        },
        "success": True
    }

    assert list_utils(data) == data


def test_list_utils_with_invalid_type_data():
    data = ["AED", "AFN", "ALL"]

    with pytest.raises(TypeError) as exc_info:
        list_utils(data)

    assert str(exc_info.value) == "Input data must be a dictionary."


def test_list_utils_with_missing_success_key_data():
    data = {
        "currencies": {
            "AED": "United Arab Emirates Dirham",
            "AFN": "Afghan Afghani",
            "ALL": "Albanian Lek"
        }
    }

    with pytest.raises(ValueError) as exc_info:
        list_utils(data)

    assert str(exc_info.value) == "Key 'success' must be present and have a boolean value."


def test_list_utils_with_invalid_success_value_data():
    data = {
        "currencies": {
            "AED": "United Arab Emirates Dirham",
            "AFN": "Afghan Afghani",
            "ALL": "Albanian Lek"
        },
        "success": "true"
    }

    with pytest.raises(ValueError) as exc_info:
        list_utils(data)

    assert str(exc_info.value) == "Key 'success' must be present and have a boolean value."

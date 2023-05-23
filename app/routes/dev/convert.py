from app.routes.dev.mocks.convert import convert_mock
from app.routes.utils import convert_utils


def convert(amount, from_currency, to_currency, date):
    data = convert_utils(convert_mock)
    return data

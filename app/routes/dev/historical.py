from app.routes.dev.mocks.historical import historical_mock
from app.routes.utils import historical_utils


def historical(date, currencies, source):
    data = historical_utils(historical_mock)
    return data

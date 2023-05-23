from app.routes.dev.mocks.timeframe import timeframe_mock
from app.routes.utils import timeframe_utils


def timeframe(end_date, start_date, currencies, source):
    data = timeframe_utils(timeframe_mock)
    return data

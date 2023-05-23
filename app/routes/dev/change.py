from app.routes.dev.mocks.change import change_mock
from app.routes.utils import change_utils


def change(end_date, start_date, currencies, source):
    data = change_utils(change_mock)
    return data

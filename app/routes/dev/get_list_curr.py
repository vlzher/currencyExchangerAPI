from app.routes.dev.mocks.get_list_curr import list_curr_mock
from app.routes.utils import list_utils


def get_list_curr():
    data = list_utils(list_curr_mock)
    return data

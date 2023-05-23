import os
from flask import request, Blueprint
from dotenv import load_dotenv

routes_bp = Blueprint('routes', __name__)
load_dotenv()
if os.environ.get('ENV') == 'dev':
    from app.routes.dev import change
    from app.routes.dev import convert
    from app.routes.dev import historical
    from app.routes.dev import get_list_curr
    from app.routes.dev import timeframe
else:
    from app.routes.prod import change
    from app.routes.prod import convert
    from app.routes.prod import historical
    from app.routes.prod import get_list_curr
    from app.routes.prod import timeframe


@routes_bp.route('/change')
def get_change():
    end_date = request.args.get('end_date')
    start_date = request.args.get('start_date')
    currencies = request.args.get('currencies')
    source = request.args.get('source')
    return change(end_date, start_date, currencies, source)


@routes_bp.route('/convert')
def get_convert():
    amount = request.args.get('amount')
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    date = request.args.get('date')

    return convert(amount, from_currency, to_currency, date)


@routes_bp.route('/historical')
def get_historical():
    date = request.args.get('date')
    currencies = request.args.get('currencies')
    source = request.args.get('source')

    return historical(date, currencies, source)


@routes_bp.route('/list')
def get_list():
    return get_list_curr()


@routes_bp.route('/timeframe')
def get_timeframe():
    end_date = request.args.get('end_date')
    start_date = request.args.get('start_date')
    currencies = request.args.get('currencies')
    source = request.args.get('source')

    return timeframe(end_date, start_date, currencies, source)

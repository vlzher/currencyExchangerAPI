import requests
import os
from dotenv import load_dotenv
from flask import jsonify

from app.routes.utils import timeframe_utils

load_dotenv()
API_KEY = os.environ.get('API_KEY')
BASE_URL = os.environ.get('BASE_URL')


def timeframe(end_date, start_date, currencies, source):
    headers = {'apikey': API_KEY}
    url = f'{BASE_URL}/timeframe?end_date={end_date}&start_date={start_date}'
    if currencies:
        url += f'&currencies={currencies}'
    if source:
        url += f'&source={source}'

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = timeframe_utils(response.json())
            return jsonify(data)
        else:
            return {"success": False,
                    "message": "Error retrieving data from external API",
                    "status_code": response.status_code}
    except Exception as e:
        print(f"An exception occurred: {e}")
        return {"success": False,
                "message": "Internal server error",
                "status_code": 500}

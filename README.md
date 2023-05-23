# Currency Exchanger API

This is a Python-based API for currency exchange using the currencylayer API. 

## How to Start the App
add .env file with fields:
1) API_KEY={ you can pick from https://apilayer.com/marketplace/currency_data-api }
2) BASE_URL=https://api.apilayer.com/currency_data
3) ENV={"prod","dev"}

To start the app, run: 

```python
python main.py
```

To test the API, run: 

```python
pytest
```

## Endpoints 

### Change Endpoint

The `change` endpoint allows you to retrieve exchange rates for a given time period.

#### Parameters:

- `end_date` (required): The end date of your preferred timeframe.
  - Location: Query, Data Type: string

- `start_date` (required): The start date of your preferred timeframe.
  - Location: Query, Data Type: string

- `currencies` (optional): Enter a list of comma-separated currency codes to limit output currencies.
  - Location: Query, Data Type: string

- `source` (optional): Enter the three-letter currency code of your preferred source currency.
  - Location: Query, Data Type: string


### Convert Endpoint

The `convert` endpoint allows you to perform a single currency conversion.

#### Parameters:

- `amount` (required): The amount to be converted.
  - Location: Query, Data Type: string

- `from` (required): The three-letter currency code of the currency you would like to convert from.
  - Location: Query, Data Type: string

- `to` (required): The three-letter currency code of the currency you would like to convert to.
  - Location: Query, Data Type: string

- `date` (optional): Specify a date (format YYYY-MM-DD) to use historical rates for this conversion.
  - Location: Query, Data Type: string
  
### Historical Endpoint

The `historical` endpoint provides historical exchange rate data for every past day all the way back to the year of 1999.

#### Parameters:

- `date` (required): Specify a date for which to request historical rates. (Format: YYYY-MM-DD)
  - Location: Query, Data Type: string

- `currencies` (optional): Specify a comma-separated list of currency codes to limit your API response to specific currencies.
  - Location: Query, Data Type: string

- `source` (optional): Specify a source currency.
  - Location: Query, Data Type: string

### List Endpoint

The `list` endpoint provides a full list of supported currencies in JSON format.


### Timeframe Endpoint

The `timeframe` endpoint allows you to query the API for daily historical rates between two dates of your choice, with a maximum time frame of 365 days.

#### Parameters:

- `end_date` (required): The end date of your preferred timeframe.
  - Location: Query, Data Type: string

- `start_date` (required): The start date of your preferred timeframe.
  - Location: Query, Data Type: string

- `currencies` (optional): Enter a list of comma-separated currency codes to limit output currencies.
  - Location: Query, Data Type: string

- `source` (optional): Enter the three-letter currency code of your preferred source currency.
  - Location: Query, Data Type: string
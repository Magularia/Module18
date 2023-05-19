# import requests
#
# api_key = '5a247dcc5a084d859a90263222712e76'
# url = 'https://openexchangerates.org/api/latest.json'
#
# def convert_currency(amount, from_currency, to_currency):
#     response = requests.get(url, params={'app_id':api_key})
#     exchange_rates = response.json()['rates']
#     if from_currency != 'USD':
#         amount_in_usd = amount / exchange_rates[from_currency]
#     else:
#         amount_in_usd = amount
#     if to_currency != 'USD':
#         converted_amount = amount_in_usd * exchange_rates[to_currency]
#     else:
#         converted_amount = amount_in_usd
#     return converted_amount
#
# print(convert_currency(1, 'USD', 'EUR')) # конвертирует 1 доллар в рубли

from django.shortcuts import render
import requests
import os
import datetime
# from requests.auth import HTTPBasicAuth
from team.models import ExchangeRate, Currency


def external_connection(request):
    method = 'get'
    current_date = datetime.date.today()
    url = f'https://api.exchangeratesapi.io/v1/{current_date}'
    api_key = os.getenv('API_KEY')
    call = requests.request(method, url, headers=None, auth=api_key)
    data = call.json()
    rates = data['rates']

    list_of_currency = Currency.currency_shortcut.all()

    # for i in rates:
    #     rates_data = ExchangeRate(
    #         exchange_rate = i[]
    #     )

    for i in list_of_currency:
        currency_id = Currency.currency_shortcut.get(name=i)
        current = ExchangeRate.objects.get(currency=currency_id)
        current.exchange_rate = rates[i]
        current.save()

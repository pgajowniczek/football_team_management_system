from django.shortcuts import render
import requests
import os
import datetime
# from requests.auth import HTTPBasicAuth
from team.models import ExchangeRate, Currency


def external_connection(request):
    method = 'get'
    current_date = datetime.date.today()
    api_key = os.getenv('API_KEY')
    url = f'http://api.exchangeratesapi.io/v1/{current_date}?access_key={api_key}'
    response = requests.request(method, url, headers=None)
    if response.ok:
        data = response.json()
        rates = data['rates']
    else:
        return print('Błąd API')

    # list_of_currency = Currency.currency_shortcut.all()
    # currencies = Currency.objects.all()

    # select * from Currency where currency_shortcut = i

    for i in rates:
        x = Currency.objects.filter(currency_shortcut=i).first()
        if x:
            # currency_id = Currency.currency_shortcut.get(currency_id=i)

            ExchangeRate.objects.update_or_create(currency=x,
                                                  defaults={'exchange_rate': rates[i]})

# for i in rates:
#     rates_data = ExchangeRate(
#         exchange_rate = i[]
#     )

# for i in list_of_currency:
#     currency_id = Currency.currency_shortcut.get(name=i)
#     current = ExchangeRate.objects.get(currency=currency_id)
#     current.exchange_rate = rates[i]
#     current.save()

# iterowac po ratach z API - dla kazdego rata sprawdzic czy istnieje currency, jezeli nie to idz dalej a jezeli tak to zrob create or update z danym currency
# api endpoint do robienia calla
# django rest framework post

# polaczenie z api
# class exchangeratesapi:
# w init jest klucz api (klucz w env)
# metoda get exchangerates


from django.shortcuts import render
import requests
import os
import datetime
# from requests.auth import HTTPBasicAuth
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from team.models import ExchangeRate, Currency


class ExchangeRatesApi:
    def __init__(self):
        self.method = 'get'
        self.current_date = datetime.date.today()
        self.api_key = os.getenv('API_KEY')
        self.url = f'http://api.exchangeratesapi.io/v234563456/{self.current_date}?access_key={self.api_key}'

    def request(self):
        response = requests.request(self.method, self.url, headers=None)
        print(response.json())

        if response.ok:
            data = response.json()
            rates = data['rates']
        else:
            raise APIException({'message': response})
        self.populate_exchange_rates(rates)
        return rates

    @staticmethod
    def populate_exchange_rates(rates):
        list_of_currency = Currency.currency_shortcut.all()
        for i in rates:
            if i in list_of_currency:
                currency_id = Currency.currency_shortcut.get(currency_id=i)
                ExchangeRate.objects.update_or_create(currency=currency_id, exchange_rate=rates[i],
                                                      defaults={'exchange_rate': 'rates[i]'})
            continue


@api_view(['POST'])
def external_connection(request):
    client = ExchangeRatesApi()
    client.request()

    return Response({'message': "Success"})
# , 'response': rates

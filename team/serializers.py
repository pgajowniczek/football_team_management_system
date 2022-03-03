from rest_framework import serializers
from . import models


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Club
        fields = ('id', 'name', 'founded', 'league')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = ('id', 'name', 'surname', 'shirt_number', 'team', 'email')


class WageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wage
        fields = ('id', 'wage', 'currency', 'start', 'end', 'player')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = ('id', 'full_name', 'currency_shortcut')


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExchangeRate
        fields = ('id', 'name', 'exchange_rate', 'currency')


class InjurySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Injury
        fields = ('id', 'start_date', 'end_date', 'description', 'main_doctor')

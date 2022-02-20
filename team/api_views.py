from rest_framework import viewsets
from . import models
from . import serializers


class ClubViewset(viewsets.ModelViewSet):
    queryset = models.Club.objects.all()
    serializer_class = serializers.ClubSerializer


class PlayerViewset(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class WageViewset(viewsets.ModelViewSet):
    queryset = models.Wage.objects.all()
    serializer_class = serializers.WageSerializer


class CurrencyViewset(viewsets.ModelViewSet):
    queryset = models.Currency.objects.all()
    serializer_class = serializers.CurrencySerializer


class ExchangeRateViewset(viewsets.ModelViewSet):
    queryset = models.ExchangeRate.objects.all()
    serializer_class = serializers.ExchangeRateSerializer


class InjuryViewset(viewsets.ModelViewSet):
    queryset = models.Injury.objects.all()
    serializer_class = serializers.InjurySerializer

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

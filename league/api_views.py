from rest_framework import viewsets
from . import models
from . import serializers


class RefereeFunctionViewset(viewsets.ModelViewSet):
    queryset = models.RefereeFunction.objects.all()
    serializer_class = serializers.RefereeFunctionSerializer


class RefereeViewset(viewsets.ModelViewSet):
    queryset = models.Referee.objects.all()
    serializer_class = serializers.RefereeSerializer


class StadiumViewset(viewsets.ModelViewSet):
    queryset = models.Stadium.objects.all()
    serializer_class = serializers.StadiumSerializer


class GameViewset(viewsets.ModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class ActionViewset(viewsets.ModelViewSet):
    queryset = models.Action.objects.all()
    serializer_class = serializers.ActionSerializer


class CourseOfTheGameViewset(viewsets.ModelViewSet):
    queryset = models.CourseOfTheGame.objects.all()
    serializer_class = serializers.CourseOfTheGameSerializer

from rest_framework import serializers
from . import models


class RefereeFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RefereeFunction
        fields = ('id', 'name')


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Referee
        fields = ('id', 'name', 'surname', 'function')


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stadium
        fields = ('id', 'name', 'capacity', 'address')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ('id', 'home', 'away', 'stadium', 'referee')


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Action
        fields = ('id', 'name')


class CourseOfTheGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseOfTheGame
        fields = ('id', 'minute', 'what_happened', 'player')

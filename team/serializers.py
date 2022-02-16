from rest_framework import serializers
from . import models


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Club
        fields = ('id', 'name', 'founded')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = ('id', 'name', 'surname', 'shirt_number', 'team')


class WageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wage
        fields = ('id', 'wage', 'currency', 'start', 'end', 'player')
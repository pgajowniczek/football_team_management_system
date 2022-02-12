from rest_framework import serializers
from team.models import Player, Wage

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'name', 'surname', 'shirt_number', 'team']
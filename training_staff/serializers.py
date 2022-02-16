from rest_framework import serializers
from . import models


class StaffFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StaffFunction
        fields = ('id', 'name')


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = ('id', 'name', 'surname', 'function', 'club')

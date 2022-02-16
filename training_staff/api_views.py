from rest_framework import viewsets
from . import models
from . import serializers


class StaffFunctionViewset(viewsets.ModelViewSet):
    queryset = models.StaffFunction.objects.all()
    serializer_class = serializers.StaffFunctionSerializer


class StaffViewset(viewsets.ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer

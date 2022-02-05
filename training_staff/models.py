from django.db import models


# Create your models here.

# staff function (coach, physiotherapist, etc.):
class StaffFunction(models.Model):
    name = models.CharField(max_length=100)


class Staff(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    function = models.ForeignKey(StaffFunction, on_delete=models.CASCADE)

from django.db import models


# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    shirt_number = models.IntegerField()
    team = models.CharField(max_length=100)


class Wage(models.Model):
    wage = models.DecimalField(max_digits=9, decimal_places=2)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)

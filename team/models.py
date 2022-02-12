from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()


class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    shirt_number = models.IntegerField()
    team = models.ForeignKey(Club, on_delete=models.CASCADE)
    # najpierw usunąc cale pole - zrobic makemigrations i pozniej dodac nowe pole z foreign key i nowa klasa team


class Wage(models.Model):
    wage = models.DecimalField(max_digits=9, decimal_places=2)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

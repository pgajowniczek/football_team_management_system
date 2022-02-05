from django.db import models
from team.models import Player


class Game(models.Model):
    home = models.CharField(max_length=100)
    away = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    referee = models.CharField(max_length=100)


# what happened on the pitch (goal, foul, etc.):
class Action(models.Model):
    name = models.CharField(max_length=100)


class CourseOfTheGame(models.Model):
    minute = models.IntegerField()
    what_happened = models.ForeignKey(Action, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

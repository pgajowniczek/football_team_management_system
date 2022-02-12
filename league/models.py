from django.db import models
from team.models import Player, Club


# ref function (main, fourth official, linesman)
class RefereeFunction(models.Model):
    name = models.CharField(max_length=100)


class Referee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    function = models.ForeignKey(RefereeFunction, on_delete=models.CASCADE)


class Stadium(models.Model):
    name = models.CharField(max_length=150)
    capacity = models.IntegerField()
    address = models.CharField(max_length=250)


class Game(models.Model):
    home = models.ForeignKey(Club, related_name='home_team', on_delete=models.CASCADE)
    away = models.ForeignKey(Club, related_name='away_team', on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)


# what happened on the pitch (goal, foul, etc.):
class Action(models.Model):
    name = models.CharField(max_length=100)


class CourseOfTheGame(models.Model):
    minute = models.IntegerField()
    what_happened = models.ForeignKey(Action, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

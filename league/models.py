from django.db import models
from team.models import Player, Club


# ref function (main, fourth official, linesman)
class RefereeFunction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Referee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    function = models.ForeignKey(RefereeFunction, on_delete=models.CASCADE)

    def __str__(self):
        pass
    # return f"self.surname


class Stadium(models.Model):
    name = models.CharField(max_length=150)
    capacity = models.IntegerField()
    street = models.CharField(max_length=250)
    post_code = models.CharField(max_length=6)
    number = models.CharField(max_length=5)
    city = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Game(models.Model):
    home = models.ForeignKey(Club, related_name='home_team', on_delete=models.CASCADE)
    away = models.ForeignKey(Club, related_name='away_team', on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)


# what happened on the pitch (goal, foul, etc.):
class Action(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        self.name = self.name
        return self.name


class CourseOfTheGame(models.Model):
    minute = models.IntegerField()
    what_happened = models.ForeignKey(Action, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # game as foreign key
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


# new class liga
class League(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', height_field=None, width_field=None)

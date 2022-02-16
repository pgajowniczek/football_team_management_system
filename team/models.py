from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()
    #logo

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    shirt_number = models.IntegerField()
    team = models.ForeignKey(Club, on_delete=models.CASCADE)
    # najpierw usunąc cale pole - zrobic makemigrations i pozniej dodac nowe pole z foreign key i nowa klasa team

    def __str__(self):
        return self.surname


class Wage(models.Model):
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=100)  #lista wyborow - klucz obcy nowej klasy currency
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    #nowa klasa kurs walut (nazwe waluty, kurs) klucz obcy do nowej klasy currency

    #nowa klasa currency (definicja walut, kolumny: nazwa, pelna nazwa, skrot(zl itp)

    #nowa klasa kontuzja


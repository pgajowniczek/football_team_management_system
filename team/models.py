from django.db import models
#from league.models import League
from training_staff.models import Staff


class Club(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()
    league = models.ForeignKey('league.League', on_delete=models.CASCADE)

    # logo

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    shirt_number = models.IntegerField()
    team = models.ForeignKey(Club, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.surname


# nowa klasa currency (definicja walut, kolumny: nazwa, pelna nazwa, skrot(zl itp)
class Currency(models.Model):
    full_name = models.CharField(max_length=100)
    currency_shortcut = models.CharField(max_length=100)


# nowa klasa kurs walut (nazwe waluty, kurs) klucz obcy do nowej klasy currency
class ExchangeRate(models.Model):
    name = models.DecimalField(max_digits=10, decimal_places=2)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class Wage(models.Model):
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # lista wyborow - klucz obcy nowej klasy currency
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)


class Injury(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    main_doctor = models.ForeignKey(Staff, on_delete=models.CASCADE)

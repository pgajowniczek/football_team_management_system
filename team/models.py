from django.db import models
# from league.models import League
from training_staff.models import Staff
from django.core.mail import EmailMessage
from django.template.loader import get_template
from football_team_management_system.settings import EMAIL_HOST_USER


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
        self.surname = self.surname
        return self.surname


# nowa klasa currency (definicja walut, kolumny: nazwa, pelna nazwa, skrot(zl itp)
class Currency(models.Model):
    full_name = models.CharField(max_length=100)
    currency_shortcut = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


# nowa klasa kurs walut (nazwe waluty, kurs) klucz obcy do nowej klasy currency
class ExchangeRate(models.Model):
    exchange_rate = models.DecimalField(max_digits=7, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class Wage(models.Model):
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # lista wyborow - klucz obcy nowej klasy currency
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    # metoda - wyslij email o platnosci
    def send_email(self):
        html_tpl_path = 'templates/email.html'
        context_data = {'object': self}
        email_html_template = get_template(html_tpl_path).render(context_data)
        receiver_email = self.player
        email_msg = EmailMessage('Test', email_html_template, EMAIL_HOST_USER, [receiver_email],
                                 reply_to=[EMAIL_HOST_USER])
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)


class Injury(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    main_doctor = models.ForeignKey(Staff, on_delete=models.CASCADE)

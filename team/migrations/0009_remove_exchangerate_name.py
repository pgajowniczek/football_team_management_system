# Generated by Django 4.0.2 on 2022-03-03 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_currency_club_league_player_email_injury_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchangerate',
            name='name',
        ),
    ]

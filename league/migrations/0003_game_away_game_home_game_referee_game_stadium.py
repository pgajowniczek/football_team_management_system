# Generated by Django 4.0.2 on 2022-02-12 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_player_name_player_shirt_number_player_surname_and_more'),
        ('league', '0002_referee_stadium_remove_game_away_remove_game_home_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='away',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='team.club'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='home',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='team.club'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='referee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='league.referee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='stadium',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='league.stadium'),
            preserve_default=False,
        ),
    ]

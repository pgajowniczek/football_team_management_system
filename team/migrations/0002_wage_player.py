# Generated by Django 4.0.2 on 2022-02-08 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wage',
            name='player',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='team.player'),
            preserve_default=False,
        ),
    ]

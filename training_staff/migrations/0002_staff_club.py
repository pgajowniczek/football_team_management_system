# Generated by Django 4.0.2 on 2022-02-12 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_wage_currency_alter_wage_wage'),
        ('training_staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='club',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='team.club'),
            preserve_default=False,
        ),
    ]
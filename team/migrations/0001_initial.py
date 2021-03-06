# Generated by Django 4.0.2 on 2022-02-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('shirt_number', models.IntegerField()),
                ('team', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wage', models.DecimalField(decimal_places=2, max_digits=9)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
            ],
        ),
    ]

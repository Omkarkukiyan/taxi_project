# Generated by Django 3.0.5 on 2020-04-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driversalltrips',
            name='rider_first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='driversalltrips',
            name='rider_last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

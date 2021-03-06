# Generated by Django 3.1.5 on 2021-02-18 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0087_remove_low_cardinality_indexes_from_observation_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='station_alt',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='station_antennas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='station_lat',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)]),
        ),
        migrations.AlterField(
            model_name='observation',
            name='station_lng',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)]),
        ),
    ]

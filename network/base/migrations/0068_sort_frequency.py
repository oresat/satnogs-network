# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-22 02:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0067_fix_station_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frequencyrange',
            options={'ordering': ['min_frequency']},
        ),
    ]
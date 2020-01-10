# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 01:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_auto_20160320_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='vetted_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='vetted_status',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('verified', 'Verified'), ('data_not_verified', 'Has Data, Not Verified'), ('no_data', 'No Data')], default='unknown', max_length=10),
        ),
        migrations.AddField(
            model_name='data',
            name='vetted_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vetted_user_set', to=settings.AUTH_USER_MODEL),
        ),
    ]

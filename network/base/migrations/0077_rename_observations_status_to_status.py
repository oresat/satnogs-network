# Generated by Django 2.2.14 on 2020-07-26 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0076_add_waterfalls_vetted_related_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observation',
            old_name='observation_status',
            new_name='status',
        ),
    ]

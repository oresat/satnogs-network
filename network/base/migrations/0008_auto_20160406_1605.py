# Generated by Django 1.9.5 on 2016-04-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_data_payload_demode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

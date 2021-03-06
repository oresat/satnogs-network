# Generated by Django 1.11.11 on 2018-08-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_auto_20180817_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antenna',
            name='antenna_type',
            field=models.CharField(choices=[('dipole', 'Dipole'), ('v-dipole', 'V-Dipole'), ('discone', 'Discone'), ('ground', 'Ground Plane'), ('yagi', 'Yagi'), ('helical', 'Helical'), ('parabolic', 'Parabolic'), ('vertical', 'Verical'), ('turnstile', 'Turnstile'), ('quadrafilar', 'Quadrafilar'), ('eggbeater', 'Eggbeater'), ('lindenblad', 'Lindenblad'), ('paralindy', 'Parasitic Lindenblad')], max_length=15),
        ),
    ]

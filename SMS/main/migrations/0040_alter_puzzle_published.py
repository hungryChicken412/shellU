# Generated by Django 3.2.4 on 2021-08-19 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_alter_puzzle_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 14, 53, 6, 125959), verbose_name='date published'),
        ),
    ]

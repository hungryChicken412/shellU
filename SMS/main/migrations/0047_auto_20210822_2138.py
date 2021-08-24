# Generated by Django 3.2.4 on 2021-08-22 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20210819_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='puzzleDesiredOutput',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 22, 21, 38, 9, 62713), verbose_name='date published'),
        ),
    ]
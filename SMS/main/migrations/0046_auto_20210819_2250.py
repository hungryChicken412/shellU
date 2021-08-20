# Generated by Django 3.2.4 on 2021-08-19 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20210819_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='xps',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 22, 50, 49, 806865), verbose_name='date published'),
        ),
    ]

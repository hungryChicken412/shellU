# Generated by Django 3.2.4 on 2021-06-07 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20210607_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='topics',
        ),
        migrations.AlterField(
            model_name='course',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 22, 50, 6, 662523), verbose_name='date published'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-08-22 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20210822_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 22, 21, 39, 18, 252300), verbose_name='date published'),
        ),
    ]

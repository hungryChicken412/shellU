# Generated by Django 3.2.4 on 2021-07-02 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_puzzle_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 2, 20, 22, 15, 760628), verbose_name='date published'),
        ),
    ]
# Generated by Django 3.2.4 on 2021-08-23 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_alter_puzzle_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='hasDone',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 23, 21, 55, 38, 665773), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='PuzzleSolution',
        ),
    ]

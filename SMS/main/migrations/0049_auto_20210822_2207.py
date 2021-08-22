# Generated by Django 3.2.4 on 2021-08-22 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_alter_puzzle_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzle',
            old_name='answer',
            new_name='functionName',
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 22, 22, 6, 54, 743489), verbose_name='date published'),
        ),
    ]

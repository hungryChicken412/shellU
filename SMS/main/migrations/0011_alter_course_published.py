# Generated by Django 3.2.4 on 2021-06-07 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_course_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 22, 22, 53, 24183), verbose_name='date published'),
        ),
    ]

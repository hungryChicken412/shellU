# Generated by Django 3.2.4 on 2021-06-07 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_course_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 23, 44, 53, 164109), verbose_name='date published'),
        ),
    ]

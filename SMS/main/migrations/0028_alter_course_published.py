# Generated by Django 3.2.4 on 2021-06-08 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_course_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 13, 10, 10, 109341), verbose_name='date published'),
        ),
    ]

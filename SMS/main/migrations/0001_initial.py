# Generated by Django 3.2.4 on 2021-06-07 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=datetime.datetime(2021, 6, 7, 22, 18, 43, 136542), verbose_name='date published')),
            ],
        ),
    ]

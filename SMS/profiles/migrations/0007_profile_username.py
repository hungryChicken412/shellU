# Generated by Django 3.2.4 on 2021-08-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210819_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='#user', max_length=200),
        ),
    ]

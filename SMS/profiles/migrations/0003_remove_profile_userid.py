# Generated by Django 3.2.4 on 2021-06-07 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_profile_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='userId',
        ),
    ]

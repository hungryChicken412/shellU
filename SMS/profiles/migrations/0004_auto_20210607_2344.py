# Generated by Django 3.2.4 on 2021-06-07 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
    ]

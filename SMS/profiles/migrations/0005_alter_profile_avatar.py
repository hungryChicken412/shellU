# Generated by Django 3.2.4 on 2021-06-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210607_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='chicken.jpg', upload_to='avatars/'),
        ),
    ]
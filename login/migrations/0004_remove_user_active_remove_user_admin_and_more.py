# Generated by Django 4.1.5 on 2023-01-22 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_living_alone_user_userimage_user_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='staff',
        ),
    ]
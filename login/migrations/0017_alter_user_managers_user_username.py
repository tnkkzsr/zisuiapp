# Generated by Django 4.1.5 on 2023-01-22 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_remove_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=128, verbose_name='ニックネーム'),
        ),
    ]

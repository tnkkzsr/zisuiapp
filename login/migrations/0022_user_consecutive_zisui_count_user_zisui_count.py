# Generated by Django 4.1.5 on 2023-02-10 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_alter_user_userimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='consecutive_zisui_count',
            field=models.CharField(default='0', max_length=128, verbose_name='総自炊回数'),
        ),
        migrations.AddField(
            model_name='user',
            name='zisui_count',
            field=models.CharField(default='0', max_length=128, verbose_name='総自炊回数'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-22 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_user_active_remove_user_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=128, verbose_name='ニックネーム'),
        ),
    ]

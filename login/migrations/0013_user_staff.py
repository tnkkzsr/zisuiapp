# Generated by Django 4.1.5 on 2023-01-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_remove_user_active_remove_user_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]

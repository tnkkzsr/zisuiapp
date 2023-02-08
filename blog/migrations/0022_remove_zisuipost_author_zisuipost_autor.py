# Generated by Django 4.1.5 on 2023-02-08 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0021_zisuipost_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zisuipost',
            name='author',
        ),
        migrations.AddField(
            model_name='zisuipost',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

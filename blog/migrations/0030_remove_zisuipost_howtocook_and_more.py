# Generated by Django 4.1.5 on 2023-02-10 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_zisuipost_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zisuipost',
            name='howtocook',
        ),
        migrations.RemoveField(
            model_name='zisuipost',
            name='ingredients',
        ),
    ]
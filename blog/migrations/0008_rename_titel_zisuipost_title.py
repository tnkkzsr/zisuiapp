# Generated by Django 4.1.5 on 2023-01-22 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_zisuipost_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zisuipost',
            old_name='titel',
            new_name='title',
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-19 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_text_recippost_titel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipPost',
            new_name='ZisuiPost',
        ),
    ]
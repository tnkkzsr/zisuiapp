# Generated by Django 4.1.5 on 2023-01-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_tag_alter_zisuipost_author_zisuipost_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]

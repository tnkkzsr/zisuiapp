# Generated by Django 4.1.5 on 2023-02-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_remove_zisuipost_howtocook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='freetext',
            field=models.TextField(blank=True, default='', null=True, verbose_name='説明'),
        ),
    ]
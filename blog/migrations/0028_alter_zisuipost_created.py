# Generated by Django 4.1.5 on 2023-02-09 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_zisuipost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
    ]

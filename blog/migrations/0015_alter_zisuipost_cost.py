# Generated by Django 4.1.5 on 2023-01-27 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='cost',
            field=models.CharField(choices=[('0~100', '0~100'), ('100~200', '100~200')], max_length=10, verbose_name='費用'),
        ),
    ]
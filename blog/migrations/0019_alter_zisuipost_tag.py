# Generated by Django 4.1.5 on 2023-01-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_zisuipost_freetext_alter_zisuipost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='tag',
            field=models.ManyToManyField(to='blog.tag', verbose_name='タグ'),
        ),
    ]
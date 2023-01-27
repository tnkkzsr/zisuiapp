# Generated by Django 4.1.5 on 2023-01-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_zisuipost_cost_alter_zisuipost_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='freetext',
            field=models.TextField(default='コメントを入力', verbose_name='コメント'),
        ),
        migrations.AlterField(
            model_name='zisuipost',
            name='howtocook',
            field=models.TextField(default='手順1:                                       \n手順2:\n手順3:\n手順4:\n手順5:\n手順6:\n', verbose_name='作り方'),
        ),
        migrations.AlterField(
            model_name='zisuipost',
            name='ingredients',
            field=models.TextField(default='1:                                       \n2:\n3:\n4:\n5:\n6:\n', max_length=128, verbose_name='材料'),
        ),
    ]

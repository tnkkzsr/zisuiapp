# Generated by Django 4.1.5 on 2023-01-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_zisuipost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='画像'),
        ),
    ]
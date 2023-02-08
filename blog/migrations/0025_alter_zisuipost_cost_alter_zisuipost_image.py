# Generated by Django 4.1.5 on 2023-02-08 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_zisuipost_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='cost',
            field=models.CharField(choices=[('0~100円', '0~100円'), ('100~200円', '100~200円'), ('200~300円', '200~300円'), ('300~400円', '300~400円'), ('500~600円', '500~600円'), ('600~700円', '600~700円'), ('700~800円', '700~800円'), ('800~900円', '800~900円'), ('900~1000円', '900~1000円'), ('1000円以上', '1000円以上'), ('不明', '不明')], max_length=20, verbose_name='費用'),
        ),
        migrations.AlterField(
            model_name='zisuipost',
            name='image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='画像'),
        ),
    ]

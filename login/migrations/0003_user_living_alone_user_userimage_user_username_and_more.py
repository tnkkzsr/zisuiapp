# Generated by Django 4.1.5 on 2023-01-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='living_alone',
            field=models.CharField(default='年', max_length=128, verbose_name='一人暮らし歴'),
        ),
        migrations.AddField(
            model_name='user',
            name='userimage',
            field=models.ImageField(default='', upload_to='images/', verbose_name='画像'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=128, verbose_name='ユーザー名'),
        ),
        migrations.AddField(
            model_name='user',
            name='years',
            field=models.CharField(default='大学\u3000年', max_length=128, verbose_name='学年'),
        ),
    ]

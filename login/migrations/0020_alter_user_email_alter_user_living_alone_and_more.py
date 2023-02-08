# Generated by Django 4.1.5 on 2023-02-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_alter_user_years'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Eメールアドレス(ログイン時に使用）'),
        ),
        migrations.AlterField(
            model_name='user',
            name='living_alone',
            field=models.CharField(choices=[('1年', '1年'), ('2年', '2年'), ('3年', '3年'), ('4年', '4年'), ('5年', '5年'), ('6年', '6年'), ('7年以上', '7年以上')], default='1年', max_length=128, verbose_name='一人暮らし歴'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userimage',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/', verbose_name='プロフィール画像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='years',
            field=models.CharField(choices=[('大学1年', '大学1年'), ('大学2年', '大学2年'), ('大学3年', '大学3年'), ('大学4年', '大学4年'), ('大学院1年', '大学院1年'), ('大学院2年', '大学院2年'), ('社会人', '社会人'), ('その他', 'その他')], default='大学1年', max_length=128, verbose_name='学年'),
        ),
    ]
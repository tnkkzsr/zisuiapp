# Generated by Django 4.1.5 on 2023-01-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='years',
            field=models.CharField(choices=[('あなたの学年を選択してください', 'あなたの学年を選択してください'), ('大学1年', '大学1年'), ('大学2年', '大学2年'), ('大学3年', '大学3年'), ('大学4年', '大学4年'), ('大学院1年', '大学院1年'), ('大学院2年', '大学院2年'), ('社会人', '社会人'), ('設定しない', '設定しない')], max_length=128, verbose_name='学年'),
        ),
    ]
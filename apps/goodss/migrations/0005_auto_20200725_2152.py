# Generated by Django 3.0.8 on 2020-07-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodss', '0004_auto_20200724_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='tag',
            field=models.ManyToManyField(to='goodss.Tag', verbose_name='タグ'),
        ),
    ]

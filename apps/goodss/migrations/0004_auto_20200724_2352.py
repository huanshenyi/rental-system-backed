# Generated by Django 3.0.8 on 2020-07-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodss', '0003_goods_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='tag',
            field=models.ManyToManyField(null=True, to='goodss.Tag', verbose_name='タグ'),
        ),
    ]

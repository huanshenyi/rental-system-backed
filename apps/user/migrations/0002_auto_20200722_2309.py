# Generated by Django 3.0.8 on 2020-07-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=200, null=True, verbose_name='アイコンリンク'),
        ),
    ]
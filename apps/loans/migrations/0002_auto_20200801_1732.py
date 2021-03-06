# Generated by Django 3.0.8 on 2020-08-01 08:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodss', '0007_auto_20200729_2157'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='period',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='period',
            unique_together={('owner', 'goods')},
        ),
    ]

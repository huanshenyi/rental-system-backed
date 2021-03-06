# Generated by Django 3.0.8 on 2020-07-21 11:52

from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='グループ名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='新規時間')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False, verbose_name='ユーザーテーブル主キー')),
                ('telephone', models.CharField(max_length=11, null=True, unique=True, verbose_name='携帯番号')),
                ('email', models.EmailField(max_length=100, null=True, unique=True, verbose_name='アドレス')),
                ('username', models.CharField(max_length=100, verbose_name='ユーザーネーム')),
                ('avatar', models.CharField(max_length=200, verbose_name='アイコンリンク')),
                ('data_joined', models.DateTimeField(auto_now_add=True, verbose_name='新規時間')),
                ('is_active', models.BooleanField(default=True, verbose_name='アカウント状態')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Group', verbose_name='所属グループ')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

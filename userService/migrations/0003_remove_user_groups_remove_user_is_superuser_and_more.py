# Generated by Django 4.2.16 on 2024-10-10 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userService', '0002_rename_hashed_password_user_password_user_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]

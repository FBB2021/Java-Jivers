# Generated by Django 4.1.1 on 2022-10-07 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_remove_user_accountcreattime_remove_user_firstname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lastLoginTime',
        ),
    ]

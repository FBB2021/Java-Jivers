# Generated by Django 4.1.1 on 2022-10-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_user_accountcreattime_alter_user_contactnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='accountCreatTime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Account Creation Time'),
        ),
    ]

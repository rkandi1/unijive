# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-16 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180203_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(default='C:/webpages/static/icons_/account_icon.PNG', upload_to=''),
        ),
    ]

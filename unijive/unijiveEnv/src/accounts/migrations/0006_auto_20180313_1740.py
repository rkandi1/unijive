# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-13 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180216_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(default='/webpages/static/icons_/account_icon.PNG', upload_to=''),
        ),
    ]

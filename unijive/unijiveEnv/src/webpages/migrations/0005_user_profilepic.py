# Generated by Django 2.0.1 on 2018-01-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_auto_20180117_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilePic',
            field=models.ImageField(default='/webpages/static/icons_/account_icon.PNG', upload_to=''),
        ),
    ]

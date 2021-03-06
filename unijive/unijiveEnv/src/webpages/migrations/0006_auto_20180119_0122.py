# Generated by Django 2.0.1 on 2018-01-19 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_user_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='memberSince',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='OG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]

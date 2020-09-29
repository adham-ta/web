# Generated by Django 2.2.4 on 2020-07-30 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0134_auto_20200728_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ignore_tribes',
            field=models.ManyToManyField(related_name='ignore', to='dashboard.Profile'),
        ),
        migrations.AlterField(
            model_name='tribessubscription',
            name='expires_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 30, 15, 18, 54, 734516), null=True),
        ),
    ]
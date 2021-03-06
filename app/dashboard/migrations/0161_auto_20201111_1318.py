# Generated by Django 2.2.4 on 2020-11-11 13:18

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0160_auto_20201111_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='identity_data_google',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_google_verified',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EPLNews', '0002_team_api_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EPLNews', '0010_auto_20170817_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='card',
        ),
        migrations.AddField(
            model_name='card',
            name='red_card',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='total_card',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='yellow_card',
            field=models.IntegerField(default=0),
        ),
    ]

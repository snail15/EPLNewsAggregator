# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EPLNews', '0007_auto_20170817_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standing',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]

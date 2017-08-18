# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('img_url', models.TextField()),
                ('source', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('newses', models.ManyToManyField(related_name='teams', to='EPLNews.News')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='playing_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='EPLNews.Team'),
        ),
    ]
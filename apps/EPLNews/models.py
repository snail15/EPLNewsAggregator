# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    url = models.TextField()
    img_url = models.TextField()
    source = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return "News #{0}, Title: {1}, Source {2}".format(self.id, self.title, self.source)

class Team(models.Model):
    name = models.CharField(max_length=100)
    api_name = models.CharField(max_length=100)
    newses = models.ManyToManyField(News, related_name='teams')
    def __repr__(self):
        return "Team: {0}".format(self.name)

class Player(models.Model):
    name = models.CharField(max_length=100)
    playing_team = models.ForeignKey(Team, related_name='players')
    created_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return "Player: {0}, {1}".format(self.name, self.playing_team)

class Standing(models.Model):
    position = models.IntegerField(default=0)
    name = models.CharField(max_length=40)
    gp = models.IntegerField()
    won = models.IntegerField()
    draw = models.IntegerField()
    lost = models.IntegerField()
    gs = models.IntegerField()
    ga = models.IntegerField()
    gd = models.IntegerField()
    point = models.IntegerField()
    recent_form = models.CharField(max_length=20)
    status = models.CharField(max_length=30)
    logo_url = models.CharField(max_length=100)

class Score(models.Model):
    name = models.CharField(max_length=55)
    logo_url = models.CharField(max_length=255)
    goal = models.IntegerField()
    nationality = models.CharField(max_length=30)
    img_url = models.CharField(max_length=255, default=None)

class Assist(models.Model):
    name = models.CharField(max_length=55)
    logo_url = models.CharField(max_length=255)
    assist = models.IntegerField()
    nationality = models.CharField(max_length=30)
    img_url = models.CharField(max_length=255, default=None)

class Card(models.Model):
    name = models.CharField(max_length=55)
    logo_url = models.CharField(max_length=255)
    yellow_card = models.IntegerField(default=0)
    red_card = models.IntegerField(default=0)
    nationality = models.CharField(max_length=30)
    img_url = models.CharField(max_length=255, default=None)
    total_card = models.IntegerField(default=0)

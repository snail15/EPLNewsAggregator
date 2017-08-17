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
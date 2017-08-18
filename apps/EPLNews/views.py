# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages
# import bcrypt

# Create your views here.

def index(request):
    all_news = News.objects.filter(teams=None).order_by('-created_at')
    top_news = all_news[0]
    header_news = all_news[1:5]
    news = all_news[5:11]
    epl_standing = Standing.objects.all().order_by('position')
    top_score_player = Score.objects.all().order_by('-goal')[:5]
    top_card_player = Card.objects.all().order_by('-total_card')[:5]
    context = {
        'top_news': top_news,
        'header_news': header_news,
        'news': news,
        'standing': epl_standing,
        'top_score': top_score_player,
        'top_card': top_card_player

    }
    return render(request, 'EPLNews/index.html', context)

def team_news(request):
    team_name = request.POST['team_name']
    all_news = News.objects.filter(teams=Team.objects.filter(api_name=team_name)).order_by('-created_at')
    top_news = all_news[0]
    header_news = all_news[1:5]
    news = all_news[5:11]
    context = {
        'top_news': top_news,
        'header_news': header_news,
        'news': news
    }
    return render(request, 'EPLNews/team_news.html', context)
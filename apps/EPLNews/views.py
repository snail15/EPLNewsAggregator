# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages
# import bcrypt

# Create your views here.

def index(request):
    top_news = News.objects.filter(teams=None).order_by('-created_at')[0]
    header_news = News.objects.filter(teams=None).order_by('-created_at')[1:5]
    news = News.objects.filter(teams=None).order_by('-created_at')[5:11]
    context = {
        'top_news': top_news,
        'header_news': header_news,
        'news': news
    }
    return render(request, 'EPLNews/index.html', context)


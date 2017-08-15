# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    pass
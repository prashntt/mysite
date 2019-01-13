# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('Hi!!! This is home page')

def about(request):
	return HttpResponse('Hi!!! This is About page')



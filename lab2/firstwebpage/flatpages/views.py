# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render
from django import template

def home(request):
    return render(request, 'templates/index.html')


def hello(request):
    return HttpResponse(u'Привет, Мир!')

def static_handler(request):
    return render(request, 'templates/static_handler.html')
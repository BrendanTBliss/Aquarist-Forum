from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def freshwater(request):
  return HttpResponse('<h1>Freshwater</h1>')

from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'home.html')

def freshwater(request):
  return HttpResponse('<h1>Freshwater</h1>')

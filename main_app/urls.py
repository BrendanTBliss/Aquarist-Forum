from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('aqua_agora', views.home, name='home'),
    path('aqua_agora/signup', views.register, name='register'),
    path('aqua_agora/sent/', views.activation_sent, name="activation_sent"),
    path('aqua_agora/activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('aqua_agora/freshwater', views.freshwater, name='freshwater'),
]
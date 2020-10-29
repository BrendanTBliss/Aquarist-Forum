from django.urls import path
from . import views

urlpatterns = [
    path('aquarist', views.home, name='home'),
    path('aquarist/freshwater', views.freshwater, name='freshwater'),
]
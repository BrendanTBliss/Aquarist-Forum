from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import home, signup, activation_sent_view, activate

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_detail, name='profile'),
    path('profile/<int:user_id>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:user_id>/delete/', views.profile_delete, name='profile_delete'),
    path('topics/', views.topics_index, name="topics_index"),
    path('topics/<int:topic_id>/', views.topics_detail, name='topics_detail'),
    path('posts/', views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.signup, name='signup'),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]

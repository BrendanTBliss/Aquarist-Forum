from django import VERSION #delete this line
from django.urls import path, include, re_path #delete re_path
from django.conf.urls import url
from . import views
from .views import home, signup, activation_sent_view, activate, InboxView, SentView, ArchivesView, TrashView, WriteView, ReplyView, MessageView, ConversationView, ArchiveView, DeleteView, UndeleteView, MarkReadView, MarkUnreadView, IndexView #delete InboxView, SentView, ArchivesView, TrashView, WriteView, ReplyView, MessageView, ConversationView, ArchiveView, DeleteView, UndeleteView, MarkReadView, MarkUnreadView, IndexView
from django.conf import settings
from django.conf.urls.static import static
if getattr(settings, 'POSTMAN_I18N_URLS', False):  #delete this line
    from django.utils.translation import pgettext_lazy   #delete this line
else:   #delete this line
    def pgettext_lazy(c, m): return m   #delete this line

# app_name = 'postman'
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
    path('activationsent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('upload/', views.image_upload_view, name='image_upload_view'),
    path('tank_images/', views.display_images, name = 'images'),
    path('user_posts/', views.user_posts_index, name='user_posts_index'),
    
    #DELETE ALL VIEWS BELOW HERE
    
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    re_path(pgettext_lazy('postman_url', r'^inbox/(?:(?P<option>m)/)?$'), InboxView.as_view(), name='inbox'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    re_path(pgettext_lazy('postman_url', r'^sent/(?:(?P<option>m)/)?$'), SentView.as_view(), name='sent'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    re_path(pgettext_lazy('postman_url', r'^archives/(?:(?P<option>m)/)?$'), ArchivesView.as_view(), name='archives'),
    # Translators: keep consistency of the <option> parameter with the translation for 'm'
    re_path(pgettext_lazy('postman_url', r'^trash/(?:(?P<option>m)/)?$'), TrashView.as_view(), name='trash'),
    re_path(pgettext_lazy('postman_url', r'^write/(?:(?P<recipients>[^/#]+)/)?$'), WriteView.as_view(), name='write'),
    re_path(pgettext_lazy('postman_url', r'^reply/(?P<message_id>[\d]+)/$'), ReplyView.as_view(), name='reply'),
    re_path(pgettext_lazy('postman_url', r'^view/(?P<message_id>[\d]+)/$'), MessageView.as_view(), name='view'),
    # Translators: 't' stands for 'thread'
    re_path(pgettext_lazy('postman_url', r'^view/t/(?P<thread_id>[\d]+)/$'), ConversationView.as_view(), name='view_conversation'),
    re_path(pgettext_lazy('postman_url', r'^archive/$'), ArchiveView.as_view(), name='archive'),
    re_path(pgettext_lazy('postman_url', r'^delete/$'), DeleteView.as_view(), name='delete'),
    re_path(pgettext_lazy('postman_url', r'^undelete/$'), UndeleteView.as_view(), name='undelete'),
    re_path(pgettext_lazy('postman_url', r'^mark-read/$'), MarkReadView.as_view(), name='mark-read'),
    re_path(pgettext_lazy('postman_url', r'^mark-unread/$'), MarkUnreadView.as_view(), name='mark-unread'),
    re_path(pgettext_lazy('postman_url', r'^postmanindex/$'), IndexView.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

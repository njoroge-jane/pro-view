from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from . import views

urlpatterns=[
path('', views.index, name='home'),
path('new/upload', views.upload, name='upload'),
path('profile/', views.profile, name='profile'),
path('search/', views.search_results, name='search_results'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
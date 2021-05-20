
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import gipda.views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',gipda.views.home,name="home"),
    path('new',gipda.views.new,name="new"),
    path('grammar',gipda.views.grammar,name="grammar"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

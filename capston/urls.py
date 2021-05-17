
from django.contrib import admin
from django.urls import path
import gipda.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',gipda.views.home,name="home"),
    path('new',gipda.views.new,name="new"),
    path('grammar',gipda.views.grammar,name="grammar"),
]

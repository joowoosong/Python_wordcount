from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.woo, name='woo'),
    path('song/', wordcount.views.song, name='song'),
    path('joo/', wordcount.views.joo, name='joo'),
]

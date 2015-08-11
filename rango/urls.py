# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from django.conf import settings

from rango import views

urlpatterns = patterns('',
    url(r'^about', views.about, name='about'),
    url(r'^$', views.index, name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static', (r'^media/(?P<path>.*'),
        'serve', {'document_root': settings.MEDIA_ROOT},
    )

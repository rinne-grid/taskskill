# coding: utf-8
from django.conf.urls import url, patterns, include

urlpatterns = [
    #url(r'^top/$|(?P<datepicker>\d{4}-\d{2}-\d{2})', 'rit.views.top', name='top'),
    url(r'^top/$', 'rit.views.top', name='top'),
]
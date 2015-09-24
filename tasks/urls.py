# coding: utf-8

from django.conf.urls import url, patterns
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^index$', 'tasks.views.do_login', name='login'),
    url(r'^logout$', 'tasks.views.do_logout', name='logout'),
    url(r'^top', 'tasks.views.top', name='top'),
    url(r'^post', 'tasks.views.do_post', name='post'),
]

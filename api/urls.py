# coding: utf-8

from django.conf.urls import url, patterns, include

urlpatterns = [
    url('^task_item_detail$', 'api.views.api_task_item_detail', name='task_item_detail'),
    url('^cre_user_task$', 'api.views.api_cre_user_task_item', name='cre_user_task'),
    url('^del_user_task$', 'api.views.api_del_user_task_item', name='del_user_task'),
    url('^add_user_task_memo$', 'api.views.api_add_user_task_item_memo', name='add_user_task_memo'),
    url('^do_user_task_status$', 'api.views.api_do_user_task_item_status', name='do_user_task_status'),
]
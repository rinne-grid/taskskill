# coding: utf-8
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout

from rit.models import TaskItem, UserTaskItem
from django.utils import timezone

@login_required
def top(request, datepicker=None):


    user = request.user
    #datepicker =
    print(str(request.POST))

    if 'datepicker' in request.POST:
        datepicker = request.POST["datepicker"]


    # ひとまず全部持ってくる。ユーザーが指定できるのはあとのバージョンで追加
    task_items_list = TaskItem.objects.all()

    task_ymd = timezone.now()
    if datepicker:
        task_ymd = datepicker
    else:
        task_ymd = "{0:%Y-%m-%d}".format(task_ymd)

    print(task_ymd)
    user_tasks_list = UserTaskItem.objects.filter(user=user, task_ymd=task_ymd)

    return render_to_response('rit/top.html',
                              dict(task_items_list=task_items_list, user_tasks_list=user_tasks_list,
                                   task_ymd=task_ymd),
                              RequestContext(request))


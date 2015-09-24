from django.shortcuts import (render, render_to_response,
                              get_object_or_404, Http404, redirect, urlresolvers)

from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from tasks.forms import LoginForm, TaskReportForm
from tasks.models import PlayerTask, Player

from tasks.functions import check_task_save, get_player_task

def top(request):
    if request.method == "GET":
        form = TaskReportForm()

        return render_to_response('tasks/top.html',
                                  dict(form=form, player_task_list=get_player_task(request, timezone.now())),
                                  RequestContext(request))

def do_post(request):
    if request.method == "POST":
        form = TaskReportForm(request.POST)
        if form.is_valid():
            task_item_detail = form.cleaned_data["task_item_detail"]
            memo = form.cleaned_data["memo"]
            ymd = timezone.now()
            player_task = PlayerTask()
            player_task.task_item_detail = task_item_detail
            player_task.memo = memo
            player_task.task_ymd = ymd
            player_task.player = Player.objects.get(user__username=request.user.username)


            if check_task_save(request, task_item_detail):
                player_task.save()

                return redirect(urlresolvers.reverse_lazy('tasks:top'))
            else:
                return render_to_response('tasks/top.html',
                                          dict(form=form, player_task_list=get_player_task(request, timezone.now()),
                                               error_message="魔力が足りません"),
                                          RequestContext(request))

        else:
            return render_to_response('tasks/top.html',
                                      dict(form=form, player_task_list=get_player_task(request, timezone.now())),
                                      RequestContext(request))




def do_logout(request):
    logout(request)
    return redirect(urlresolvers.reverse_lazy('tasks:login'))


def do_login(request):

    if request.method == "GET":
        form = LoginForm()
        return render_to_response('index.html',
                                  dict(form=form),
                                  RequestContext(request)
                                  )
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect(urlresolvers.reverse_lazy('rit:top'))
            else:
                return render_to_response('index.html',
                                          dict(form=LoginForm(initial={'username':username, 'password':password}),
                                               error_message="ログインに失敗しました。"),
                                          RequestContext(request))


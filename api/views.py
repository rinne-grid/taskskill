# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# task
from tasks.models import TaskItemDetail

# rit
from rit.models import TaskItem as RitTaskItem, UserTaskItem

from collections import OrderedDict
import json
import datetime

def api_task_item_detail(request):
    key = request.POST["key"]
    item_detail_list = TaskItemDetail.objects.filter(task_item__id=key)

    # python辞書をjsonに変換
    # OrderedDictを利用
    task_item_details = []
    for item in item_detail_list.order_by('id'):
        item_dict = OrderedDict([
            ('id', item.id),
            ('name', item.name),
            ('point', item.point),
        ])
        task_item_details.append(item_dict)

    json_str = json.dumps(task_item_details, ensure_ascii=False, indent=2)

    return HttpResponse(json_str, content_type='application/json; charset=UTF-8')

def api_cre_user_task_item(request):
    key = request.POST["key"]
    task_ymd = request.POST["task_ymd"]
    task_item = RitTaskItem.objects.get(pk=key)

    # TODO: エラー制御を忘れずに
    user_item = UserTaskItem()
    user_item.task_item = task_item
    user_item.user = request.user

    task_ymd_ptime = datetime.datetime.strptime(task_ymd, "%Y-%m-%d")

    user_item.task_ymd = task_ymd_ptime
    user_item.finished = False
    user_item.save()

    item_dict = {'task_id': user_item.id}
    json_str = json.dumps(item_dict, ensure_ascii=False, indent=2)

    return HttpResponse(json_str, content_type='application/json; charset=UTF-8')

def api_del_user_task_item(request):
    key = request.POST["key"]

    user_item = UserTaskItem.objects.get(pk=key)
    user_item.delete()

    return HttpResponse("deleted")

def api_add_user_task_item_memo(request):
    key = request.POST["key"]
    memo = request.POST["memo"]

    user_item = UserTaskItem.objects.get(pk=key)
    user_item.memo = memo
    user_item.save()

    return HttpResponse("ok")

def api_do_user_task_item_status(request):
    key = request.POST["key"]
    status = request.POST["status"]

    # 終了：True、まだ：False
    task_status = True
    if status == "doing":
        task_status = False

    user_item = UserTaskItem.objects.get(pk=key)
    user_item.finished = task_status
    user_item.save()

    return HttpResponse("ok")
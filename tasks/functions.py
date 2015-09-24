# coding: utf-8
from django.utils import timezone
from tasks.models import PlayerTask, Player

def check_task_save(request, task_detail):
    user = request.user
    if user is not None and user.is_authenticated():
        player = Player.objects.get(user=user)
        player_task = PlayerTask.objects.filter(player__user=request.user, task_ymd=timezone.now())

        dec_pt = task_detail.point
        for task in player_task:
            dec_pt += task.task_item_detail.point

        if player.skill_point - dec_pt < 0:
            return False
        else:
            return True

def get_player_task(request, tz_info):
    return PlayerTask.objects.filter(player__user=request.user, task_ymd=tz_info)

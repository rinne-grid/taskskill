# coding: utf-8

from tasks.models import Player, PlayerTask
from django.utils import timezone
def user_account_config(request):
    """
    user = request.user

    if user is not None and user.is_authenticated():
        player = Player.objects.get(user__username=user.username)
        player_task = PlayerTask.objects.filter(player__user=request.user, task_ymd=timezone.now())

        dec_pt = 0
        for task in player_task:
            dec_pt += task.task_item_detail.point


        return {
            'skill_point':player.skill_point - dec_pt,
            'level': player.level,
        }
    else:
        return {
            'none':'none',
        }
    """
from django.contrib import admin
from tasks.models import Player, PlayerTask, TaskItem, TaskItemDetail
admin.site.register(Player)
admin.site.register(PlayerTask)
admin.site.register(TaskItem)
admin.site.register(TaskItemDetail)


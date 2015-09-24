from django.contrib import admin

from rit.models import TaskItem, UserTaskItem
# Register your models here.
admin.site.register(TaskItem)
admin.site.register(UserTaskItem)
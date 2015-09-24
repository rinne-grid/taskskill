from django.db import models
from django.contrib.auth.models import User

class TaskItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserTaskItem(models.Model):
    user = models.ForeignKey(User)
    task_ymd = models.DateField()
    task_item = models.ForeignKey(TaskItem)
    memo = models.CharField(max_length=255, null=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + self.task_item.name

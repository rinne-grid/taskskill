# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskItem(models.Model):
    """読書、勉強、執筆等
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TaskItemDetail(models.Model):
    """易しい本、普通の本
    """
    task_item = models.ForeignKey(TaskItem)
    name = models.CharField(max_length=200)
    point = models.PositiveIntegerField()

    def __str__(self):
        return self.name


#その日に使ったポイント合計

class Player(models.Model):
    """プレイヤーの属性情報
    """
    user = models.ForeignKey(User)
    level = models.PositiveIntegerField(default=1)
    skill_point = models.PositiveIntegerField(default=100)
    exp = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username + "Lv:" + str(self.level)


class PlayerTask(models.Model):
    """プレイヤーのタスク
    """
    player = models.ForeignKey(Player)
    task_item_detail = models.ForeignKey(TaskItemDetail)
    task_ymd = models.DateField()
    memo = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.task_item_detail.name


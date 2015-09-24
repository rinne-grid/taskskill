# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('level', models.PositiveIntegerField()),
                ('skill_point', models.PositiveIntegerField(default=100)),
                ('exp', models.PositiveIntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('task_ymd', models.DateField()),
                ('player', models.ForeignKey(to='tasks.Player')),
            ],
        ),
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TaskItemDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('point', models.PositiveIntegerField()),
                ('task_item', models.ForeignKey(to='tasks.TaskItem')),
            ],
        ),
        migrations.AddField(
            model_name='playertask',
            name='task_item_detail',
            field=models.ForeignKey(to='tasks.TaskItemDetail'),
        ),
    ]

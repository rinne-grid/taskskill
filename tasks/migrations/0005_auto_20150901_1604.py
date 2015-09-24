# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_playertask_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playertask',
            name='memo',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]

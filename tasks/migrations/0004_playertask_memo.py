# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20150901_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='playertask',
            name='memo',
            field=models.TextField(max_length=1000, default=''),
            preserve_default=False,
        ),
    ]

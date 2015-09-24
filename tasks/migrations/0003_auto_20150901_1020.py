# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150901_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='exp',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

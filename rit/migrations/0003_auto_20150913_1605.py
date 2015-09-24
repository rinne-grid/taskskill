# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rit', '0002_usertaskitem_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertaskitem',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]

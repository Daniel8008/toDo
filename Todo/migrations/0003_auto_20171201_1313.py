# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_auto_20171201_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 13, 13, 40, 191340)),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_auto_20171201_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 8, 44, 48, 573086)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(max_length=42524),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
                ('text', models.CharField(max_length=4252)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 11, 26, 15, 6, 1, 430304), blank=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0018_mylist_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='Body',
            field=models.TextField(default=b'please enter some text'),
        ),
    ]

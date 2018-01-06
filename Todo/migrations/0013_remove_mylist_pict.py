# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0012_auto_20171213_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylist',
            name='pict',
        ),
    ]

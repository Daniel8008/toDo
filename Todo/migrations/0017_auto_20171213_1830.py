# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0016_auto_20171213_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mylist',
            old_name='created',
            new_name='Date',
        ),
    ]

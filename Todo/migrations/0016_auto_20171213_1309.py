# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0015_mylist_prev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mylist',
            old_name='prev',
            new_name='text_preview',
        ),
        migrations.RemoveField(
            model_name='mylist',
            name='text',
        ),
    ]

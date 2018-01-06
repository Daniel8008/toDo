# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0008_auto_20171212_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mylist',
            old_name='clip',
            new_name='pict',
        ),
    ]

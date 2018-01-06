# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0014_mylist_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist',
            name='prev',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

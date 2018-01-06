# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0017_auto_20171213_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist',
            name='Body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

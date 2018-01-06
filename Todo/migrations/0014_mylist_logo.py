# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0013_remove_mylist_pict'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist',
            name='logo',
            field=models.FileField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]

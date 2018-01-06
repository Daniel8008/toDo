# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0007_auto_20171212_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='clip',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]

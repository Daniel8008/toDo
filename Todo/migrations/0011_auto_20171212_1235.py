# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0010_auto_20171212_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='pict',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]

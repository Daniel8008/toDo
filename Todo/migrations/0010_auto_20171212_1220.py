# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0009_auto_20171212_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='pict',
            field=models.FileField(upload_to=b''),
        ),
    ]

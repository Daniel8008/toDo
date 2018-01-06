# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0006_auto_20171212_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='clip',
            field=models.FileField(upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='mylist',
            name='text',
            field=models.TextField(),
        ),
    ]

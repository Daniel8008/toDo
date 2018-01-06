# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0005_auto_20171212_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
                ('text', models.TextField(max_length=42524)),
                ('created', models.DateTimeField()),
                ('clip', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]

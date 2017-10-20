# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171006_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='std',
            field=models.CharField(max_length=10, default='---'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]

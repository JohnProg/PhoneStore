# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 12, 5, 23, 25, 657278, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 12, 5, 23, 30, 452700, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

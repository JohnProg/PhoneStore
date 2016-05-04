# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20160504_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(upload_to=apps.product.models.download_loc2, null=True, verbose_name='Logo', blank=True),
        ),
    ]

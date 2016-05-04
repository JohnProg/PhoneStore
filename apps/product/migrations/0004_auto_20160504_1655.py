# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20160504_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='features',
        ),
        migrations.AddField(
            model_name='productfeature',
            name='product',
            field=models.ForeignKey(default=1, verbose_name='Producto', blank=True, to='product.Product'),
            preserve_default=False,
        ),
    ]

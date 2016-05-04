# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20160504_1712'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='products',
            field=models.ManyToManyField(related_name='products', verbose_name='Productos', to='product.Product', blank=True),
        ),
    ]

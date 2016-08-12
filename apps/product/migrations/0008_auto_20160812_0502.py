# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_brand_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeature',
            name='product',
            field=models.ForeignKey(related_name='features', verbose_name='Producto', blank=True, to='product.Product'),
        ),
    ]

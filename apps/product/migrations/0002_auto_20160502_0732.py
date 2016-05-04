# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='video_url',
            new_name='video',
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(related_name='features', verbose_name='Caracter\xedstica', to='product.ProductFeature', blank=True),
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Nombre de la caracter\xedstica'),
        ),
    ]

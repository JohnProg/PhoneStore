# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.product.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=120, verbose_name='Nombre del Producto')),
                ('frontal_image', models.ImageField(upload_to=apps.product.models.download_loc, null=True, verbose_name='Im\xe1gen Frontal', blank=True)),
                ('back_image', models.ImageField(upload_to=apps.product.models.download_loc, null=True, verbose_name='Im\xe1gen Trasera', blank=True)),
                ('video_url', models.URLField(null=True, verbose_name='Video', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo', choices=[(True, 'Activo'), (False, 'No Activo')])),
            ],
            options={
                'db_table': 'product',
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80, verbose_name='Nombre de la tienda')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo', choices=[(True, 'Activo'), (False, 'No Activo')])),
            ],
            options={
                'db_table': 'feature',
                'verbose_name': 'ProductFeature',
                'verbose_name_plural': 'ProductFeatures',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(related_name='features', verbose_name='Usuarios', to='product.ProductFeature', blank=True),
        ),
    ]

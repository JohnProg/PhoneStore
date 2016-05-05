# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_brand_logo'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_visible', models.BooleanField(default=False, verbose_name='Es Visible', choices=[(True, 'Visible'), (False, 'No Visible')])),
                ('product', models.ForeignKey(verbose_name='Producto', to='product.Product')),
                ('store', models.ForeignKey(verbose_name='Tienda', to='users.Store')),
            ],
            options={
                'db_table': 'store_product',
                'verbose_name': 'Tienda Producto',
                'verbose_name_plural': 'Tienda Productos',
            },
        ),
        migrations.AddField(
            model_name='store',
            name='products',
            field=models.ManyToManyField(related_name='products', verbose_name='Productos', to='product.Product', through='users.StoreProduct', blank=True),
        ),
    ]

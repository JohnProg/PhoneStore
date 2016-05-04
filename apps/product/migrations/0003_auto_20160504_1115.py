# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160502_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80, verbose_name='Nombre de la marca')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo', choices=[(True, 'Activo'), (False, 'No Activo')])),
            ],
            options={
                'db_table': 'brand',
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, verbose_name='Marca', blank=True, to='product.Brand'),
            preserve_default=False,
        ),
    ]

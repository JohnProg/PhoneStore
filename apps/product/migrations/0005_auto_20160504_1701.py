# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20160504_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeature',
            name='description',
            field=models.TextField(verbose_name='Descripci\xf3n de la caracter\xedstica', blank=True),
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Nombre de la caracter\xedstica'),
        ),
    ]

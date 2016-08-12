# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160505_0304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storeproduct',
            options={'verbose_name': 'Productos para el carrusel', 'verbose_name_plural': 'Productos para el carrusel'},
        ),
        migrations.AlterField(
            model_name='store',
            name='user',
            field=models.ManyToManyField(related_name='stores', verbose_name='Usuarios', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20160504_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productfeature',
            options={'verbose_name': 'Caracter\xedstica', 'verbose_name_plural': 'Caracter\xedsticas'},
        ),
    ]

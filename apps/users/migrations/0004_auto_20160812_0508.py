# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160812_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='telephone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Tel\xe9fono', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'solo se permite ingresar numeros.'), django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(12)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='cellphone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Celular', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'solo se permite ingresar numeros.'), django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(12)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Tel\xe9fono', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'solo se permite ingresar numeros.'), django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(12)]),
        ),
    ]

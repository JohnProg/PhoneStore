# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.commons.utils.constants import STATUS_CHOICES, STATUS_ACTIVE
from django.conf import settings


class Store(models.Model):
    """
    Organization model
    """
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='users',
        verbose_name=_(u'Usuarios'),
        blank=True
    )
    store_name = models.CharField(
        max_length=80,
        verbose_name=_(u'Nombre de la tienda')
    )
    telephone = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name=_(u'Teléfono')
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name=_(u'Correo electrónico')
    )

    is_active = models.BooleanField(
        choices=STATUS_CHOICES,
        verbose_name=_(u'Activo'),
        default=STATUS_ACTIVE
    )

    def __unicode__(self):
        return unicode(self.store_name)

    def __str__(self):
        return unicode(self).encode('utf-8')

    class Meta:
        db_table = 'store'
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"
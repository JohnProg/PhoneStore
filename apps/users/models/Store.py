# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.utils.translation import ugettext_lazy as _

from apps.commons.utils.database import AuditableMixin
from apps.commons.utils.constants import STATUS_CHOICES, STATUS_ACTIVE, VISIBLE_CHOICES, NO_VISIBLE
from django.conf import settings
from apps.product.models import Product
from apps.users.models.StoreProduct import StoreProduct


class Store(AuditableMixin):
    """
    Store model
    """
    alphanumeric = RegexValidator(r'^[0-9]*$', 'solo se permite ingresar numeros.')
    products = models.ManyToManyField(
        Product,
        through=StoreProduct,
        related_name='products',
        verbose_name=_(u'Productos'),
        blank=True
    )
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='stores',
        verbose_name=_(u'Usuarios'),
        blank=True
    )
    store_name = models.CharField(
        max_length=80,
        verbose_name=_(u'Nombre de la tienda')
    )
    telephone = models.CharField(
        max_length=12,
        verbose_name=_(u'Teléfono'),
        validators=[
            alphanumeric,
            MinLengthValidator(4),
            MaxLengthValidator(12),
        ],
        null=True,
        blank=True
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
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'

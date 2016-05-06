# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from apps.commons.utils.constants import VISIBLE_CHOICES, NO_VISIBLE
from apps.product.models import Product


class StoreProduct(models.Model):
    store = models.ForeignKey(settings.STORE_MODEL, verbose_name=_(u'Tienda'))
    product = models.ForeignKey(Product, verbose_name=_(u'Producto'))
    is_visible = models.BooleanField(
        choices=VISIBLE_CHOICES,
        verbose_name=_(u'Es Visible'),
        default=NO_VISIBLE
    )

    def __unicode__(self):
        return unicode('%s-%s' % (self.store, self.product))

    class Meta:
        db_table = 'store_product'
        verbose_name = "Productos para el carrusel"
        verbose_name_plural = "Productos para el carrusel"
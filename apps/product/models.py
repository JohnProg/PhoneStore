# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.commons.utils.constants import STATUS_CHOICES, STATUS_ACTIVE
from django.conf import settings

from apps.commons.utils.validators import get_name_token


def download_loc(instance, filename):
    return "user/%s" % get_name_token(filename)


class Brand(models.Model):
    """
    Brand model
    """
    title = models.CharField(
        max_length=80,
        verbose_name=_(u'Nombre de la marca')
    )
    is_active = models.BooleanField(
        choices=STATUS_CHOICES,
        verbose_name=_(u'Activo'),
        default=STATUS_ACTIVE
    )

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return unicode(self).encode('utf-8')

    class Meta:
        db_table = 'brand'
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


class ProductFeature(models.Model):
    """
    ProductFeature model
    """
    title = models.CharField(
        max_length=80,
        verbose_name=_(u'Nombre de la característica')
    )
    is_active = models.BooleanField(
        choices=STATUS_CHOICES,
        verbose_name=_(u'Activo'),
        default=STATUS_ACTIVE
    )

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return unicode(self).encode('utf-8')

    class Meta:
        db_table = 'feature'
        verbose_name = "ProductFeature"
        verbose_name_plural = "ProductFeatures"


class Product(models.Model):
    """
    Product model
    """
    features = models.ManyToManyField(
        ProductFeature,
        related_name='features',
        verbose_name=_(u'Característica'),
        blank=True
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name=_(u'Marca'),
        blank=True
    )
    title = models.CharField(
        max_length=120,
        verbose_name=_(u'Nombre del Producto')
    )
    frontal_image = models.ImageField(
        upload_to=download_loc,
        blank=True, null=True,
        verbose_name=_(u'Imágen Frontal')
    )
    back_image = models.ImageField(
        upload_to=download_loc,
        blank=True, null=True,
        verbose_name=_(u'Imágen Trasera')
    )
    video = models.URLField(
        null=True,
        blank=True,
        verbose_name=_(u'Video')
    )
    is_active = models.BooleanField(
        choices=STATUS_CHOICES,
        verbose_name=_(u'Activo'),
        default=STATUS_ACTIVE
    )

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return unicode(self).encode('utf-8')

    class Meta:
        db_table = 'product'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

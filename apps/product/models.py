# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from catalogo.settings import STATIC_URL, MEDIA_URL
from apps.commons.utils.constants import STATUS_CHOICES, STATUS_ACTIVE
from apps.commons.utils.validators import get_name_token


def download_loc(instance, filename):
    return "product/%s" % get_name_token(filename)


def download_loc2(instance, filename):
    return "brand/%s" % get_name_token(filename)


class Brand(models.Model):
    """
    Brand model
    """
    title = models.CharField(
        max_length=80,
        verbose_name=_(u'Nombre de la marca')
    )
    logo = models.ImageField(
        upload_to=download_loc2,
        blank=True, null=True,
        verbose_name=_(u'Logo')
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


class Product(models.Model):
    """
    Product model
    """
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

    @property
    def thumbnail(self):
        return MEDIA_URL + '%s' % self.frontal_image.name if self.frontal_image.name else STATIC_URL + "public/assets/images/user-default.png"

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return unicode(self).encode('utf-8')

    class Meta:
        db_table = 'product'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class ProductFeature(models.Model):
    """
    ProductFeature model
    """
    product = models.ForeignKey(
        Product,
        related_name='features',
        verbose_name=_(u'Producto'),
        blank=True
    )
    title = models.CharField(
        max_length=120,
        verbose_name=_(u'Nombre de la característica')
    )
    description = models.TextField(
        verbose_name=_(u'Descripción de la característica'),
        blank=True
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
        verbose_name = 'Característica'
        verbose_name_plural = 'Características'

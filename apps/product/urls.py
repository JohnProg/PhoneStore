# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from apps.product.views import products, product

urlpatterns = patterns('',
                       url(r'^api/products/$', products, name='products'),
                       url(r'^api/product/(?P<id>\d+)/$', product, name='product'),
                       )

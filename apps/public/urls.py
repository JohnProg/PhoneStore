# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from apps.product.views import IndexPage, ProductListPage, BrandListPage, ProductDetailPage
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
                       # landing page
                       url(r'^$', IndexPage.as_view(), name='home'),
                       url(r'^brands/(?P<brand_id>\d+)/products/$', ProductListPage.as_view(), name='list_product'),
                       url(r'^brands/(?P<brand_id>\d+)/products/(?P<product_id>\d+)/$', ProductDetailPage.as_view(), name='detail_product'),
                       url(r'^brands/$', BrandListPage.as_view(), name='list_brand'),
                       url(r'^login/$', login_author_user, name='login_user'),
                       url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout_user'),
                       )

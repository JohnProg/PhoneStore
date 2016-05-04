# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from apps.product.views import IndexPage, ProductListPage, BrandListPage
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
                       # landing page
                       url(r'^$', IndexPage.as_view(), name='home'),
                       url(r'^products/$', ProductListPage.as_view(), name='list_product'),
                       url(r'^brands/$', BrandListPage.as_view(), name='list_brand'),
                       url(r'^login/$', login_author_user, name='login_user'),
                       url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout_user'),
                       )

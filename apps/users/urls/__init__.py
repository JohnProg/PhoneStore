from django.conf.urls import url, include
from apps.users.views.profile import profile_user, account_user, organization_user, \
    ApplicationUserTemplateView, ProfileTemplateView, AdminTemplateView

urlpatterns = [
    url(r'^$', AdminTemplateView.as_view(), name='dashboard'),
    url(r'^organization/', include('apps.users.urls.organization')),

    url(r'^client/', include('apps.users.urls.client')),
    url(r'^member/', include('apps.users.urls.member')),
    # url(r'^users/', include('apps.users.urls.user')),
    url(r'^profile/', include('apps.users.urls.profile')),

    url(r'^applications/$', ApplicationUserTemplateView.as_view(), name='application'),
]

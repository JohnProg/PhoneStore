from django.conf.urls import url
from apps.users.views.profile import *

urlpatterns = [
    url(r'^$', ProfileTemplateView.as_view(), name='profile'),
    url(r'^upload-avatar/$', upload_avatar, name='upload_avatar'),
    url(r'^save-profile/$', profile_user, name='save_profile'),
    url(r'^save-account/$', account_user, name='save_account'),
    url(r'^save-organization/$', organization_user, name='save_organization'),

]

from django.conf.urls import url

from ..views import user

urlpatterns = [
    url(r'^list/$',
        user.ClientList.as_view(),
        name='client_list'),

    url(r'^invite/$',
        user.InviteUser.as_view(),
        name='client_invite'),

    url(r'^(?P<user_id>\d+)/delete/$',
        user.delete_user,
        name='client_delete_organization'),

    url(r'^(?P<user_id>\d+)/restore/$',
        user.restore_user,
        name='client_restore_organization'),
]

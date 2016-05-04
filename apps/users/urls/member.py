from django.conf.urls import url

from ..views import user

urlpatterns = [
    url(r'^list/$',
        user.MemberList.as_view(),
        name='team_list'),

    url(r'^invite/$',
        user.InviteUser.as_view(),
        name='team_invite'),

    url(r'^invite-resent/(?P<pk>\d+)/$',
        user.resent_invitation,
        name='team_resent_invitation'),

    url(r'^(?P<user_id>\d+)/delete/$',
        user.delete_user,
        name='team_delete_organization'),

    url(r'^(?P<user_id>\d+)/get/$',
        user.UserView.as_view(),
        name='team_get_organization'),

    url(r'^(?P<user_id>\d+)/restore/$',
        user.restore_user,
        name='team_restore_organization'),
]

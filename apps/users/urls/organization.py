from apps.users.views._user import team_confirm_member

from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<organization_id>\d+)/confirm/$',
        team_confirm_member,
        name='team_confirm_member'),
]

from django.conf.urls import url
from apps.users.views._user import module_client_list_for_organization, \
    add_or_create_member_to_organization, delete_team_member, \
    module_team_list_for_organization, update_team_member

from ..views import _user

urlpatterns = [
    # Clientes
    # url(r'^client/list/$',
    #     user.client_list,
    #     name='client_list'),
    # url(r'^client/list_json/$',
    #     module_client_list_for_organization,
    #     name='client_list_json'),
    #
    # #Equipo de trabajo
    # url(r'^member/list/$',
    #     user.team_list,
    #     name='team_list'),
    # url(r'^member/list_json/$',
    #     module_team_list_for_organization,
    #     name='team_list_json'),
    #
    # url(r'^add_or_create_member_to_organization/$',
    #     add_or_create_member_to_organization,
    #     name='client_create'),
    #
    # url(r'^(?P<user_id>\d+)/delete/$',
    #     delete_team_member,
    #     name='delete_team_member'),
    #
    # url(r'^(?P<user_id>\d+)/update/$',
    #     update_team_member,
    #     name='update_team_member'),
]

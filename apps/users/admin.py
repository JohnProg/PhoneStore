# coding=utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.users.models.Store import Store
from apps.users.models.StoreProduct import StoreProduct
from apps.users.models.User import User


class MyUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'imagen')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': (
            'username', 'first_name', 'last_name', 'dni','avatar', 'birth_date', 'telephone', 'cellphone', 'gender', )}),
        ('Permisos', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def imagen(self, user):
        tag = '<a href="{0}"><img src="{0}" width=50px height=50px/></a>'.format(user.thumbnail)
        return tag

    imagen.allow_tags = True

admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)


class StoreProductInline(admin.TabularInline):
    model = StoreProduct
    extra = 1


class StoreAdmin(admin.ModelAdmin):
    inlines = (StoreProductInline,)
    list_display = ('store_name', 'telephone', 'email', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ['store_name', 'email']

admin.site.register(Store, StoreAdmin)

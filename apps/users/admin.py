# coding=utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.users.models.Store import Store
from apps.users.models.StoreProduct import StoreProduct
from apps.users.models.User import User


class MyUserAdmin(UserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'avatar', 'birth_date', 'dni','telephone', 'cellphone', 'gender',)
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': (
            'username', 'first_name', 'last_name', 'dni','avatar', 'birth_date', 'telephone', 'cellphone', 'gender', )}),
        ('Permisos', {'fields': ('is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

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
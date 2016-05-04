# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager

from apps.commons.utils.constants import GENDER
from apps.commons.utils.validators import validate_dni, get_name_token
from catalogo.settings import STATIC_URL, MEDIA_URL


def download_loc(instance, filename):
    return "user/%s" % get_name_token(filename)


class User(AbstractUser):
    """
    User model
    """
    alphanumeric = RegexValidator(r'^[0-9]*$', 'solo se permite ingresar numeros.')
    avatar = models.ImageField(
        upload_to=download_loc,
        blank=True, null=True
    )
    telephone = models.CharField(
        max_length=12,
        verbose_name=_(u'Teléfono'),
        validators=[
            alphanumeric,
            MinLengthValidator(4),
            MaxLengthValidator(12),
        ],
    )
    cellphone = models.CharField(
        max_length=12,
        verbose_name=_(u'Celular'),
        validators=[
            alphanumeric,
            MinLengthValidator(4),
            MaxLengthValidator(12),
        ]
    )
    dni = models.CharField(
        verbose_name=_(u'DNI'),
        validators=[validate_dni],
        max_length=8
    )
    birth_date = models.DateField(
        blank=True, null=True,
        verbose_name=_(u'Fecha de nacimiento')
    )
    gender = models.IntegerField(
        choices=GENDER,
        blank=True, null=True,
        verbose_name=_(u'Sexo')
    )

    objects = UserManager()

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __unicode__(self):
        return self.username

    def __str__(self):
        return unicode(self).encode('utf-8')

    def thumbnail(self):
        return MEDIA_URL + '%s' % self.avatar.name if self.avatar.name else STATIC_URL + "public/assets/images/user-default.png"

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'users'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        default_permissions = ()
        unique_together = ('email', )

    @property
    def as_dict(self):
        user = {
            'id': self.id,
            'full_name': self.full_name,
            'cellphone': self.cellphone,
            'dni': self.dni,
            'thumbnail': self.thumbnail(),
        }
        return user
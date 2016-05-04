#! coding: utf-8
"""
Utils constants.
Authors:
    John Paul Machahuay Giraldo <john.cfmr.2009@gmail.com>
"""
from django.utils.translation import ugettext as _

MALE = 1
FEMALE = 2

GENDER = (
    (MALE, _('Hombre')),
    (FEMALE, _('Mujer'))
)

STATUS_ACTIVE = True
STATUS_INACTIVE = False

STATUS_CHOICES = (
    (STATUS_ACTIVE, _('Activo')),
    (STATUS_INACTIVE, _('No Activo'))
)
# coding=utf-8
"""
Utils validations.
Authors:
    John Paul Machahuay Giraldo <john.cfmr.2009@gmail.com>
"""
import re
import uuid

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def validate_phone(value):
    """
    Validates phone number
    :param value:  value to validate as a RUC number
    """
    if value and not re.match('\+*[0-9]{5,12}', value):
        raise ValidationError(
            _(u"%s no es un número de teléfono válido") % value, 400)


def validate_dni(value):
    """
    Validates DNI are only 8 numbers
    :param value:  value to validate as a DNI number
    """
    if value and not re.match('[0-9]{8}', value):
        raise ValidationError(_('%s is not valid DNI') % value)


def get_name_token(filename):
    return "%s.%s" % (str(uuid.uuid4()), filename.split('.')[-1])
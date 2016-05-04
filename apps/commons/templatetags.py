# coding=utf-8
import simplejson
from django import template
from django.core import urlresolvers
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='default_if_none')
def default_if_none(value, text):
    return text


@register.filter
def to_json(obj):
    return mark_safe(simplejson.dumps(obj))


def active(request, views):
    views = views
    try:
        view = urlresolvers.resolve(request.path).view_name
        url_name = urlresolvers.resolve(request.path).url_name
        if view in views or url_name in views:
            return 'class=active'
        else:
            return ""
    except urlresolvers.Resolver404:
        return ""

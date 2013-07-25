from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="phone")
@stringfilter
def phone_filter(value):
    if len(value) != 10: return value

    return  '(' + value[0:3] + ') ' + value[3:6] + '-' + value[6:10]
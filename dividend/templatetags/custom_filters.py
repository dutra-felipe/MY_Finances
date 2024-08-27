from django import template
from dividend.utils import convert_unix_timestamp


register = template.Library()


@register.filter(name='convert_unix_timestamp')
def convert_unix_timestamp_filter(value):
    return convert_unix_timestamp(value)


@register.filter
def to_percentage(value):
    try:
        return f"{value * 100:.2f}%"
    except TypeError:
        return "0.00%"

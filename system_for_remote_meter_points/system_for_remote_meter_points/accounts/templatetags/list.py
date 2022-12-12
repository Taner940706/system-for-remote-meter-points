from django.template import Library

register = Library()


@register.filter(name="lists")
def lists(value, text):
    value.field.widget.attrs['list'] = text
    return value
from django.template import Library

register = Library()


# templatetag for adding placeholders
@register.filter(name="placeholder")
def placeholder(value, text):
    value.field.widget.attrs['placeholder'] = text
    return value

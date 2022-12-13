from django.template import Library

register = Library()


# templatetag for adding form class
@register.filter(name="form_class")
def form_class(value):
    value.field.widget.attrs['class'] = 'form-control'
    return value

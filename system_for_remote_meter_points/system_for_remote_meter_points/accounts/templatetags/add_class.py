from django.template import Library

register = Library()


@register.filter(name="form_class")
def form_class(value):
    value.field.widget.attrs['class'] = 'form-control'
    return value
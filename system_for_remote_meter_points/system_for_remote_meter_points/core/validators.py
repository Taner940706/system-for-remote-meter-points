from django.core import exceptions


# only letter validation
def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed!')


# only digits validation
def only_int(value):
    if not value.isdigit():
        raise exceptions.ValidationError('Only digits are allowed!')

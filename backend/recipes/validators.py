from re import fullmatch

from django.core.exceptions import ValidationError


def validate_name(value):
    if not fullmatch(r'^[\w+.\-]$', value):
        return ValidationError('Имя рецепта должно состоять из...')
    return value

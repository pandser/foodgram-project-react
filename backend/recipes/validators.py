import re

from django.core.exceptions import ValidationError


def validate_name(value):
    if not re.fullmatch(r'^[а-яА-Яa-zA-Z\s]+$', value):
        return ValidationError('Имя рецепта должно состоять из ')
    return value

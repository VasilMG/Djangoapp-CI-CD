import datetime
import re

from django.core.exceptions import ValidationError


def date_validator(value):
    if value < datetime.date.today():
        raise ValidationError('Date cannot be in the past.')
    return value

def validate_load_size(value):
    if 0 > value or value > 15:
        raise ValidationError('The value should be between 0 and 15.00 meters')
    return value

def validate_load_weight(value):
    if 0 > value or value > 28:
        raise ValidationError('The value should be between 0 and 28 tons.')
    return value

def phone_number_validator(value):
    pattern = r'(\+\d{9,15}$)'
    the_match = re.match(pattern, value)
    if not the_match:
        raise ValidationError("Phone number must start with '+' followed by 9 up to 15 digits.")
    return value

def name_validator(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("The name cannot contain digits.")
    return value

def validate_price(value):
    if value < 0:
        raise ValidationError('The price cannot be less than zero.')
    return value


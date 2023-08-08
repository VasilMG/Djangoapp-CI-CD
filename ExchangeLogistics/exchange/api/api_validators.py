import datetime
from rest_framework import serializers


def api_date_validator(value):
    if value < datetime.date.today():
        raise serializers.ValidationError('Date cannot be in the past.')


def api_validate_load_size(value):
    if 0 > value or value > 15:
        raise serializers.ValidationError('The value should be between 0 and 15.00 meters')


def api_validate_load_weight(value):
    if 0 > value or value > 28:
        raise serializers.ValidationError('The value should be between 0 and 28 tons.')

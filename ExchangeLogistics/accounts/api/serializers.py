from django.contrib.auth import get_user_model
from rest_framework import serializers

from ExchangeLogistics.accounts.api.validators import name_validator, phone_number_validator
from ExchangeLogistics.accounts.models import CompanyProfile

UserModel = get_user_model()


class ConfirmPasswordSerializer(serializers.Serializer):
    confirm_password = serializers.CharField(max_length=30, required=True, style={'input_type': 'password'})


class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = ConfirmPasswordSerializer()

    class Meta:
        model = UserModel
        fields = [UserModel.USERNAME_FIELD, 'password', 'confirm_password']
        # fields = '__all__'
        extra_kwargs = {"password": {"write_only": True}, }


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        # fields = '__all__'
        extra_kwargs = {
            'user': {'validators': []},
            'country': {'validators': [name_validator, ]},
            'contact_person': {'validators': [name_validator, ]},
            'city': {'validators': [name_validator, ]},
            'phone_number': {'validators': [phone_number_validator, ]},
        }
        exclude = ['user']


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(
        max_length=128,
        style={'input_type': 'password'},
    )

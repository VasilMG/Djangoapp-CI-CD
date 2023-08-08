from django.contrib.auth import get_user_model
from rest_framework import serializers

from ExchangeLogistics.accounts.api.validators import name_validator
from ExchangeLogistics.accounts.models import CompanyProfile
from ExchangeLogistics.exchange.api.api_validators import api_date_validator, \
    api_validate_load_size, api_validate_load_weight
from ExchangeLogistics.exchange.models import Offer

UserModel = get_user_model()


class ShortCompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'contact_person', 'company_email', 'phone_number']


class ShortUserProfileDetailsSerializer(serializers.ModelSerializer):
    companyprofile = ShortCompanyDetailsSerializer()

    class Meta:
        model = UserModel
        fields = ['companyprofile']


class ShortOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        exclude = ['company', 'comment', 'created_on']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'


class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        # fields = '__all__'
        exclude = ['company']
        extra_kwargs = {
            'loading_date': {'validators': [api_date_validator, ]},
            'unloading_date': {'validators': [api_date_validator, ]},
            'load_size': {'validators': [api_validate_load_size, ]},
            'weight': {'validators': [api_validate_load_weight, ]},
            'loading_country': {'validators': [name_validator, ]},
            'unloading_country': {'validators': [name_validator, ]},
            'unloading_place': {'validators': [name_validator, ]},
            'loading_place': {'validators': [name_validator, ]},
        }


class UserProfileDetailsApiSerializer(serializers.ModelSerializer):
    companyprofile = ProfileSerializer()
    offer_set = ShortOfferSerializer(many=True)

    class Meta:
        model = UserModel
        fields = ['username', 'companyprofile', 'offer_set']


class UpdateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        exclude = ['company']
        extra_kwargs = {
            'loading_date': {'validators': [api_date_validator, ]},
            'unloading_date': {'validators': [api_date_validator, ]},
            'load_size': {'validators': [api_validate_load_size, ]},
            'weight': {'validators': [api_validate_load_weight, ]},
            'loading_country': {'validators': [name_validator, ]},
            'unloading_country': {'validators': [name_validator, ]},
            'unloading_place': {'validators': [name_validator, ]},
            'loading_place': {'validators': [name_validator, ]},

        }


class CompleteOfferDetailsSerializer(serializers.ModelSerializer):
    company = ShortUserProfileDetailsSerializer()

    class Meta:
        model = Offer
        fields = '__all__'



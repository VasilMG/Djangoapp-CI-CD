from rest_framework import serializers

from ExchangeLogistics.common.models import PrimaryService, SecondaryService, Location, AboutData


class PrimaryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryService
        fields = '__all__'

class SecondaryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryService
        fields = '__all__'



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class AboutDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutData
        fields = '__all__'

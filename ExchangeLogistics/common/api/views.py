from rest_framework import generics as rest_views

from ExchangeLogistics.common.api.serializers import PrimaryServiceSerializer, SecondaryServiceSerializer,\
    LocationSerializer, AboutDataSerializer
from ExchangeLogistics.common.models import PrimaryService, SecondaryService, Location, AboutData


class IndexPrimaryServicesApiView(rest_views.ListAPIView):
    queryset = PrimaryService.objects.all()
    serializer_class = PrimaryServiceSerializer

class IndexSecondaryServicesApiView(rest_views.ListAPIView):
    queryset = SecondaryService.objects.all()
    serializer_class = SecondaryServiceSerializer

class LocationsApiView(rest_views.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AboutDataApiView(rest_views.ListAPIView):
    queryset = AboutData.objects.all()
    serializer_class = AboutDataSerializer
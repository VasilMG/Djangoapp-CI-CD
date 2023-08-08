from django.urls import path

from ExchangeLogistics.common.api.views import IndexPrimaryServicesApiView, IndexSecondaryServicesApiView, \
    LocationsApiView, AboutDataApiView

urlpatterns = [
    path('index/primary/', IndexPrimaryServicesApiView.as_view(), name='api_primary'),
    path('index/secondary/', IndexSecondaryServicesApiView.as_view(), name='api_secondary'),
    path('locations/', LocationsApiView.as_view(), name='api_locations'),
    path('about/', AboutDataApiView.as_view(), name='api_about'),
]


from django.urls import path

from ExchangeLogistics.common.views import index, services, network, about, settings_view,\
    primary_services_view, secondary_services_view, locations_view, about_data_view, create_primary_service_view, \
    edit_primary_view, delete_primary_view, create_secondary_service_view, edit_secondary_view, delete_secondary_view,\
    create_location_view, edit_location_view, delete_location_view, create_about_view, edit_about_view,\
    delete_about_view

urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services_main'),
    path('newtwork/', network, name='network'),
    path('about/', about, name='about'),
    path('settings/', settings_view, name='settings'),
    path('settings/primary/', primary_services_view, name='primary_services'),
    path('settings/secondary/', secondary_services_view, name='secondary_services'),
    path('settings/locations/', locations_view, name='locations'),
    path('settings/about/', about_data_view, name='about_data'),
    path('settings/primary/create/', create_primary_service_view, name='create_primary'),
    path('settings/primary/<int:pk>/edit/', edit_primary_view, name='edit_primary'),
    path('settings/primary/<int:pk>/delete/', delete_primary_view, name='delete_primary'),
    path('settings/secondary/create/', create_secondary_service_view, name='create_secondary'),
    path('settings/secondary/<int:pk>/edit/', edit_secondary_view, name='edit_secondary'),
    path('settings/secondary/<int:pk>/delete/', delete_secondary_view, name='delete_secondary'),
    path('settings/locations/create/', create_location_view, name='create_location'),
    path('settings/locations/<int:pk>/edit/', edit_location_view, name='edit_location'),
    path('settings/locarions/<int:pk>/delete/', delete_location_view, name='delete_location'),
    path('settings/about/create/', create_about_view, name='create_about'),
    path('settings/about/<int:pk>/edit/', edit_about_view, name='edit_about'),
    path('settings/about/<int:pk>/delete/', delete_about_view, name='delete_about'),
]
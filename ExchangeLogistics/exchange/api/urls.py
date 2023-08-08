from django.urls import path

from ExchangeLogistics.accounts.api.views import UpadateUserProfileApiView
from ExchangeLogistics.exchange.api.views import ProfileDetailsApiView, ViewDetailsDeleteUserProfileApiView, \
    CreateOfferApiView, \
    UpdateOfferApiView, DeleteOfferApiView, ListOffersApiView
urlpatterns = [
    path('<int:pk>/profile', ProfileDetailsApiView.as_view(), name='api_profile_details'),
    path('<int:pk>/profile/edit/', UpadateUserProfileApiView.as_view(), name='api_edit_profile'),
    path('<int:pk>/profile/delete/', ViewDetailsDeleteUserProfileApiView.as_view(), name='api_view_delete_profile'),

    path('<int:pk>/create-offer/', CreateOfferApiView.as_view(), name='api_create_offer'),
    path('offers/', ListOffersApiView.as_view(), name='api_offers_list'),
    path('offers/<int:pk>/edit/', UpdateOfferApiView.as_view(), name='api_offer_edit'),
    path('offers/<int:pk>/details/', DeleteOfferApiView.as_view(), name='api_delete_offer'),
]

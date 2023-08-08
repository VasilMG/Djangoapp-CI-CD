from django.urls import path, include

from ExchangeLogistics.exchange.views import CompanyProfileView, create_offer, OfferDetails, ListOffers, EditOffer, \
    EditCompanyProfileView, DeleteProfile, confirmation_delete_profile, delete_offer, support

urlpatterns = [
    path('<int:pk>/profile/',
         CompanyProfileView.as_view(template_name='exchange/company_profile.html'), name='profile_details_company'),
    path('<int:pk>/profile/edit/', EditCompanyProfileView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/delete/', DeleteProfile.as_view(), name='delete_profile'),
    path('<int:pk>/profile/delete/confirmation/', confirmation_delete_profile, name='confirm_delete'),

    path('<int:pk>/new-offer/', create_offer, name='create_offer'),
    path('offers/<int:pk>/offer-details/', OfferDetails.as_view(), name='offer_details'),
    path('offers/<int:pk>/offer-details/delete/', delete_offer, name='delete_offer'),
    path('offers/<int:pk>/offers-list/', ListOffers.as_view(), name='list_offers'),
    path('offers/<int:pk>/edit/', EditOffer.as_view(), name='edit_offer'),
    path('support/', support, name='support'),

]

from django.urls import path

from ExchangeLogistics.accounts.views import CreateCustomUserView, UpdateCompanyProfileView, login_view, \
    logout_view

urlpatterns = [
    path('sign-in/', login_view, name='sign_in'),
    path('sign-up/', CreateCustomUserView.as_view(), name='register'),
    path('sign-up/<int:pk>/create-profile/',
         UpdateCompanyProfileView.as_view(template_name='accounts/sign_up_profile.html'), name='create_main_profile'),
    path('logout/', logout_view, name='logout'),

]

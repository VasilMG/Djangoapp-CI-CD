from django.urls import path

from ExchangeLogistics.accounts.api.views import CreateUserApiView, UpadateUserProfileApiView, LoginUserApiView

urlpatterns = [
    path('register/', CreateUserApiView.as_view(), name='api_register'),
    path('<int:pk>/profile/', UpadateUserProfileApiView.as_view(), name='api_update_profile'),
    path('login/', LoginUserApiView.as_view(), name='api_login'),
]

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ExchangeLogistics.common.urls')),
    path('exchange/', include('ExchangeLogistics.exchange.urls')),
    path('accounts/', include('ExchangeLogistics.accounts.urls')),

    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'api_schema'},
    ), name='swagger-ui'),
    path('api-schema/', get_schema_view(title='API schema', description='Path to API schema'), name='api_schema'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-common/', include('ExchangeLogistics.common.api.urls')),
    path('api-accounts/', include('ExchangeLogistics.accounts.api.urls')),
    path('api-exchange/', include('ExchangeLogistics.exchange.api.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

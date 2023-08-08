from django.contrib import admin

from ExchangeLogistics.common.models import PrimaryService, SecondaryService,  Location, AboutData


@admin.register(PrimaryService)
class ServicesDataAdmin(admin.ModelAdmin):
    list_display = ['service_type']

@admin.register(SecondaryService)
class ServicesDataAdmin(admin.ModelAdmin):
    list_display = ['service_type']

@admin.register(Location)
class NetworkDataAdmin(admin.ModelAdmin):
    list_display = ['country']


@admin.register(AboutData)
class AboutDataAdmin(admin.ModelAdmin):
    pass

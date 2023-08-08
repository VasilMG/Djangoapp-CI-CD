from django.contrib import admin

from ExchangeLogistics.exchange.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'company']

# @admin.register(Support)
# class SupportAdmin(admin.ModelAdmin):
#     list_display = ['support_email', 'phone_number']

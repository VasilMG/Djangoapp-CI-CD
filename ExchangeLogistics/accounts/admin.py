from django.contrib import admin
from django.contrib.auth import get_user_model

from ExchangeLogistics.accounts.models import CustomUser, CompanyProfile
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'password', 'is_staff']
    list_filter = ('username',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'is_staff', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'company_name', 'country', 'company_email']
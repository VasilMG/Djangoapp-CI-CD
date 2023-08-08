from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ExchangeLogistics.accounts.managers import AppUSerManager
from ExchangeLogistics.exchange.validators import name_validator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    REQUIRED_FIELDS = []

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)

    objects = AppUSerManager()

    USERNAME_FIELD = "username"


UserModel = get_user_model()


class CompanyProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, validators=(name_validator,),)
    city = models.CharField(max_length=50, validators=(name_validator,),)
    address = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=100, validators=(name_validator,),)
    company_email = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        validators=(EmailValidator(),)
    )
    phone_number = models.CharField(
        max_length=20,
    )
    logo = models.ImageField(
        upload_to='logos',
        blank=True,

    )

    def __str__(self):
        return f'{self.company_name}'

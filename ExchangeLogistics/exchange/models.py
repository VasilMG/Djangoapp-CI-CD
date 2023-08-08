from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models

from ExchangeLogistics.exchange.validators import date_validator, validate_load_size, validate_load_weight, \
    phone_number_validator, validate_price

UserModel = get_user_model()


class Offer(models.Model):
    TYPES = (('Freight', 'Freight'), ('Truck space', 'Truck space'))
    created_on = models.DateTimeField(auto_now_add=True)
    offer_type = models.CharField(
        max_length=50,
        choices=TYPES,
        default='Freight'
    )
    loading_date = models.DateField()
    loading_country = models.CharField(max_length=50)
    loading_place = models.CharField(max_length=50)
    load_size = models.DecimalField(
        validators=((validate_load_size,)),
        max_digits=4,
        decimal_places=2,
        help_text='Value between 0 and 15 meters.'
    )
    weight = models.DecimalField(validators=((validate_load_weight,)),
                                 max_digits=4,
                                 decimal_places=2,
                                 help_text='Value between 0 and 28 tons.',
                                 )
    unloading_date = models.DateField(validators=(date_validator,))
    unloading_country = models.CharField(max_length=50)
    unloading_place = models.CharField(max_length=50)
    company = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    comment = models.TextField(blank=True, null=True)

    price = models.DecimalField(validators=((validate_price,)),
                                 max_digits=6,
                                 decimal_places=2,
                                verbose_name='Price in EURO',
                                null=True,
                                blank=True,
                                 )

    def __str__(self):
        return f"{self.created_on} -- {self.company}"


# class Support(models.Model):
#     short_text = models.TextField()
#     support_email = models.EmailField(
#         validators=[EmailValidator, ]
#     )
#     phone_number = models.CharField(
#         max_length=100,
#         validators=[phone_number_validator, ]
#     )
#
#     def __str__(self):
#         return f'{self.support_email} - {self.phone_number}'

    # def clean(self):
    #     main_services= len(Support.objects.all())
    #     if main_services == 3:
    #         raise ValidationError("There must be maximum 3 main services")
    #     return True
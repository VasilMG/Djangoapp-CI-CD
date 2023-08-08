from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models

from ExchangeLogistics.exchange.validators import phone_number_validator, name_validator


class PrimaryService(models.Model):

    service_type = models.CharField(max_length=100, verbose_name='Service Type',)

    short_text = models.CharField(max_length=300, verbose_name='Short Text',)

    long_text = models.TextField(verbose_name='Long text')

    contact_person = models.CharField(max_length=200, verbose_name='Contact person', validators=(name_validator,),)

    general_email = models.EmailField(verbose_name="Email")

    phone_number = models.CharField(max_length=25, verbose_name='Phone number', validators=(phone_number_validator,),)

    background_picture = models.ImageField(
        upload_to='service_images',
        verbose_name='Slide picture',
    )

    def __iter__(self):
        for field_name in self._meta.get_fields():
            value = getattr(self, field_name.attname, None)
            yield field_name.verbose_name, value

    def __str__(self):
        return f"{self.service_type}"


class SecondaryService(models.Model):
    class Meta:
        verbose_name_plural = 'Secondary Services'

    service_type = models.CharField(max_length=100, verbose_name='Service type',)

    short_text = models.CharField(max_length=300, verbose_name='Short text',)

    long_text = models.TextField(verbose_name='Long text',)

    contact_person = models.CharField(max_length=200, verbose_name='Contact person',validators=(name_validator,),)

    general_email = models.EmailField(verbose_name="Email")

    phone_number = models.CharField(
        max_length=25,
        verbose_name='Phone number',
        validators=(phone_number_validator,),
    )

    icon = models.ImageField(
        upload_to='icons',
        verbose_name='Icon',
    )

    def __iter__(self):
        for field_name in self._meta.get_fields():
            value = getattr(self, field_name.attname, None)
            yield field_name.verbose_name, value

    def __str__(self):
        return f"{self.service_type}"


class Location(models.Model):

    country = models.CharField(max_length=50, verbose_name='Country',validators=(name_validator,),)
    city = models.CharField(max_length=50, verbose_name='City', validators=(name_validator,),)
    address = models.CharField(max_length=200, verbose_name='Address',)
    contact_email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=25, verbose_name='Phone number', validators=(phone_number_validator,),)

    def __iter__(self):
        for field_name in self._meta.get_fields():
            value = getattr(self, field_name.attname, None)
            yield field_name.verbose_name, value

    def __str__(self):
        return f'{self.country}: {self.city}'


class AboutData(models.Model):
    class Meta:
        verbose_name_plural = 'About Data'

    history = models.TextField(verbose_name='History',)
    exchange_introduction = models.TextField(verbose_name='Exchange intro',)

    support_text = models.TextField(blank=True, null=True)
    support_email = models.EmailField(
        validators=[EmailValidator, ]
    )
    support_phone_number = models.CharField(
        max_length=100,
        validators=[phone_number_validator, ]
    )

    def __iter__(self):
        for field_name in self._meta.get_fields():
            value = getattr(self, field_name.attname, None)
            yield field_name.verbose_name, value


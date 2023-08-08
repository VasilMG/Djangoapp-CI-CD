import datetime
from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from ExchangeLogistics.accounts.utils import BaseTestCase
from ExchangeLogistics.exchange.forms import CreateOfferForm
from ExchangeLogistics.exchange.models import Offer
from ExchangeLogistics.exchange.validators import date_validator, validate_load_size, validate_load_weight, \
    phone_number_validator

UserModel = get_user_model()

'''Test offer form'''


class TestOfferForm(BaseTestCase):

    def test_offer_form_when_data_is_valid_expect_created_offer(self):

        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        user = self.create_user()

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10.5,
            'weight': 10.5,
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        response = self.client.post(reverse('create_offer', kwargs={'pk': 1}), data=entered_data)

        self.assertIsNotNone(Offer.objects.get(pk=1))

    def test_offer_form_when_loading_date_is_in_the_past_expect_error(self):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        user = self.create_user()

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': yesterday,
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10.5,
            'weight': 10.5,
            'unloading_date': datetime.date.today(),
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        form = CreateOfferForm(entered_data)
        self.assertIn('Date cannot be in the past.', form.errors['loading_date'])

    def test_offer_form_when_unloading_date_is_in_the_past_expect_error(self):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        user = self.create_user()

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10.5,
            'weight': 10.5,
            'unloading_date': yesterday,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        form = CreateOfferForm(entered_data)
        self.assertIn('Date cannot be in the past.', form.errors['unloading_date'])

    def test_offer_form_when_unloading_date_is_before_loading_date_expect_error(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        user = self.create_user()

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': tomorrow,
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10.5,
            'weight': 10.5,
            'unloading_date': datetime.date.today(),
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        form = CreateOfferForm(entered_data)
        self.assertIn('The unloading date cannot be before the loading date', form.errors['unloading_date'])

    def test_offer_form_when_load_size_greater_than_15__expect_error(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        user = self.create_user()

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 16,
            'weight': 10.5,
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        form = CreateOfferForm(entered_data)
        self.assertIn('Value must be between 0 and 15 meters', form.errors['load_size'])

    def test_offer_form_when_load_size_less_than_0__expect_error(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        user = self.create_user()

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),  # current date 17.03.2023
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': -1,
            'weight': 10.5,
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        form = CreateOfferForm(entered_data)
        self.assertIn('Value must be between 0 and 15 meters', form.errors['load_size'])

    def test_offer_form_when_load_weight_less_than_0__expect_error(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        user = self.create_user()

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10,
            'weight': -1,
            'unloading_date':tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        form = CreateOfferForm(entered_data)
        self.assertIn('Value must be between 0 and 28 tons', form.errors['weight'])

    def test_offer_form_when_load_weight_greater_than_28__expect_error(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        user = self.create_user()


        entered_data = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10,
            'weight': 29,
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        form = CreateOfferForm(entered_data)
        self.assertIn('Value must be between 0 and 28 tons', form.errors['weight'])


''' Views tests'''


class TestCreateOfferView(BaseTestCase):

    def test_create_offer_view_when_data_is_valid_expect_redirect_to_offer_details(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        user = self.create_user()

        self.client.login(username=user.username, password=user.password)

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10,
            'weight': 20,
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        response = self.client.post(reverse('create_offer', kwargs={'pk': 1}), data=entered_data)
        redirect_url = f'/exchange/offers/1/offer-details/'
        self.assertEqual(redirect_url, response.headers.get('Location'))

    def test_create_offer_view_when_data_is_not_valid_expect_reverse_status_404(self):
        user = self.create_user()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        self.client.login(username=user.username, password=user.password)

        entered_data = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10,
            'weight': 29, # not valid
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        response = self.client.post(reverse('create_offer', kwargs={'pk': 1}), data=entered_data)

        self.assertEqual(404, response.status_code)


class TestEditOfferView(BaseTestCase):

    def test_edit_offer_view_when_data_is_valid_expect_redirect_offer_details(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        user = self.create_user()

        self.client.login(username=user.username, password=user.password)

        entered_data1 = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10,
            'weight': 20,
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }
        offer = Offer.objects.create(**entered_data1)

        entered_data2 = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Germany',
            'loading_place': 'Berlin',
            'load_size': 10,
            'weight': 20,
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        response = self.client.post(reverse('edit_offer', kwargs={'pk': 1}), data=entered_data2)
        redirect_url = f'/exchange/offers/1/offer-details/'
        self.assertEqual(redirect_url, response.headers.get('Location'))

    def test_edit_offer_view_when_data_is_not_valid_expect_redirect_with_errors(self):
        user = self.create_user()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        self.client.login(username=user.username, password=user.password)

        entered_data1 = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Bulgaria',
            'loading_place': 'Sofia',
            'load_size': 10,
            'weight': 20,
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }
        offer = Offer.objects.create(**entered_data1)

        entered_data2 = {
            'offer_type': 'Freight',
            'loading_date': datetime.date.today(),
            'loading_country': 'Germany',
            'loading_place': '11',  # incorrect value
            'load_size': 30,  # incorrect value
            'weight': 29,  # incorrect value
            'unloading_date': tomorrow,
            'unloading_country': 'Bulgaria',
            'unloading_place': 'Plovdiv',
            'company': user,
            'comment': '22 pallets',
        }

        response = self.client.post(reverse('edit_offer', kwargs={'pk': 1}), data=entered_data2)

        self.assertIsNotNone(response.context_data['form'].errors)


class TestEditCompanyProfileView(BaseTestCase):

    def test_edit_company_profile_view_when_data_is_correct_expect_redirect_profile_url(self):
        user = self.create_user()

        self.client.login(username=user.username, password=user.password)

        entered_data2 = {
            'company_name': 'New Company Ltd',
            'country': 'Bulgaria',
            'city': 'Sofia',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+359888888888'
        }
        response = self.client.post(reverse('edit_profile', kwargs={'pk': 1}), data=entered_data2)

        redirect_url = f'/exchange/1/profile/'

        self.assertEqual(redirect_url, response.headers.get('Location'))

    def test_edit_company_profile_view_when_data_is_not_correct_expect_redirect_status_404(self):
        user = self.create_user()

        self.client.login(username=user.username, password=user.password)

        entered_data2 = {
            'company_name': 'New Company Ltd',
            'country': 'Bulgaria151',
            'city': 'Sofia5151',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan 15Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+359888888888'
        }
        response = self.client.post(reverse('edit_profile', kwargs={'pk': 1}), data=entered_data2)

        self.assertEqual(404, response.status_code)


'''Test validators'''


class TestDateValidator(TestCase):

    def test_date_validator_when_date_is_in_the_past_expect_error(self):
        value = datetime.date.today() - datetime.timedelta(days=1)
        with self.assertRaises(ValidationError) as ve:
            date_validator(value)
        self.assertIsNotNone(ve.exception)

    def test_date_validator_when_date_is_in_the_future_expect_return_date(self):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        self.assertEqual(tomorrow, date_validator(tomorrow))



class TestValidateLoadSize(TestCase):
    def test_validate_size_when_given_value_is_in_range(self):
        value = 10
        self.assertEqual(value, validate_load_size(value))

    def test_validate_size_when_given_value_is_bigger_than_15_expect_error(self):
        value = 16
        with self.assertRaises(ValidationError) as va:
            validate_load_size(value)
        self.assertEqual('The value should be between 0 and 15.00 meters', str(va.exception.message))

    def test_validate_size_when_given_value_is_less_than_0_expect_error(self):
        value = -1
        with self.assertRaises(ValidationError) as va:
            validate_load_size(value)
        self.assertEqual('The value should be between 0 and 15.00 meters', str(va.exception.message))


class TestValidateLoadWeight(TestCase):

    def test_validate_weight_when_given_value_is_in_range(self):
        value = 10
        self.assertEqual(value, validate_load_weight(value))

    def test_validate_size_when_given_value_is_bigger_than_28_expect_error(self):
        value = 29
        with self.assertRaises(ValidationError) as va:
            validate_load_weight(value)
        self.assertEqual('The value should be between 0 and 28 tons.', str(va.exception.message))

    def test_validate_size_when_given_value_is_less_than_0_expect_error(self):
        value = -1
        with self.assertRaises(ValidationError) as va:
            validate_load_weight(value)
        self.assertEqual('The value should be between 0 and 28 tons.', str(va.exception.message))


class TestPhoneNumberValidator(TestCase):

    def test_phone_validator_when_value_is_correct_expect_return_value(self):
        value = '+359888888888'
        self.assertEqual(value, phone_number_validator(value))

    def test_phone_validator_when_value_does_not_start_with_plus_expect_error(self):
        value = '0359888888888'
        with self.assertRaises(ValidationError) as va:
            phone_number_validator(value)

        self.assertEqual("Phone number must start with '+' followed by 9 up to 15 digits.", str(va.exception.message))

    def test_phone_validator_when_value_has_eight_digits_expect_error(self):
        value = '+35988888'
        with self.assertRaises(ValidationError) as va:
            phone_number_validator(value)

        self.assertEqual("Phone number must start with '+' followed by 9 up to 15 digits.", str(va.exception.message))

    def test_phone_validator_when_value_has_sixteen_digits_expect_error(self):
        value = '+3598888888888888'
        with self.assertRaises(ValidationError) as va:
            phone_number_validator(value)

        self.assertEqual("Phone number must start with '+' followed by 9 up to 15 digits.", str(va.exception.message))

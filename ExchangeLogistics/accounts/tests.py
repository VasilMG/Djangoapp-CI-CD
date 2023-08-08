from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse

from ExchangeLogistics.accounts.forms import CreateCompanyProfileForm
from ExchangeLogistics.accounts.models import CompanyProfile
from ExchangeLogistics.accounts.utils import BaseTestCase

UserModel = get_user_model()

'''Form Tests'''


class TestCreateCompanyAccountForm(BaseTestCase):

    def test_create_blank_profile_when_user_form_valid_expect_created_profile(self):
        user = self.create_user()

        self.assertIsNotNone(CompanyProfile.objects.get(pk=1))

    # invalid credentials not tested since it is a base django form


class TestCreateCompanyProfileForm(BaseTestCase):

    def test_create_profile_form_when_form_is_valid_expect_updated_info(self):
        user = self.create_user()

        entered_data2 = {
            'company_name': 'New Company Ltd',
            'country': 'Bulgaria',
            'city': 'Sofia',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+359888888888'
        }
        self.client.post(reverse('create_main_profile', kwargs={'pk': 1}), data=entered_data2)

        updated_profile = CompanyProfile.objects.get(**entered_data2)
        self.assertIsNotNone(updated_profile)

    def test_create_profile_form_when_form_country_is_not_valid_expect_error_message(self):
        user = self.create_user()

        entered_data2 = {
            'company_name': 'New Company Ltd',
            'country': 'Bulg123aria',
            'city': 'Sofia',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+359888888888',
        }

        form = CreateCompanyProfileForm(entered_data2)

        self.assertFalse(form.is_valid())
        self.assertIn('Country cannot contain digits.', form.errors['country'])

    def test_create_profile_form_when_form_city_is_not_valid_expect_error_message(self):
        user = self.create_user()

        entered_data2 = {

            'company_name': 'New Company Ltd',
            'country': 'Bulgaria',
            'city': 'Sofia123',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+359888888888',
        }

        form = CreateCompanyProfileForm(entered_data2)

        self.assertFalse(form.is_valid())
        self.assertIn('City cannot contain digits.', form.errors['city'])

    def test_create_profile_form_when_form_contact_person__is_not_valid_expect_error_message(self):
        user = self.create_user()

        entered_data2 = {

            'company_name': 'New Company Ltd',
            'country': 'Bulgaria',
            'city': 'Sofia',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan1215 Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+359888888888',
        }

        form = CreateCompanyProfileForm(entered_data2)

        self.assertFalse(form.is_valid())
        self.assertIn('The name cannot contain digits.', form.errors['contact_person'])

    def test_create_profile_form_when_form_phone_number_doesnt_start_with_plus__expect_error_message(self):
        user = self.create_user()

        entered_data2 = {

            'company_name': 'New Company Ltd',
            'country': 'Bulgaria',
            'city': 'Sofia',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '09888888888',
        }

        form = CreateCompanyProfileForm(entered_data2)

        self.assertFalse(form.is_valid())
        self.assertIn("Value must start with '+' followed by 9 up to 15 digits.", form.errors['phone_number'])

    def test_create_profile_form_when_form_phone_number_contains_more_than_15_digits__expect_error_message(self):
        user = self.create_user()

        entered_data2 = {
            # 'user_id': 1,
            'company_name': 'New Company Ltd',
            'country': 'Bulgaria',
            'city': 'Sofia',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+9888888888000000',
        }

        form = CreateCompanyProfileForm(entered_data2)

        self.assertFalse(form.is_valid())
        self.assertIn("Value must start with '+' followed by 9 up to 15 digits.", form.errors['phone_number'])

    def test_create_profile_form_when_form_phone_number_contains_less_than_9_digits__expect_error_message(self):
        user = self.create_user()

        entered_data2 = {

            'company_name': 'New Company Ltd',
            'country': 'Bulgaria',
            'city': 'Sofia',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+98888888',
        }

        form = CreateCompanyProfileForm(entered_data2)

        self.assertFalse(form.is_valid())
        self.assertIn("Value must start with '+' followed by 9 up to 15 digits.", form.errors['phone_number'])


'''Veiw tests'''


class TestCreateCustomUserView(TestCase):

    def test_create_user_view_when_data_is_valid_expect_redirect_to_user_profile(self):
        entered_data1 = {
            'username': 'newuser1',
            'password1': '3048lask',
            'password2': '3048lask',
        }
        response = self.client.post(reverse('register'), data=entered_data1)

        redirect_url = f'/accounts/sign-up/1/create-profile/'
        self.assertEqual(redirect_url, response.headers.get('Location'))


class TestUpdateCompanyProfileView(BaseTestCase):

    def test_update_company_profile_view_when_data_is_valid_expect_redirect_to_profile_details(self):
        user = self.create_user()

        entered_data2 = {
            'company_name': 'New Company Ltd',
            'country': 'Bulgaria',
            'city': 'Sofia',
            'address': 'bul.Bulgaria 35',
            'contact_person': 'Ivan Ivanov',
            'company_email': 'ivan@new.com',
            'phone_number': '+359888888888'
        }
        response = self.client.post(reverse('create_main_profile', kwargs={'pk': 1}), data=entered_data2)

        redirect_url = f'/exchange/1/profile/'

        self.assertEqual(redirect_url, response.headers.get('Location'))


class TestLoginView(BaseTestCase):

    def test_login_view_when_data_is_valid(self):
        user = self.create_user()

        entered_data = {
            'username': 'newuser1',
            'password': '3048lask'
        }

        response = self.client.post(reverse('sign_in'), data=entered_data)

        redirect_url = f'/exchange/1/profile/'
        self.assertEqual(redirect_url, response.headers.get('Location'))

    def test_login_view_when_data_is_not_valid(self):
        user = self.create_user()

        entered_data = {
            'username': 'newuser123',
            'password': '3048lask'
        }

        response = self.client.post(reverse('sign_in'), data=entered_data)

        self.assertEqual(404, response.status_code)

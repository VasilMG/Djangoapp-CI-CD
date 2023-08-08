from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()

class BaseTestCase(TestCase):
    def create_user(self):
        entered_data1 = {
            'username': 'newuser1',
            'password1': '3048lask',
            'password2': '3048lask',
        }
        self.client.post(reverse('register'), data=entered_data1)
        user = UserModel.objects.get(pk=1)
        return user


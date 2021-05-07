from django.test import TestCase
from django.urls import reverse

from ..models import User


class TestSigninView(TestCase):

    url = reverse('access')

    @classmethod
    def setUpTestData(cls):

        User.objects.create_user(username='dorothy',
                                 email='dot@kansas.gov',
                                 is_active=True,
                                 password='rubySlippers')

    def test_access_page(self):
        response = self.client.post(self.url,
                                    {'username': 'dorothy',
                                     'password': 'rubySlippers'})
        # dorothy has no user profile; redirect to profile page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('profile'))

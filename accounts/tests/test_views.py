from django.test import TestCase
from django.urls import reverse

from ..models import User, UserProfile


class TestSigninView(TestCase):

    url = reverse('access')

    @classmethod
    def setUpTestData(cls):

        cls.usr1 = User.objects.create_user(username='dorothy',
                                            email='dot@kansas.gov',
                                            is_active=True,
                                            password='rubySlippers')
        cls.usr2 = User.objects.create_user(username='evillene',
                                            email='queen@theWest.gov',
                                            is_active=True,
                                            password='flyingMonkeys')
        UserProfile(user=cls.usr2).save()

    def test_access_page(self):
        response = self.client.post(self.url,
                                    {'username': 'dorothy',
                                     'password': 'rubySlippers'})
        # dorothy has no user profile; redirect to profile page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('profile'))

        response = self.client.post(self.url,
                                    {'username': 'evillene',
                                     'password': 'flyingMonkeys'})
        # evillene has a user profile; redirect to home page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home'))


class TestProfileView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.usr1 = User.objects.create_user(username='dorothy',
                                            email='dot@kansas.gov',
                                            is_active=True,
                                            password='rubySlippers')
        cls.usr2 = User.objects.create_user(username='evillene',
                                            email='deadbeef',
                                            is_active=True,
                                            password='flyingMonkeys')
        UserProfile(user=cls.usr2).save()

    the_url = reverse('profile')
    template = 'accounts/profile.html'

    def test_get(self):

        self.client.force_login(self.usr1)
        response = self.client.get(self.the_url)
        self.assertEqual(response.status_code, 200, "get should succeed")

        bgn = response.content.find(b'id_email')
        end = response.content.find(b'</p>', bgn)
        self.assertIn(self.usr1.email,
                      response.content[bgn:end].decode(),
                      'email should display on page')

    def test_get_with_kludge(self):

        self.client.force_login(self.usr2)
        response = self.client.get(self.the_url)
        self.assertEqual(response.status_code, 200, "get should succeed")

    def test_post(self):

        self.client.force_login(self.usr1)
        response = self.client.post(self.the_url, location='kansas')
        self.assertIn(b'<p>Successfully saved.</p>', response.content,
                      "'Success' message should be visible")

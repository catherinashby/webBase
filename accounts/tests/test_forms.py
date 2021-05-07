import string

from django.test import TestCase

from ..forms import CustomUserCreationForm


class UserCreationFormTest(TestCase):

    def test_default_password_kludge(self):
        form = CustomUserCreationForm(data={'username': 'evillene',
                                            'password1': 'brandNewDay',
                                            'password2': 'brandNewDay'})
        user = form.save(commit=False)
        self.assertTrue(set(user.email).issubset(string.hexdigits),
                        "kludge should set email equal to hexstring")
        self.assertIsNone(user.pk, "Shouldn't be saved to db yet")
        user = form.save(commit=True)
        self.assertIsNotNone(user.pk, "Should be saved to db now")
        return

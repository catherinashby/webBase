from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # kludge to get past unique constraint of email address:
        # number of seconds since Day One, converted to hexstring
        interval = (datetime.now() - datetime(1, 1, 1)).total_seconds()
        user.email = hex(int(interval))[2:]
        user.is_active = True
        if commit:
            user.save()
        return user


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['user']

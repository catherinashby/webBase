from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('access')
    template_name = 'accounts/signup.html'


class SigninView(LoginView):
    profile_url = reverse_lazy('profile')
    template_name = 'accounts/access.html'

    def get_success_url(self):
        usr = self.request.user

        firstTimer = True
        if hasattr(usr, 'userprofile'):
            firstTimer = False

        url = self.profile_url if firstTimer else super().get_success_url()
        return url

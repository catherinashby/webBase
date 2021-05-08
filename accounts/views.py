from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView

from .forms import CustomUserCreationForm, UserForm, ProfileForm


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


@method_decorator(login_required, name='dispatch')
class ProfileView(FormView):

    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        if request.user.email.find('@') == -1:
            request.user.email = None
        user_form = UserForm(instance=request.user)
        if hasattr(request.user, 'userprofile'):
            profile_form = ProfileForm(instance=request.user.userprofile)
        else:
            gdef = ProfileForm.Meta.model.gender.field.default
            profile_form = ProfileForm({'user': request.user,
                                        'gender': gdef})
        self.extra_context = {'userform': user_form, 'form': profile_form}
        return super().get(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = self.get_form()
        self.extra_context = {'userform': user_form, 'form': profile_form}
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.instance.user = user_form.save()
            profile_form.save()
            self.extra_context['saved'] = True
        # always return to the profile form
        return self.form_invalid(profile_form)

"""Module adding views to accounts app."""
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, RedirectView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str # force_text on older versions of Django

from .forms import SignUpForm, token_generator, user_model

# Create your views here.
class SignUpView(CreateView):
    """Class representing the SignUp view for users"""

    form_class = SignUpForm
    success_url = reverse_lazy('accounts:check_email')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        to_return = super().form_valid(form)

        user = form.save()
        user.is_active = False # Turns the user status to inactive
        user.save()

        form.send_activation_email(self.request, user)

        return to_return


class ActivateView(RedirectView):
    """Class representing the Activate view for users"""

    url = reverse_lazy('accounts:success')

    # Custom get method
    def get(self, request, uidb64=None, token=None):

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = user_model.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return super().get(request, uidb64, token)
        else:
            return render(request, 'accounts/activate_account_invalid.html')


class CheckEmailView(TemplateView):
    """Class representing the view for users to check their email for validation"""

    template_name = 'accounts/check_email.html'


class SuccessView(TemplateView):
    """Class representing the view for users after verification email link success"""

    template_name = 'accounts/success.html'

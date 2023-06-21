from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives

from .forms import SignUpForm

class SignUpView(CreateView):
    """
    Allow the User to Create a New Account
    """
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('habits:home')
    # If the form is valid it directly login the user and redirect him to the blog.

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        self.send_welcome_email(user=user)
        return to_return

    def send_welcome_email(self, user):
        msg= EmailMessage(
            f"{user.get_username().capitalize()} Te has registrado en SIMA!",
            f"""<h1> Hola {user.first_name} {user.last_name}! <h1/> <p>Te has registrado en SIMA estamos contentos por ello<p>
            <p>Ya puedes comenzar a usar todas las funcionalidades de SIMA</p>
            """,
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        msg.content_subtype = "html"
        msg.send()
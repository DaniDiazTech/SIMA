from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views




class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Correo', 'class': 'form-control bg-white border-left-0 border-md'}))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Usuario', 'class': 'form-control bg-white border-left-0 border-md'}))
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'placeholder': 'Nombres', 'class': 'form-control bg-white border-left-0 border-md'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'placeholder': 'Apellidos', 'class': 'form-control bg-white border-left-0 border-md'}))

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", 
                  "email", "username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # self.fields["username"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'

        # First password
        self.fields["password1"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-sm'
        self.fields["password1"].widget.attrs["placeholder"] = 'Contraseña'

        # Password confirmation
        self.fields["password2"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'
        self.fields["password2"].widget.attrs["placeholder"] = 'Confirmar'

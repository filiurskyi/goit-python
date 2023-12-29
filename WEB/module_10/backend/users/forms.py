from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

form_style = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": form_style}))
    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(attrs={"class": form_style})
    )
    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(attrs={"class": form_style})
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "class": form_style}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": form_style}),
    )
    class Meta:
        model = User
        fields = ['username', 'password']
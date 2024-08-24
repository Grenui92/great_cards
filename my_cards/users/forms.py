from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """User registration form.

    The class has the following attributes:
    
    - username (str): User's username.
    - email (str): User's email.
    - password1 (str): User's password.
    - password2 (str): User's password confirmation.
    """

    username = forms.CharField(max_length=20,
                               required=True,
                               widget=forms.TextInput())

    email = forms.CharField(max_length=255,
                            required=True,
                            widget=forms.TextInput())

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        """Meta class for RegistrationForm."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']

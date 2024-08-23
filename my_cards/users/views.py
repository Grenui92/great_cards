from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView, LoginView, LogoutView
from django.views import View
from django.urls import reverse_lazy

from .forms import RegistrationForm


class MyRegistrationView(View):
    """Class for user registration."""

    def post(self, request):
        """Register a new user. Redirect to the main page if the form is valid.
        Render the registration page with the form if the form is not valid.

        :param request: request object
        :return: render or redirect
        """
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(to='news:main')
        return render(request, 'users/signup.html', context={'form': form})

    def get(self, request):
        """Render the registration page with the form.

        :param request: request object
        :return: render
        """
        return render(request,
                      'users/signup.html',
                      context={'form': RegistrationForm()})


class MyLoginView(LoginView):
    """LogIn class.

    Attributes:
        template_name (str): The name of the template.
        next_page (str): The URL to redirect to after a successful login.
    """

    template_name = 'users/login.html'
    next_page = reverse_lazy('news:main')


class MyLogoutView(LogoutView):
    """LogOut class.

    Attributes:
        next_page (str): The URL to redirect to after a successful logout.
    """

    next_page = reverse_lazy('news:main')


class MyResetPasswordView(PasswordResetView):
    """Class for reset password.

    Attributes:
        template_name (str): The name of the template.
        email_template_name (str): The name of the email template.
        html_email_template_name (str): The name of the html email template.
        success_url (str): The URL to redirect to after a successful
        password reset.
        success_message (str): The message that will be displayed after a
        successful password reset.
        subject_template_name (str): The name of the subject template.
    """

    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = """An email with instructions to reset your
                        password has been sent to %(email)s."""
    subject_template_name = 'users/password_reset_subject.txt'

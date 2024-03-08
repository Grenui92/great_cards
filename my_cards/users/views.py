import logging

from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView, LoginView, LogoutView
from django.views import View
from django.urls import reverse_lazy

from .forms import RegistrationForm


class MyRegistrationView(View):

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect(to='news:main')
        return render(request, 'users/signup.html', context={'form': form})

    def get(self, request):
        return render(request, 'users/signup.html', context={'form': RegistrationForm()})


class MyLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('news:main')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('news:main')


class MyResetPasswordView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'

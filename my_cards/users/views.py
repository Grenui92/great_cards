import logging

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, LoginForm
from .massages import NOT_VALID_USER
from cards.models import CardsCollections

# from my_cards.cards.models import CardsCollections


def user_signup(request):
    if request.user.is_authenticated:
        redirect(to='cards:main')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            user = form.save()

            collection_1 = CardsCollections.objects.create(name='main', owner=user)
            collection_2 = CardsCollections.objects.create(name='other', owner=user)
            logging.info(f'User -{user}- created')
            return redirect(to='cards:main')

    return render(request, 'users/signup.html', context={'form': RegistrationForm()})

def user_login(request):
    if request.user.is_authenticated:
        return redirect(to='cards:main')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            logging.info(f'Wrong information for user -{username}-')
            return render(request, 'users/login.html', context={'message': NOT_VALID_USER, 'form': LoginForm()})
        login(request, user)
        logging.info(f'User -{username}- login')
        return redirect(to='cards:main')

    return render(request, 'users/login.html', context={'form': LoginForm()})

@login_required
def user_logout(request):
    logging.info(f'User -{request.user.id}- logout')
    logout(request)
    return redirect(to='cards:main')
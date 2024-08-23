import re

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from users.forms import RegistrationForm


def user_login(request, created_user=None):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    token, *_ = Token.objects.get_or_create(user=user)

    if user is not None:
        login(request, user)

        return {'message': 'Sucessfully log',
                'username': user.username,
                'email': user.email,
                'id': user.id,
                'token': token.key}
    else:
        return {'message': 'Wrong credentials'}


def user_create(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        form.save()
        return {'message': f'User {form.data["username"]} succesfully registred'}
    return {'message': 'Wrong credentials.'}


def parse_promt(text):
    pattern = re.compile(r'\d{2}:\d{2}:\d{2}')
    new_text = pattern.sub('', text)
    return new_text

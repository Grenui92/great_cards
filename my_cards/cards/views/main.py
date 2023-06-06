import logging

from django.shortcuts import render


def main(request):
    if request.method == 'GET':
        logging.info(f'Open main page. User -{request.user.id}-')
        return render(request, 'cards/index.html')
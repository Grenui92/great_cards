import logging

from django.shortcuts import render


def main(request):
    """
    The main function is the main page of the site.
    It displays a list of all cards in the database, and allows you to add new ones.

    :param request: Get the request object
    :return: The main page
    """
    if request.method == 'GET':
        logging.info(f'Open main page. User -{request.user.id}-')
        return render(request, 'cards/index.html')
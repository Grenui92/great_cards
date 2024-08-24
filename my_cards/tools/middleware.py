from django.shortcuts import render

from tools.logger import logger


def simple_middleware(get_response):
    """A simple middleware that logs the response."""
    def middleware(request):

        try:
            response = get_response(request)
            return response
        except Exception as exc:
            return render(request,
                          'message.html',
                          context={'message': 'Sorry, something went wrong.'})

    return middleware

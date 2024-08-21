from django.shortcuts import redirect, render
import time

from tools.logger import logger

def simple_middleware(get_response):

    def middleware(request):
        now = time.time()

        try: 
            response = get_response(request)
            logger.info((time.time() - now))
            return response
        except Exception as exc:
            logger.info(exc)
            return render(request, 'message.html', context={'message': 'Sorry, something went wrong.'})

    return middleware
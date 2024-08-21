from django.shortcuts import render
import time

from tools.logger import logger

def simple_middleware(get_response):

    def middleware(request):
        now = time.time()

        try: 
            response = get_response(request)
            logger.debug('Succes')
            logger.debug(response.status_code)
            for k in response.content:
                logger.debug(k)
            return response
        except Exception as exc:
            logger.debug(exc.args)
            return render(request, 'message.html', context={'message': 'Sorry, something went wrong.'})

    return middleware
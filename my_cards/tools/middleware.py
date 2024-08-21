from django.shortcuts import redirect, render

import time
def simple_middleware(get_response):

    def middleware(request):
        now = time.time()

        try: 
            response = get_response(request)
            print(time.time() - now)
            return response
        except:
            return render(request, 'message.html', context={'message': 'Sorry, something went wrong.'})

    return middleware
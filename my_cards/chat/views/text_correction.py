from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View

from chat.services.checking_sentences import text_generator

class CorrectorView(View):

    def post(self, request):
        """
        The post function is called when the user submits a message.
        The function takes in the request and returns a JsonResponse object with
        the response from chatbot_response.

        :param self: Represent the instance of the object itself
        :param request: Get the message from the user
        :return: A json response with the original message and the corrected message
        """

        message = request.POST.get('message')
        chatbot_response = text_generator(message)
        return JsonResponse({'response': f'Original: {message}\n'
                                         f'Correct: {chatbot_response.strip()}'})

    def get(self, request):
        """
        The get function is called when a user navigates to the /chat/text_correction url.
        It renders the text_correction.html template, which contains a form for users to enter text into.

        :param self: Represent the instance of the class
        :param request: Pass the request object to the view
        :return: A rendered template chat/text_correction.html
        """
        return render(request, 'chat/text_correction.html')

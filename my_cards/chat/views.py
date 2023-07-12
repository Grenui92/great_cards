from django.shortcuts import render
from django.views import View

class ChatView(View):

    def get(self, request):
        """
        The get function is used to render the chat_ai.html page, which contains
        the chatbot interface.

        :param self: Represent the instance of the class
        :param request: Get the request object
        :return: The chat_ai.html render
        """
        return render(request, 'chat/chat.html')

class CorrectorView(View):

    def get(self, request):
        """
        The get function is called when a user navigates to the /chat/text_correction url.
        It renders the text_correction.html template, which contains a form for users to enter text into.

        :param self: Represent the instance of the class
        :param request: Pass the request object to the view
        :return: A rendered template chat/text_correction.html
        """
        return render(request, 'chat/corrector.html')

class EnRuTranslateView(View):

    def get(self, request):
        return render(request, 'chat/en_ru_translate.html')

class RuEnTranslateView(View):

    def get(self, request):
        return render(request, 'chat/ru_en_translate.html')
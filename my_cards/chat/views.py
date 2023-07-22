from django.shortcuts import render
from django.views import View

from tools.decorators import class_login_required

class ChatView(View):

    @class_login_required
    def get(self, request):
        """
        The get function is used to render the chat_ai.html page, which contains
        the chatbot interface.

        :param self: Represent the instance of the class
        :param request: Get the request object
        :return: The chat_ai.html render
        """
        return render(request, 'chat/chat_scr.html')

class CorrectorView(View):

    @class_login_required
    def get(self, request):
        """
        The get function is called when a user navigates to the /chat/text_correction url.
        It renders the text_correction.html template, which contains a form for users to enter text into.

        :param self: Represent the instance of the class
        :param request: Pass the request object to the view
        :return: A rendered template chat/text_correction.html
        """
        return render(request, 'chat/corrector_scr.html')

class EnRuTranslateView(View):

    @class_login_required
    def get(self, request):
        return render(request, 'chat/en_ru_translate_scr.html')

class RuEnTranslateView(View):

    @class_login_required
    def get(self, request):
        return render(request, 'chat/ru_en_translate_scr.html')
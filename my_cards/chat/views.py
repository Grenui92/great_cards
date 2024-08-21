from django.shortcuts import render
from django.views import View

from tools.decorators import class_login_required
from tools.logger import logger
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
        
        logger.info('Start')
        return render(request, 'chat/chat_scr.html')
    
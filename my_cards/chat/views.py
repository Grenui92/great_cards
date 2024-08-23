from django.shortcuts import render
from django.views import View

from tools.decorators import class_login_required
from tools.logger import logger


class ChatView(View):
    """The ChatView class is used to render the chat_ai.html page, which
    contains the chatbot interface.
    """

    @class_login_required
    def get(self, request):
        """The get function is used to render the chat_ai.html page, which
        contains the chatbot interface.

        :param request: Get the request object
        :return: render
        """
        logger.info('Chat Start')
        return render(request, 'chat/chat_scr.html')

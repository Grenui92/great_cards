from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from chat.services.conversation import chat_bot

MAX_AI_PHRASES_MEMORY = 20

class ChatView(View):

    def post(self, request, messages=[]):
        """
        The post function is used to handle the POST request from the user.
        It takes in a list of messages, which are stored as dictionaries with two keys: role and content.
        The role key can be either &quot;user&quot; or &quot;system&quot;, while the content key stores a string message.
        The post function then adds another dictionary to this list of messages, containing information about what was posted by the user (role = &quot;user&quot;) and what they wrote (content = whatever they typed).  It then calls text_generator() on this updated list of messages, which returns a tuple containing two strings: response_role and response_

        :param self: Represent the instance of the class
        :param request: Get the message from the user
        :param messages: Store the messages that have been sent to the chatbot
        :return: A jsonresponse object, which is a subclass of httpresponse
        """
        if len(messages) >= MAX_AI_PHRASES_MEMORY:
            messages = messages[1:]
        message = request.POST.get("message", "")

        messages.append({"role": "system",
                         "content": "Show linguistic mistakes in user message."
                                    "Tell about mistakes in message."
                                    "Then answer user request."})
        messages.append({"role": "user", "content": message})

        response_role, response_content = chat_bot(messages)

        messages.append({"role": response_role, "content": response_content})

        return JsonResponse({'response': f'YOU: {message.strip()}<br>'
                                         f'{response_role.upper()}: {response_content.strip()}<br><br>'})

    def get(self, request):
        """
        The get function is used to render the chat_ai.html page, which contains
        the chatbot interface.

        :param self: Represent the instance of the class
        :param request: Get the request object
        :return: The chat_ai.html render
        """
        return render(request, 'chat/chat_ai.html')


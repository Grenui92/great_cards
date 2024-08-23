import json

from channels.generic.websocket import WebsocketConsumer

from chat.services.conversation import chat_bot
from chat.services.checking_sentences import chekicg_sentences
from chat.services.translate import translate_ru_en, translate_en_ru
from tools.logger import logger

MAX_AI_PHRASES_MEMORY = 20


class ChatConsumer(WebsocketConsumer):
    """Websocket consumer for chat."""

    def connect(self):
        """Accept the connection."""
        self.bot_messages = []
        self.accept()

    def disconnect(self, code):
        """Disconnect the user."""
        self.bot_messages = []

    def receive(self, text_data=None, *args, **kwargs):
        """Receive the message from the user and send the response back.

        :param text_data: The message from the user, defaults to None
        """
        logger.info('Chat')
        if len(self.bot_messages) >= MAX_AI_PHRASES_MEMORY:
            self.bot_messages = self.bot_messages[1:]

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.bot_messages.append({"role": "system",
                                  "content": "Show linguistic mistakes in user message."
                                  "Tell about this mistakes in message."
                                  "Then answer user message."})
        self.bot_messages.append({"role": "user", "content": message})

        response_role, response_content = chat_bot(self.bot_messages)

        self.bot_messages.append(
            {"role": response_role, "content": response_content})

        self.send(text_data=json.dumps(
            {'message': f'{response_role.capitalize()}: {response_content} \n \n'}))


class CorrectorConsumer(WebsocketConsumer):
    """Websocket consumer for correcting sentences."""

    def connect(self):
        """Accept the connection."""
        self.accept()

    def disconnect(self, code):
        """Disconnect the user."""
        pass

    def receive(self, text_data=None, *args, **kwargs):
        """Receive the message from the user and send the corrected message.

        :param text_data: The message from the user, defaults to None
        """
        logger.info('Corrector')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        corrector_response = chekicg_sentences(message)

        self.send(text_data=json.dumps(
            {'message': f'Correct: {corrector_response.strip()} \n \n'}))


class RuEnTranslateConsumer(WebsocketConsumer):
    """Websocket consumer for translating Russian to English."""

    def connect(self):
        """Accept the connection."""
        self.accept()

    def disconnect(self, code):
        """Disconnect the user."""
        pass

    def receive(self, text_data=None, *args, **kwargs):
        """Receive the message from the user and send the translated message
        back.

        :param text_data: The message from the user, defaults to None
        :return: None
        """
        logger.info('RuEn')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        corrector_response = translate_ru_en(message)

        self.send(text_data=json.dumps(
            {'message': f'Answer: {corrector_response.strip()} \n \n'}))


class EnRuTranslateConsumer(WebsocketConsumer):
    """Websocket consumer for translating English to Russian."""

    def connect(self):
        """Accept the connection."""
        self.accept()

    def disconnect(self, code):
        """Disconnect the user."""
        pass

    def receive(self, text_data=None, *args, **kwargs):
        """Receive the message from the user and send the translated message
        back.

        :param text_data: The message from the user, defaults to None
        :return: None
        """
        text_data_json = json.loads(text_data)
        logger.debug(text_data_json)
        message = text_data_json['message']

        corrector_response = translate_en_ru(message)

        self.send(text_data=json.dumps(
            {'message': f'Answer: {corrector_response.strip()} \n \n',
             'english': message,
             'russian': corrector_response}))

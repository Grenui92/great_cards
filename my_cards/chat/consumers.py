import json

from channels.generic.websocket import WebsocketConsumer

from chat.services.conversation import chat_bot
from chat.services.checking_sentences import text_generator
from chat.services.translate import translate_ru_en, translate_en_ru
MAX_AI_PHRASES_MEMORY = 20

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.bot_messages = []
        self.accept()

    def disconnect(self, code):
        self.bot_messages = []

    def receive(self, text_data=None, bytes_data=None):
        if len(self.bot_messages) >= MAX_AI_PHRASES_MEMORY:
            self.bot_messages = self.bot_messages[1:]

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.bot_messages.append({"role": "system",
                         "content": "Show linguistic mistakes in user message."
                                    "Tell about this mistakes in message."
                                    "Then answer user request."})
        self.bot_messages.append({"role": "user", "content": message})

        response_role, response_content = chat_bot(self.bot_messages)

        self.bot_messages.append({"role": response_role, "content": response_content})

        self.send(text_data=json.dumps({'message': f'{response_role.capitalize()}:  {response_content} \n \n'}))

class CorrectorConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        corrector_response = text_generator(message)

        self.send(text_data=json.dumps({'message': f'Correct: {corrector_response.strip()} \n \n'}))

class RuEnTranslateConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        corrector_response = translate_ru_en(message)

        self.send(text_data=json.dumps({'message': f'Answer: {corrector_response.strip()} \n \n'}))

class EnRuTranslateConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        corrector_response = translate_en_ru(message)

        self.send(text_data=json.dumps({'message': f'Answer: {corrector_response.strip()} \n \n'}))
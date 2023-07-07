import json

from channels.generic.websocket import WebsocketConsumer

from chat.services.conversation import chat_bot
MAX_AI_PHRASES_MEMORY = 20

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.bot_messages = []
        self.accept()

    def disconnect(self, code):
        self.bot_messages = []

    def receive(self, text_data=None):
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
        print(self.bot_messages)

        self.send(text_data=json.dumps({'message': f'{response_role.capitalize()}:  {response_content}'}))
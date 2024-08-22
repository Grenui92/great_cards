from django.urls import re_path
from .consumers import ChatConsumer, CorrectorConsumer, EnRuTranslateConsumer, RuEnTranslateConsumer
websocket_urlpatterns = [
    re_path('chat_ai/', ChatConsumer.as_asgi()),
    re_path('text_correction/', CorrectorConsumer.as_asgi()),
    re_path('translate_to_en/', RuEnTranslateConsumer.as_asgi()),
    re_path('translate_to_ru', EnRuTranslateConsumer.as_asgi()),
    re_path('ws/translate_to_en/', RuEnTranslateConsumer.as_asgi()),
    re_path('ws/translate_to_ru/', EnRuTranslateConsumer.as_asgi())
]
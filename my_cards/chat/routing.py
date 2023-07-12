from django.urls import re_path
from .consumers import ChatConsumer, CorrectorConsumer, EnRuTranslateConsumer, RuEnTranslateConsumer
websocket_urlpatterns = [
    re_path('chat', ChatConsumer.as_asgi()),
    re_path('corrector', CorrectorConsumer.as_asgi()),
    re_path('translate_to_en', RuEnTranslateConsumer.as_asgi()),
    re_path('translate_to_ru', EnRuTranslateConsumer.as_asgi())
]
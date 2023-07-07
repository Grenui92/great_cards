from django.urls import re_path
from .consumers import ChatConsumer, CorrectorConsumer
websocket_urlpatterns = [
    re_path('chat', ChatConsumer.as_asgi()),
    re_path('corrector', CorrectorConsumer.as_asgi())
]
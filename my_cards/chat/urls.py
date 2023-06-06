from django.urls import path
from .views.text_correction import text_correction
from .views.chat_ai import chat

app_name = 'chat'

urlpatterns = [
    path('text_correction/', text_correction, name='text_correction'),
    path('chat_ai/', chat, name='chat_ai'),
]
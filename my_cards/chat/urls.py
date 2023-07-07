from django.urls import path
from .views.text_correction import CorrectorView
from .views.chat_ai import ChatView
from .views1 import room

app_name = 'chat'

urlpatterns = [
    path('text_correction/', CorrectorView.as_view(), name='text_correction'),
    # path('chat_ai/', ChatView.as_view(), name='chat_ai'),
    path('chat_ai/', room, name='chat_ai'),
]
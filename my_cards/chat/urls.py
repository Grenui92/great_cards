from django.urls import path
from .views import ChatView


app_name = 'chat'

urlpatterns = [
    path('text_correction/', ChatView.as_view(), name='text_correction'),
    path('chat_ai/', ChatView.as_view(), name='chat_ai'),
    path('translate_to_ru/', ChatView.as_view(), name='translate_to_ru'),
    path('translate_to_en/', ChatView.as_view(), name='translate_to_en')
]

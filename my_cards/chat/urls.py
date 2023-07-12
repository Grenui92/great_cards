from django.urls import path
from .views import CorrectorView, ChatView, EnRuTranslateView, RuEnTranslateView



app_name = 'chat'

urlpatterns = [
    path('text_correction/', CorrectorView.as_view(), name='text_correction'),
    path('chat_ai/', ChatView.as_view(), name='chat_ai'),
    path('to_ru_translate/', EnRuTranslateView.as_view(), name='to_ru_translate'),
    path('to_en_translate/', RuEnTranslateView.as_view(), name='to_en_translate')
]
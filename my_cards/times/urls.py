from django.urls import path
from .views import TimesView, DeleteSentenceView
app_name = 'times'

urlpatterns = [
    path('times/', TimesView.as_view(), name='times'),
    path('times/<int:time_id>/', TimesView.as_view(), name='times_post'),
    path('delete_sentence/<int:sentence_id>/',
         DeleteSentenceView.as_view(),
         name='delete_sentence')
]

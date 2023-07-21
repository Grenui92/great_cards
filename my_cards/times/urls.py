from django.urls import path
from .views import TimesView
app_name = 'times'

urlpatterns = [
    path('times/', TimesView.as_view(), name='times')
]

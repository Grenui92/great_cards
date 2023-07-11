from django.urls import path
from news.views import NewsView, NewsListView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='main'),
]
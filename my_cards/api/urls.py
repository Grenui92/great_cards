from django.urls import path
from .views import CollectionsApi, CardsApi

urlpatterns = [
    path('collections/', CollectionsApi.as_view(), name='collections_api'),
    path('cards/', CardsApi.as_view(), name='cards_api')
]



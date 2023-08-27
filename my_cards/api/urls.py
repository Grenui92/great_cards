from django.urls import path, include
from .views import CollectionsApi, CardsApi, LoginApi, LogoutApi

urlpatterns = [
    path('collections/', CollectionsApi.as_view(), name='collections_api'),
    path('cards/', CardsApi.as_view(), name='cards_api'),
    path('auth/login/', LoginApi.as_view(), name='auth_api'),
    path('auth/logout/', LogoutApi.as_view(), name='logout_api')
]



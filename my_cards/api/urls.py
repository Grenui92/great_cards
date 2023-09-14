from django.urls import path, include
from .views import CollectionsApi, CardsApi, LoginApi, LogoutApi, RegistrationApi, ChangeCardsOrder

urlpatterns = [
    path('collections/', CollectionsApi.as_view(), name='collections_api'),
    path('cards/', CardsApi.as_view(), name='cards_api'),
    path('auth/login/', LoginApi.as_view(), name='auth_api'),
    path('auth/logout/', LogoutApi.as_view(), name='logout_api'),
    path('auth/registration/', RegistrationApi.as_view(), name='registration_api'),
    path('cards/change_position/', ChangeCardsOrder.as_view(), name='change_order')
]



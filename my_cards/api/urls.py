from django.urls import path, include
from .views import CollectionsApi, CardsApi, LoginApi, LogoutApi, RegistrationApi, ChangeCardsOrderApi
from .views import CreateCardApi, GetCardInformation, CreateCollecitonApi

urlpatterns = [
    path('collections/', CollectionsApi.as_view(), name='collections_api'),
    path('cards/', CardsApi.as_view(), name='cards_api'),
    path('auth/login/', LoginApi.as_view(), name='auth_api'),
    path('auth/logout/', LogoutApi.as_view(), name='logout_api'),
    path('auth/registration/', RegistrationApi.as_view(), name='registration_api'),
    path('cards/change_position/', ChangeCardsOrderApi.as_view(), name='change_order'),
    path('cards/create_card/', CreateCardApi.as_view(), name='create_card'),
    path('cards/get_card_information/', GetCardInformation.as_view(), name='get_card_information'),
    path('cards/create_collection/', CreateCollecitonApi.as_view(), name='create_collection')
]



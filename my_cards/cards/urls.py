from django.urls import path
from .views.collection_views import CollectionEditView, CollectionListView, CollectionCreateView, CollectionDeleteView, CardPositionView
from .views.card_views import CardsListView, CreateCardView, CardDeleteView

app_name = 'cards'

urlpatterns = [
    path('study_cards/',
         CollectionListView.as_view(),
         name='study_cards'),
    path('open_collection/<int:collection_id>/',
         CardsListView.as_view(),
         name='open_collection'),
    path('create_card/',
         CreateCardView.as_view(),
         name='create_card'),
    path('create_collection/',
         CollectionCreateView.as_view(),
         name='create_collection'),
    path('edit_collection/<int:collection_id>/',
         CollectionEditView.as_view(),
         name='edit_collection'),
    path('remove_card/<int:card_id>/<int:collection_id>/',
         CardDeleteView.as_view(),
         name='remove_card'),
    path('delete_collection/<int:collection_id>/',
         CollectionDeleteView.as_view(),
         name='delete_collection'),
    path('cards:card_position/<int:collection_id>/<int:word_id>/',
         CardPositionView.as_view(),
         name='card_position')
]

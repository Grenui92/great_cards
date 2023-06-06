from django.urls import path
from .views.main import main
from .views.collection_views import CollectionTools
from .views.card_views import CardTools, CardsListView

app_name = 'cards'

urlpatterns = [
    path('', main, name='main'),
    path('create_card/', CardTools.create_card, name='create_card'),
    path('create_collection/', CollectionTools.create_collection, name='create_collection'),
    path('study_cards/', CollectionTools.collections_list, name='study_cards'),
    path('open_collection/<int:collection_id>/', CardsListView.as_view(), name='open_collection'),
    path('edit_collection/<int:collection_id>/', CollectionTools.edit_collection, name='edit_collection'),
    path('remove_card/<int:card_id>/<int:collection_id>/', CardTools.remove_card_from_collection, name='remove_card'),
    path('rename_collection/<int:collection_id>/', CollectionTools.rename_collection, name='rename_collection'),
    path('delete_collection/<int:collection_id>/', CollectionTools.delete_collection, name='delete_collection'),
]

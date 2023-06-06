from cards.models import CardsCollections


class CollectionSrvices:

    @staticmethod
    def get_collection_by_id(collection_id):
        collection = CardsCollections.objects.get(id=collection_id)
        return collection

    @staticmethod
    def get_collections_by_owner(owner_id):
        collections = CardsCollections.objects.filter(owner=owner_id)
        return collections
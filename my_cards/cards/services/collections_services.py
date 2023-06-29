from cards.models import Collections


class CollectionServices:

    @staticmethod
    def get_collection_by_id(collection_id):
        """
        The get_collection_by_id function takes in a collection_id and returns the CardsCollections object with that id.

        :param collection_id: Find the collection in the database
        :return: A collection object
        """
        collection = Collections.objects.get(id=collection_id)
        return collection

    @staticmethod
    def get_collections_by_owner(owner_id):
        """
        The get_collections_by_owner function returns a list of all collections owned by the user with the given owner_id.

        :param owner_id: Filter the collections by owner
        :return: A list of collections that belong to the owner with the given id
        """
        collections = Collections.objects.filter(owner=owner_id)
        return collections

    @staticmethod
    def get_all_cards(collection):
        """
        The get_all_cards function takes a collection as an argument and returns all of the cards in that collection.

        :param collection: Get all of the cards in that collection
        :return: A list of all the cards in a collection
        """
        cards = collection.cards.all()
        return cards

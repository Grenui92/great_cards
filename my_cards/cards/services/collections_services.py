from cards.models import Collections


class CollectionServices:
    """The CollectionServices class provides methods for interacting with
    collections.
    """

    @staticmethod
    def get_collection_by_id(collection_id):
        """The get_collection_by_id function takes in a collection_id and
        returns the CardsCollections object with that id.

        :param collection_id: The id of the collection.
        :return: A collection object
        """
        collection = Collections.objects.get(id=collection_id)
        return collection

    @staticmethod
    def get_collections_by_owner(owner_id):
        """The get_collections_by_owner function returns a list of all
        collections owned by the user with the given owner_id.

        :param owner_id: The id of the owner of the collections
        :return: A list of collections that belong to the owner with
        the given id
        """
        collections = Collections.objects.filter(owner=owner_id)
        return collections

    @staticmethod
    def get_all_cards(collection):
        """The get_all_cards function takes a collection as an argument and
        returns all of the cards in that collection.

        :param collection: The collection object
        :return: A list of all the Cards in a collection
        """
        cards = collection.cards.all()
        return cards

    @staticmethod
    def change_card_position(collection, replace, card_id):
        """The change_card_position function takes in a collection, a boolean
        value, and a word_id. It removes the word_id from the collection's
        order_list and inserts it at the 4th index if replace is False, or
        appends it to the end of the list if replace is True.

        :param collection: Collection object
        :param replace: Boolean value
        :param card_id: The id of the Card
        :return: None
        """
        collection.order_list.remove(card_id)

        if replace:
            collection.order_list.append(card_id)
        else:
            collection.order_list.insert(4, card_id)

        collection.save()

    @staticmethod
    def create_collection(owner, collection_name, collection_img):
        """The create_collection function takes in an owner, a collection_name,
        and a collection_img, and creates a new collection with the given
        parameters.

        :param owner: User object
        :param collection_name: The name of the collection
        :param collection_img: The image of the collection
        :type collection_img: File object, collection image
        :return: A message indicating whether the collection was created
        """
        if Collections.objects.filter(name=collection_name,
                                      owner_id=owner.id).exists():
            return False, f'Collection with name "{collection_name}" already exist, choice another name!'

        if collection_img:
            collection = Collections.objects.create(name=collection_name,
                                                    owner=owner,
                                                    img=collection_img)
        else:
            collection = Collections.objects.create(name=collection_name,
                                                    owner=owner)

        collection.save()

        return f'Collection "{collection_name}" successfully created.'

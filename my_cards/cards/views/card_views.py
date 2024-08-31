from django.db.models import Case, When
from django.shortcuts import render
from django.views.generic import ListView, View
from django.utils.datastructures import MultiValueDictKeyError


from cards.services.cards_services import CardsServices
from cards.services.collections_services import CollectionServices
from cards.models import Collections

from tools.mixins import MessageMixin
from tools.decorators import class_login_required
from tools.exceptions import MessageException
from tools.logger import logger


class CardsListView(ListView, MessageMixin):
    """The CardsListView class is a class-based view that displays all the
    cards in a collection.
    
    The class has the following attributes:
    
    - model: a model class that represents the collection
    - template_name: a string that represents the name of the template file
    - paginate_by: an integer that represents the number of cards to display
    """

    model = Collections
    template_name = 'cards/open_collection.html'
    paginate_by = 1

    def get_queryset(self):
        """Get all cards from the collection. The collection_id is passed as a
        keyword argument. The collection is retrieved from the database using
        the get_collection_by_id method from the CollectionServices class. The
        cards are then retrieved from the collection using the get_all_cards
        method from the CollectionServices class. The cards are ordered based
        on the order_list of the collection.

        :return: A list of cards that belong to a certain collection
        """
        collection_id = self.kwargs['collection_id']
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        cards = CollectionServices.get_all_cards(collection=collection)
        return cards.order_by(Case(*[When(id=card_id, then=pos) for pos, card_id in enumerate(collection.order_list)]))

    def get_context_data(self, *args, object_list=None, **kwargs):
        """Get the context data for the template and add the collection_id to
        the context.

        :param args: Pass a list of arguments to the function
        :param object_list: Pass the list of objects to the template, default\
        is None
        :param kwargs: Pass keyworded, variable-length argument list
        :return: A dictionary of data that will be used to render the template
        """
        context = super().get_context_data(**kwargs)

        collection_id = self.kwargs['collection_id']
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)

        context['collection'] = collection

        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except MessageException as exc:
            return render(request,
                          self.error_500_template,
                          context={'message': exc.message})

class CreateCardView(View, MessageMixin):
    """The CreateCardView class is a class-based view that allows users to
    create a new card.
    
    The class has the following attributes:
    
    - template_name: a string that represents the name of the template file
    - confirm_create_template: a string that represents the name of the\
    template file that confirms the creation of a card
    """

    template_name = 'cards/create_card.html'
    confirm_create_template = 'cards/confirm_card_create.html'

    @class_login_required
    def get(self, request):
        """The get function is used to render the create card form. It also
        gets the collections that belong to the user and passes them to the
        template.

        :param request: request object
        :return: render
        """
        collections = CollectionServices.get_collections_by_owner(
            owner_id=request.user.id)
        selected = request.GET.get('hidden_select')

        # if selected:
        #     original, translit = selected.split('<br><br>')
        #     original = ' '.join(original.split(':')[1:]).strip()
        #     translit = ' '.join(translit.split(':')[1:]).strip()
        #     return render(request,
        #                   self.template_name,
        #                   context={'collections': collections,
        #                            'original': original,
        #                            'translit': translit})
        try:
            english, russian, usage, collection = CardsServices.get_information_from_forms(
                request=request)
            english_word, russian_word, word_usage = CardsServices.get_card_data(english_word=english,
                                                                                 russian_word=russian,
                                                                                 word_usage=usage)
        except MultiValueDictKeyError:
            return render(request, self.template_name, context={'collections': collections})
        except MessageException as exc:
            logger.error(exc.message)
            return render(request,
                          self.error_500_template,
                          context={'message': exc.message})
        message = {
            'russian': russian_word,
            'english': english_word,
            'usage': word_usage,
            'collection': collection}

        return render(request, self.confirm_create_template, context=message)

    @class_login_required
    def post(self, request):
        """The post function is used to create a new card.

        :param request: request object
        :return: render
        """
        english = request.POST.get('english')
        russian = request.POST.get('russian')
        usage = request.POST.get('usage')
        try:
            collection = CollectionServices.get_collection_by_id(
                int(request.POST.get('collection_id')))

            CardsServices.get_new_card(english=english,
                                   russian=russian,
                                   usage=usage,
                                   collection=collection)
        except MessageException as exc:
            return render(request,
                          self.error_500_template,
                          context={'message': exc.message})
            
        return render(request,
                      self.message_template,
                      context={'message': f'Card "{english}" successfully created and added to the collection "{collection.name}"'},)


class CardDeleteView(View):
    """The CardDeleteView class is a view class that deletes a card from a
    collection.

    The class has the following attributes:
    
    - template_name: a string that represents the name of the template file
    """

    template_name = 'cards/edit_collection.html'

    @class_login_required
    def post(self, request, card_id, collection_id):
        """The post function is used to delete a card from a collection.

        :param request: request object
        :param card_id: The id of the Card
        :param collection_id: The id of the Collection
        :return: A render of the collection page with a new queryset
        """
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        card = CardsServices.get_card_from_collection(card_id=card_id)

        collection.cards.remove(card)
        collection.order_list.remove(card.id)
        collection.save()

        queryset = CollectionServices.get_all_cards(collection=collection)

        return render(request,
                      self.template_name,
                      context={'collection': collection,
                               'queryset': queryset,
                               'collection_id': collection_id})

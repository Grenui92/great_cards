import logging
from django.shortcuts import render
from django.views.generic import ListView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from cards.services.cards_services import CardsServices
from cards.services.collections_services import CollectionServices
from cards.forms import CardForm, CollectionForm
from cards.models import Collections, CardCollection
from cards.services.abstract_class import MessageMixin

class CardsListView(ListView):
    """Return all  cards when you open collection."""
    model = Collections
    template_name = 'cards/open_collection.html'
    paginate_by = 1

    def get_queryset(self):
        """
        The get_queryset function is used to filter the queryset of cards that are returned by the view.
        In this case, we want to return all cards in a collection. The collection_id is passed as an argument
        to the view and then used here to get all cards in that particular collection.

        :param self: Represent the instance of the class
        :return: A list of cards that belong to a certain collection
        """

        collection_id = self.kwargs['collection_id']
        collection = CollectionServices.get_collection_by_id(collection_id=collection_id)
        cards = CardCollection.objects.filter(collection=collection)
        # cards = CollectionServices.get_all_cards(collection=collection)
        print(cards)
        return cards.order_by('-rating')

    def get_context_data(self, *_, object_list=None, **kwargs):
        """
        The get_context_data function is a function that allows you to pass additional context variables to the template.
        The get_context_data function takes in an optional object_list parameter, which is used by ListViews and DetailViews.
        It also takes in any number of keyword arguments (kwargs). The **kwargs are passed into the superclass's
        get_context_data method, which returns a dictionary containing all of the context variables for this view.

        :param self: Represent the instance of the class
        :param _: Pass a list of arguments to the function
        :param object_list: Pass the list of objects to the template
        :param kwargs: Pass keyworded, variable-length argument list
        :return: A dictionary of data that will be used to render the template
        """
        context = super().get_context_data(**kwargs)

        collection_id = self.kwargs['collection_id']
        collection = CollectionServices.get_collection_by_id(collection_id=collection_id)

        context['collection'] = collection

        return context

class CreateCardView(View, MessageMixin):
    template_name = 'cards/create_card.html'

    @method_decorator(login_required)
    def post(self, request):
        """
        The post function is used to create a new card.
        It takes in the request and returns a rendered template with either an error message or success message.
        If the form is valid, it saves the form but does not commit it yet, then calls get_new_card from CardsServices
        which creates a new card object and adds it to the database. The function then renders either an error or success
        message depending on whether there was an issue creating the card.

        :param self: Represent the instance of the object itself
        :param request: Get the information from the form
        :return: A render function
        """
        form = CardForm(request.POST, user_id=request.user.id)

        if form.is_valid():
            form.save(commit=False)
            message = CardsServices.get_new_card(form=form)

            return render(request, self.message_template, context=message)

        return render(request, self.template_name, context={'form': form})

    @method_decorator(login_required)
    def get(self, request):

        """
        The get function is used to render the form for a new card.
        It takes in a request object and returns an HTML page with the form.

        :param self: Refer to the class itself
        :param request: Get the user id
        :return: The form object
        """
        form = CardForm(user_id=request.user.id)
        return render(request, self.template_name, context={'form': form})

class CardDeleteView(View):
    template_name = 'cards/edit_collection.html'

    @method_decorator(login_required)
    def post(self, request, card_id, collection_id):

        """
        The post function is used to remove a card from the collection.
        It takes in the request, card_id and collection_id as parameters.
        The function then gets the collection by its id and gets the card from that specific collection.
        Then it removes that specific card from that specific collections cards list using .remove().

        :param self: Represent the instance of the class
        :param request: Pass the request object to the view
        :param card_id: Get the card from the collection
        :param collection_id: Get the collection object from the database
        :return: A render of the collection page with a new queryset
        """
        collection = CollectionServices.get_collection_by_id(collection_id=collection_id)
        card = CardsServices.get_card_from_collection(card_id=card_id)

        collection.cards.remove(card)

        queryset = CollectionServices.get_all_cards(collection=collection)

        return render(request, self.template_name, context={'collection': collection,
                                                                      'queryset': queryset,
                                                                      'collection_id': collection_id,
                                                                      'form': CollectionForm()})


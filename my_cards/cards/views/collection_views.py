import logging

from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from cards.models import Collections
from cards.services.collections_services import CollectionServices
from tools.mixins import MessageMixin
from tools.decorators import class_login_required


class CollectionListView(ListView):
    """The CollectionListView class is a view class that displays a list of
    collections created by the user.
    The class inherits from the ListView class, which is a generic view that
    displays a list of objects.

    The class has the following attributes:
    - model: a model class that represents the collection
    - template_name: a string that represents the name of the template file
    """

    model = Collections
    template_name = 'cards/study_cards.html'

    def get_queryset(self):
        """The get_queryset function is a built-in function that returns a list
        of objects that match the given query parameters.

        :return: A list of objects that match the given query parameters
        """
        collection = Collections.objects.filter(owner=self.request.user.id)
        return collection


class CollectionCreateView(View, MessageMixin):
    """The CollectionCreateView class is a view class that creates a new
    collection.

    The class has the following attributes:
    - template_name: a string that represents the name of the template file
    """

    template_name = 'cards/create_collection.html'

    @class_login_required
    def get(self, request):
        """The get function is used to render the create collection page.

        :param request: request object
        :return: render function
        """
        return render(request, self.template_name)

    @class_login_required
    def post(self, request):
        """The post function is used to create a new collection. It takes in a
        request object and creates a new collection with the given name and
        image. The function then renders the message template with the message
        returned by the CollectionServices.create_collection function.

        :param request: request object
        :return: render function
        """
        owner = request.user
        img = request.FILES.get('collection_img')
        collection_name = request.POST.get('collection_name')

        message = CollectionServices.create_collection(owner=owner,
                                                       collection_name=collection_name,
                                                       collection_img=img)

        return render(request, self.message_template,
                      context={'message': message})


class CollectionDeleteView(View):
    """The CollectionDeleteView class is a view class that deletes a
    collection.

    The class has the following attributes:
    - template_name: a string that represents the name of the template file
    """

    template_name = 'cards/deleting_warning.html'

    @class_login_required
    def get(self, request, collection_id):
        """The get function is used to render the delete warning page for a
        specific collection.

        :param request: request object
        :param collection_id: Collection id
        :return: render function
        """
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        return render(request,
                      self.template_name,
                      context={'collection': collection})

    @class_login_required
    def post(self, request, collection_id):
        """The post function is used to delete a collection.

        :param request: request object
        :param collection_id: Collection id
        :return: redirect function
        """
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        collection.delete()
        return redirect(to='cards:study_cards')


class CollectionEditView(View):
    """The CollectionEditView class is a view class that edits a collection.

    The class has the following attributes:
    - template_name: a string that represents the name of the template file
    """

    template_name = 'cards/edit_collection.html'

    @class_login_required
    def get(self, request, collection_id):
        """The get function is used to render the edit collection page.

        :param request: request object
        :param collection_id: Collection id
        :return: render function
        """
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        queryset = collection.cards.all()
        logging.info(
            f'User -{request.user.id}- open editor for collection -{collection_id}- ')
        return render(request,
                      self.template_name,
                      context={'collection': collection,
                               'queryset': queryset,
                               'collection_id': collection_id})

    @class_login_required
    def post(self, request, collection_id):
        """The post function is used to edit a collection. It takes in a request
        object and edits the collection name.

        :param request: request object
        :param collection_id: Collection id
        :return: redirect function
        """
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        new_name = self.request.POST['new_name']

        if new_name:
            collection.name = new_name
            collection.save()

            return redirect(to='cards:edit_collection',
                            collection_id=collection_id)

        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        queyset = collection.cards.all()
        return render(request,
                      self.template_name,
                      context={'message': 'Field cant be empty',
                               'queryset': queyset,
                               'collection_id': collection_id,
                               'collection': collection})


class CardPositionView(View):
    """The CardPositionView class is a view class that changes the position of
    a card in a collection.

    The class has the following attributes:
    - template_name: a string that represents the name of the template file
    """

    template_name = 'cards:open_collection'

    @class_login_required
    def post(self, request, collection_id: Collections, card_id):
        """The post function is used to change the position of a card in a
        collection.

        :param request: request object
        :param collection_id: Collection id
        :param card_id: _description_
        :return: redirect function
        """
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        replace = int(request.POST.get('replace'))

        CollectionServices.change_card_position(
            collection=collection, replace=replace, card_id=card_id)

        return redirect(to=self.template_name, collection_id=collection_id)

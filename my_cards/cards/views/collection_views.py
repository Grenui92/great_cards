import logging
from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.core.files.storage import FileSystemStorage

from cards.models import Collections
from cards.services.collections_services import CollectionServices
from tools.mixins import MessageMixin
from tools.decorators import class_login_required


class CollectionListView(ListView):
    model = Collections
    template_name = 'cards/study_cards.html'

    def get_queryset(self):
        """
        The get_queryset function is used to filter the queryset of objects that will be displayed in the view.
        In this case, we are filtering by owner (the user who created it). This means that only cards collections
        created by a specific user will be shown.

        :param self: Represent the instance of the class
        :return: A list of objects that match the given query parameters
        """

        collection = Collections.objects.filter(owner=self.request.user.id)
        return collection


class CollectionCreateView(View, MessageMixin):
    template_name = 'cards/create_collection.html'

    @class_login_required
    def get(self, request):
        """
        The get function is used to render the form on the page.
        It takes in a request and returns a rendered template with context.

        :param self: Refer to the current instance of the class, and is used to access variables that belongs to the class
        :param request: Pass the request object to the view
        :return: A form object to the template
        """
        
        return render(request, self.template_name)

    @class_login_required
    def post(self, request):
        """
        The post function is used to create a new collection.
            It takes the following arguments:
                request - The HTTP request object that contains the data for creating a new collection.

        :param self: Represent the instance of the class
        :param request: Get the user who is logged in
        :return: A render function
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
    template_name = 'cards/deleting_warning.html'

    @class_login_required
    def get(self, request, collection_id):
        """
        The get function is used to retrieve a collection from the database.
        It takes in a request and an id of the collection that you want to retrieve.
        The function then uses CollectionServices to get the collection by its id, and returns it as context for rendering.

        :param self: Represent the instance of the object itself
        :param request: Get the request object
        :param collection_id: Get the collection from the database
        :return: A render function
        """

        collection = CollectionServices.get_collection_by_id(collection_id=collection_id)
        return render(request, self.template_name, context={'collection': collection})

    @class_login_required
    def post(self, request, collection_id):
        """
        The post function is used to delete a collection.
        It takes in the request and collection_id as parameters.
        The function then gets the collection by its id, deletes it, and redirects to study cards.

        :param self: Represent the instance of the object itself
        :param request: Pass the request object to the view
        :param collection_id: Get the collection object from the database
        :return: A redirect to the study_cards view
        """

        collection = CollectionServices.get_collection_by_id(collection_id=collection_id)
        collection.delete()
        return redirect(to='cards:study_cards')


class CollectionEditView(View):
    template_name = 'cards/edit_collection.html'

    @class_login_required
    def get(self, request, collection_id):
        """
        The get function is used to render the editor page for a specific collection.
        It takes in a request and collection_id, then uses the CollectionServices class to get that specific collection.
        The function then renders the template with context containing:
        the queryset of cards belonging to that collection,
        the id of that particular card, and
        the name of the template being rendered.

        :param self: Represent the instance of the class
        :param request: Get the request object
        :param collection_id: Get the collection from the database
        :return: A render function
        """

        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        queryset = collection.cards.all()
        logging.info(
            f'User -{request.user.id}- open editor for collection -{collection_id}- ')
        return render(request, self.template_name, context={'collection': collection,
                                                            'queryset': queryset,
                                                            'collection_id': collection_id})

    @class_login_required
    def post(self, request, collection_id):
        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        new_name = self.request.POST['new_name']

        if new_name:
            collection.name = new_name
            collection.save()

            return redirect(to='cards:edit_collection', collection_id=collection_id)

        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        queyset = collection.cards.all()
        return render(request, self.template_name, context={'message': 'Field cant be empty',
                                                            'queryset': queyset,
                                                            'collection_id': collection_id,
                                                            'collection': collection})


class CardPositionView(View):
    template_name = 'cards:open_collection'

    @class_login_required
    def post(self, request, collection_id: Collections, word_id):

        collection = CollectionServices.get_collection_by_id(
            collection_id=collection_id)
        replace = int(request.POST.get('replace'))

        CollectionServices.change_card_position(
            collection=collection, replace=replace, word_id=word_id)

        return redirect(to=self.template_name, collection_id=collection_id)

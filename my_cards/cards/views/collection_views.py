import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View

from cards.forms import CollectionForm
from cards.models import Collections
from cards.services.collections_services import CollectionServices
from cards.services.abstract_class import MessageMixin

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

    @method_decorator(login_required)
    def get(self, request):
        """
        The get function is used to render the form on the page.
        It takes in a request and returns a rendered template with context.

        :param self: Refer to the current instance of the class, and is used to access variables that belongs to the class
        :param request: Pass the request object to the view
        :return: A form object to the template
        """

        form = CollectionForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        """
        The post function is used to create a new collection.
        It takes the request and form as parameters, validates the form, saves it if it's valid and returns a message
        with success or error.

        :param self: Represent the instance of the class
        :param request: Get the data from the form
        :return: A render function that renders the template message_template
        :doc-author: Trelent
        """

        form = CollectionForm(request.POST, request.FILES)
        if form.is_valid():
            collection = form.save(commit=False)

            if Collections.objects.filter(name=collection.name).exists():
                return render(request, self.message_template,
                              context={'message': f'Collection with name "{collection.name}" already exist, '
                                                  f'choice another name!'})

            collection.owner = request.user
            collection.save()
            form.save_m2m()

            return render(request, self.message_template,
                          context={'message': f'Collection "{collection.name}" successfully created.'})

        return render(request, self.template_name, context={'form': form})

class CollectionDeleteView(View):
    template_name = 'cards/deleting_warning.html'

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

        collection = CollectionServices.get_collection_by_id(collection_id=collection_id)
        queryset = collection.cards.all()
        logging.info(f'User -{request.user.id}- open editor for collection -{collection_id}- ')
        return render(request, self.template_name, context={'collection': collection,
                                                                      'queryset': queryset,
                                                                      'collection_id': collection_id})

class CollectionRenameView(View):
    template_name = 'cards/edit_collection.html'

    def post(self, request, collection_id):
        """
        The post function is used to change the name of a collection.
        It takes in a request and collection_id, then gets the collection by its id.
        Then it checks if there is anything in new_name, if so it changes the name of
        that specific collection and saves it. If not, an error message will be displayed.

        :param self: Represent the instance of the class
        :param request: Get the data from the form
        :param collection_id: Get the collection from the database
        :return: The redirect to the edit_collection view
        """

        collection = CollectionServices.get_collection_by_id(collection_id=collection_id)
        new_name = self.request.POST['new_name']
        if new_name:
            collection.name = new_name
            collection.save()

            return redirect(to='cards:edit_collection', collection_id=collection_id)
        return render(request, self.template_name, context={'message': 'Field cant be empty',
                                                            'collection_id': collection_id})

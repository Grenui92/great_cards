import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View

from cards.forms import CollectionForm
from cards.models import CardsCollections
from cards.services.collections_services import CollectionSrvices
from cards.services.abstract_class import MessageMixin

class CollectionListView(ListView):
    model = CardsCollections
    template_name = 'cards/study_cards.html'

    def get_queryset(self):
        collection = CardsCollections.objects.filter(owner=self.request.user.id)
        return collection


class CollectionCreateView(View, MessageMixin):
    template_name = 'cards/create_collection.html'

    @method_decorator(login_required)
    def get(self, request):
        form = CollectionForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = CollectionForm(request.POST, request.FILES)
        if form.is_valid():
            collection = form.save(commit=False)

            if CardsCollections.objects.filter(name=collection.name).exists():
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
        collection = CollectionSrvices.get_collection_by_id(collection_id=collection_id)
        return render(request, self.template_name, context={'collection': collection})

    def post(self, request, collection_id):
        collection = CollectionSrvices.get_collection_by_id(collection_id=collection_id)
        collection.delete()
        return redirect(to='cards:study_cards')

class CollectionEditView(View):
    template_name = 'cards/edit_collection.html'

    def get(self, request, collection_id):
        collection = CollectionSrvices.get_collection_by_id(collection_id=collection_id)
        queryset = collection.cards.all()
        logging.info(f'User -{request.user.id}- open editor for collection -{collection_id}- ')
        return render(request, self.template_name, context={'collection': collection,
                                                                      'queryset': queryset,
                                                                      'collection_id': collection_id})

class CollectionRenameView(View):
    template_name = 'cards/edit_collection.html'

    def post(self, request, collection_id):
        collection = CollectionSrvices.get_collection_by_id(collection_id=collection_id)
        new_name = self.request.POST['new_name']
        if new_name:
            collection.name = new_name
            collection.save()

            return redirect(to='cards:edit_collection', collection_id=collection_id)
        return render(request, self.template_name, context={'message': 'Field cant be empty',
                                                            'collection_id': collection_id})

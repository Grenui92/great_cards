import logging
from django.shortcuts import render
from django.views.generic import ListView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from cards.services.cards_services import CardsServices
from cards.forms import CardForm, CollectionForm
from cards.models import EnglishCards, CardsCollections

class CardsListView(ListView):
    """Return all  cards when you open collection."""
    model = CardsCollections
    template_name = 'cards/open_collection.html'
    paginate_by = 1

    def get_queryset(self):
        collection_id = self.kwargs['collection_id']
        cards = CardsCollections.objects.get(id=collection_id).cards.all().order_by('id')

        return cards

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        collection = CardsCollections.objects.get(id=self.kwargs['collection_id'])

        context['collection'] = collection

        return context

class CreateCardView(View):
    template_name = 'cards/create_card.html'

    @method_decorator(login_required)
    def post(self, request):
        form = CardForm(request.POST, user_id=request.user.id)
        if form.is_valid():
            form.save(commit=False)
            message = CardsServices.get_new_card(form=form)
            return render(request, 'cards/message.html',
                          context=message)

        return render(request, self.template_name, context={'form': form})

    @method_decorator(login_required)
    def get(self, request):
        form = CardForm(user_id=self.request.user.id)
        return render(self.request, self.template_name, context={'form': form})

class CardDeleteView(View):
    template_name = 'cards/edit_collection.html'

    @method_decorator(login_required)
    def post(self, request, card_id, collection_id):
        collection = CardsCollections.objects.get(id=collection_id)
        card = EnglishCards.objects.get(id=card_id)
        collection.cards.remove(card)
        queryset = collection.cards.all()
        logging.info(f'User -{self.request.user.id}- delete card -{card_id}- from collection -{collection_id}-')
        return render(self.request, 'cards/edit_collection.html', context={'collection': collection,
                                                                      'queryset': queryset,
                                                                      'collection_id': collection_id,
                                                                      'form': CollectionForm()})


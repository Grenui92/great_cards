import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator

from cards.forms import CollectionForm
from cards.models import CardsCollections
from cards.services.collections_services import CollectionSrvices

class CollectionTools:

    @staticmethod
    @login_required
    def collections_list(request):
        """Открывает список коллекций карточек."""

        if request.method == 'GET':

            coll = CardsCollections.objects.filter(owner=request.user.id)
            logging.info(f'Get collections owned by user -{request.user.id}- from DB ')
            return render(request, 'cards/study_cards.html', context={'collections': coll})

    @staticmethod
    @login_required
    def open_collection(request, collection_id):
        """Открывает одну коллекцию на экран, выводя список карточек которые в ней есть. Ориентируется по айди коллекции."""

        if request.method == 'GET':
            collection = CollectionSrvices.get_collection_by_id(collection_id=collection_id)
            words_list = collection.cards.all().order_by('id')
            paginator = Paginator(words_list, 1)
            page_number = request.GET.get('page')
            page = paginator.get_page(page_number)
            logging.info(f'User -{collection.owner.id}- open collection -{collection.id}-')
            return render(request, 'cards/open_collection.html', context={'page': page, 'collection': collection})

    @staticmethod
    @login_required
    def create_collection(request):
        if request.method == 'POST':
            form = CollectionForm(request.POST, request.FILES)

            if form.is_valid():
                collection = form.save(commit=False)

                # Проверяет существует ли уже коллекция с таким именемм.
                if CardsCollections.objects.filter(name=collection.name).exists():
                    logging.info(f'User -{request.user.id}- try to create collection with id -{collection.id}-'
                                 f'but it already exist.')

                    return render(request, 'cards/message.html',
                                  context={'message': f'Collection with name "{collection.name}" already exist, '
                                                      f'choice another name!'})

                # Устанавливает текущего пользователя в поле Владелец
                collection.owner = request.user

                collection.save()

                # Для проверки что отношения "многие ко многим" сохранились удачно
                form.save_m2m()

                logging.info(f'User -{request.user.id}- create collection -{collection.id}-')

                return render(request, 'cards/message.html',
                              context={'message': f'Collection "{collection.name}" successfully created.'})

            logging.info(f'User -{request.user.id}- entered wrong information {form} to CardForm')
            return render(request, 'cards/create_collection.html', context={'form': form})

        return render(request, 'cards/create_collection.html', context={'form': CollectionForm()})

    @staticmethod
    @login_required
    def delete_collection(request, collection_id):
        collection = CollectionSrvices.get_collection_by_id(id=collection_id)
        collection.delete()
        collections = CardsCollections.objects.filter(owner=request.user.id)
        logging.info(f'User -{request.user.id}- delete collection -{collection_id}-')
        return render(request, 'cards/study_cards.html', context={'collections': collections})

    @staticmethod
    @login_required
    def edit_collection(request, collection_id):
        collection = CollectionSrvices.get_collection_by_id(collection_id=collection_id)
        queryset = collection.cards.all()
        logging.info(f'User -{request.user.id}- open editor for collection -{collection_id}- ')
        return render(request, 'cards/edit_collection.html', context={'collection': collection,
                                                                      'queryset': queryset,
                                                                      'collection_id': collection_id,
                                                                      'form': CollectionForm()})

    @staticmethod
    @login_required
    def rename_collection(request, collection_id):
        collection = CardsCollections.objects.get(id=collection_id)
        queryset = collection.cards.all()
        if request.method == 'POST':
            form = CollectionForm(request.POST)

            if form.is_valid():
                form.save(commit=False)
                new_name = form.cleaned_data['name']
                collection.name = new_name
                collection.save()
                logging.info(f'User -{request.user.id}- rename collection -{collection_id}- to -{new_name}-')

        return render(request, 'cards/edit_collection.html', context={'form': CollectionForm(),
                                                                      'collection': collection,
                                                                      'collection_id': collection_id,
                                                                      'queryset': queryset})
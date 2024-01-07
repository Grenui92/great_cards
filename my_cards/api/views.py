from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import logout
from django.contrib.auth.models import User

from .serializer import CollectionsSerializer, CardsSerializer
from .services import user_login, user_create, parse_promt

from cards.models import Collections
from cards.services.collections_services import CollectionServices
from cards.services.cards_services import CardsServices
from chat.services.translate import translate_en_ru


class LogingBase(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CollectionsApi(generics.ListAPIView, LogingBase):

    serializer_class = CollectionsSerializer

    def get_queryset(self):
        owner_id = self.request.data.get('user_id')
        result = CollectionServices.get_collections_by_owner(owner_id=owner_id)
        return result


class CardsApi(generics.ListAPIView, LogingBase):

    serializer_class = CardsSerializer

    def get_queryset(self):
        collection = Collections.objects.get(
            id=self.request.data.get('collection_id'))
        result = CollectionServices.get_all_cards(collection=collection)
        return result


class LoginApi(APIView):

    def post(self, request):
        result = user_login(request=request)
        return Response(result)


class LogoutApi(APIView):

    def get(self, request):
        logout(request)
        return Response({'message': 'Succesfully Logout'})


class RegistrationApi(APIView):
    def post(self, request):
        result = user_create(request=request)
        return Response(result)


class ChangeCardsOrderApi(LogingBase):

    def post(self, request):
        collection_id = int(request.data.get('collection_id'))
        replace = int(request.data.get('replace'))
        word_id = int(request.data.get('word_id'))
        collection = Collections.objects.get(id=collection_id)

        CollectionServices.change_card_position(
            collection=collection, replace=replace, word_id=word_id)

        s_collection = CollectionsSerializer(collection)
        return Response({'new_collection': s_collection.data})


class CreateCardApi(LogingBase):

    def post(self, request):
        english_word = request.data.get('english_word')
        russian_word = request.data.get('russian_word')
        word_usage = request.data.get('word_usage')
        collection = CollectionServices.get_collection_by_id(
            collection_id=request.data.get('collection_id'))

        new_card = CardsServices.get_new_card(english=english_word,
                                              russian=russian_word,
                                              usage=word_usage,
                                              collection=collection)
        s_card = CardsSerializer(new_card)
        s_collection = CollectionsSerializer(collection)
        return Response({'new_card': s_card.data, 'colleciton': s_collection.data})


class GetCardInformation(LogingBase):

    def post(self, request):
        english_word = request.data.get('english_word')
        russian_word = request.data.get('russian_word')
        word_usage = request.data.get('word_usage')
        new_english_word, new_russian_word, new_word_usage = CardsServices.get_card_data(english_word=english_word,
                                                                                         russian_word=russian_word,
                                                                                         word_usage=word_usage)
        return Response({'english_word': new_english_word,
                         'russian_word': new_russian_word,
                         'word_usage': new_word_usage})


class CreateCollecitonApi(LogingBase):
    
    def post(self, request):
        user = User.objects.get(username=request.data.get('username'))
        print(user, 'aaaaaaaaaaaaaaaaaaaaaaaaaaa')
        collection_name = request.data.get('collection_name')
        print(collection_name, 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        message = CollectionServices.create_collection(owner=user, collection_name=collection_name)
        return Response({'message': message})
    
class TranslateSentencesApi(APIView):
    def post(self, request):
        text = request.data.get('selected_text')
        from_site = request.data.get('from_site')
        print(from_site)
        if from_site:
            text = parse_promt(text)
        result = translate_en_ru(prompt=text)
        return Response({'message': result})
    
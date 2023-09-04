from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import logout

from .serializer import CollectionsSerializer, CardsSerializer
from .services import user_login, user_create

from cards.models import Collections
from cards.services.collections_services import CollectionServices


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
        collection = Collections.objects.get(id=self.request.data.get('collection_id'))
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

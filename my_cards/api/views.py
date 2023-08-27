from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth import login, authenticate, logout
from django.middleware.csrf import get_token

from .serializer import CollectionsSerializer, CardsSerializer
from cards.models import Collections, Cards


class CollectionsApi(generics.ListAPIView):

    serializer_class = CollectionsSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        return Collections.objects.all()
    
    
class CardsApi(generics.ListAPIView):
    
    serializer_class = CardsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        print(self.request.headers)
        if self.request.user.is_authenticated:
            return Cards.objects.all()
    
class LoginApi(APIView):
    
    def post(self, request):
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        token, *_ = Token.objects.get_or_create(user=user)
        if user is not None:
            login(request, user)

            return Response({'username': user.username,
                             'email': user.email,
                             'id': user.id,
                             'token': token.key})
        else:
            return Response({'server_message': 'Wrong credentials'})
            
class LogoutApi(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': '1'})
    
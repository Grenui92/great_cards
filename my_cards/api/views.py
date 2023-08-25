from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import CollectionsSerializer, CardsSerializer
from cards.models import Collections, Cards


class CollectionsApi(generics.ListAPIView):

    serializer_class = CollectionsSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        return Collections.objects.all()
    
    
class CardsApi(generics.ListAPIView):
    
    serializer_class = CardsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Cards.objects.all()
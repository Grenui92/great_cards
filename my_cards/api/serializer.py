from rest_framework import serializers

from cards.models import Collections, Cards

class CollectionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Collections
        fields = ('id', 'name', 'order_list')
        
        
class CardsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cards
        fields = ('english_word', 'russian_word', 'word_usage')
    
        
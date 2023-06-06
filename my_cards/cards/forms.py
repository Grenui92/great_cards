from django import forms

from .models import EnglishCards, CardsCollections


class CardForm(forms.ModelForm):
    english_word = forms.CharField(max_length=50, widget=forms.TextInput(), required=False)
    russian_word = forms.CharField(max_length=50, widget=forms.TextInput(), required=False)
    word_usage = forms.CharField(required=False)
    collection = forms.ChoiceField(choices=[], required=True, error_messages={'required': f'This field is required. '
                                                                                          f'Turn back and create your first collection.'})
    img = forms.ImageField(required=False)

    def __init__(self, *args, user_id=None, **kwargs):
        """Создает раскрывающийся список для выбора коллекции"""
        super().__init__(*args, **kwargs)
        if user_id:
            self.fields['collection'].choices = [(cc.id, cc.name) for cc in
                                                 CardsCollections.objects.filter(owner=user_id)]

    class Meta:
        model = EnglishCards
        fields = ['english_word', 'russian_word', 'word_usage', 'collection']


class CollectionForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(), required=True)
    img = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = CardsCollections
        fields = ['name', 'img']

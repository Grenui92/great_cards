from django import forms

from .models import Cards, Collections


class CardForm(forms.ModelForm):
    english_word = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'col-5'}), required=False)
    russian_word = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'col-5'}), required=False)
    word_usage = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'col-5'}))
    collection = forms.ChoiceField(choices=[], required=True, error_messages={'required': f'This field is required. '})
    img = forms.ImageField(required=False)

    def __init__(self, *args, user_id=None, **kwargs):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the attributes of an object, which are sometimes called fields or properties.
        In this case, we're setting up a name and age for each Person.

        :param self: Represent the instance of the object itself
        :param *args: Pass a non-keyworded variable length argument list to the function
        :param user_id: Filter the choices in the collection field
        :param **kwargs: Pass keyworded, variable-length argument list to the function
        :return: The instance of the class
        """
        super().__init__(*args, **kwargs)
        if user_id:
            self.fields['collection'].choices = [(cc.id, cc.name) for cc in
                                                 Collections.objects.filter(owner=user_id)]

    class Meta:
        model = Cards
        fields = ['english_word', 'russian_word', 'word_usage', 'collection']


class CollectionForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(), required=True)
    img = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = Collections
        fields = ['name', 'img']

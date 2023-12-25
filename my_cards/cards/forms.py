from django import forms

from .models import Cards, Collections





class CollectionForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'text-input'}), required=True)
    img = forms.FileField(required=False, widget=forms.FileInput())

    class Meta:
        model = Collections
        fields = ['name', 'img']

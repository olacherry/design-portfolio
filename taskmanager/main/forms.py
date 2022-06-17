from .models import Card
from django.forms import ModelForm, TextInput, Textarea

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["name", "contact", "desk"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'feedback__info-name-enter'
            }),
            "contact": TextInput(attrs={
                'class': 'feedback__info-contact-enter'
            }),
            "desk": Textarea(attrs={
                'class': 'feedback__info-desk-enter'
            }),
        }
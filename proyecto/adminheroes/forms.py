from django import forms

from adminheroes.models import Superheroe, User


class SuperheroeForm(forms.ModelForm):

    class Meta:
        model = Superheroe
        fields = [
            'name',
            'alias',
            'poder',
        ]

class UniversoForm(forms.ModelForm):
    
    class Meta:
        model = Universo
        fields = [
            'name',
            'heroes',
        ]
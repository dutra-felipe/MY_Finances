from django import forms
from . import models


class TypeForm(forms.ModelForm):

    class Meta:
        model = models.Type
        fields = ['name', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Tipo de Investimento',
        }

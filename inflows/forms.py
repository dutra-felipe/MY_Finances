from django import forms
from . import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['asset', 'quantity', 'amount', 'created_at', ]

        widgets = {
            'asset': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }
        labels = {
            'asset': 'Ativo',
            'quantity': 'Quantidade',
            'amount': 'Quantia Desembolsada',
            'created_at': 'Data de Compra',
        }

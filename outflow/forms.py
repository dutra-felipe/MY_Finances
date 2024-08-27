from django import forms
from . import models
from django.core.exceptions import ValidationError


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['asset', 'quantity', 'amount', 'created_at',]

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
            'created_at': 'Data de Venda',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        asset = self.cleaned_data.get('asset')

        if quantity > asset.quantity:
            raise ValidationError(
                f'A quantidade disponível para venda do ativo {asset.name} é de {asset.quantity}.'
            )
        return quantity

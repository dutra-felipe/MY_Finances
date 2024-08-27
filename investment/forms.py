from django import forms
from . import models
from django.core.exceptions import ValidationError


class InvestmentForm(forms.ModelForm):

    class Meta:
        model = models.Investment
        fields = ['name', 'symbol', 'investment_type', 'operation', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'symbol': forms.TextInput(attrs={'class': 'form-control'}),
            'investment_type': forms.Select(attrs={'class': 'form-control'}),
            'operation': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome do Ativo',
            'symbol': 'Símbolo',
            'investment_type': 'Tipo de Investimento',
            'operation': 'Operação',
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        symbol = cleaned_data.get('symbol')

        if name and models.Investment.objects.filter(name=name).exclude(id=self.instance.id).exists():
            raise ValidationError("Já existe um investimento com esse nome.")

        if symbol and models.Investment.objects.filter(symbol=symbol).exclude(id=self.instance.id).exists():
            raise ValidationError("Já existe um investimento com esse símbolo.")

        return cleaned_data

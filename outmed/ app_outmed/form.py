
from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'email', 'celular', 'fixo', 'cidade', 'bairro', 'rua', 'numero', 'cep']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['first_name', 'email', 'cnpj', 'email', 'cidade', 'bairro', 'rua', 'numero', 'cep']

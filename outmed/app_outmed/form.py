
from django import forms
from .models import Cliente, Fornecedor, Funcionario, Pedido, contato_fornecedor, Devolução, Livros

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'email', 'celular', 'fixo', 'cidade', 'bairro', 'rua', 'numero', 'cep']


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['first_name', 'email', 'cnpj', 'email', 'cidade', 'bairro', 'rua', 'numero', 'cep']
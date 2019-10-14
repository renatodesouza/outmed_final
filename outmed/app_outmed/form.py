
from django import forms
from .models import Cliente, Fornecedor, Funcionario, Pedido, contato_fornecedor, Devolução, Livros

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'email', 'celular', 'fixo', 'cep', 'cidade', 'bairro', 'rua', 'numero' ]


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['first_name', 'email', 'cnpj', 'email', 'cidade', 'bairro', 'rua', 'numero', 'cep']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['first_name', 'email', 'cpf', 'celular', 'fixo']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['ISBN', 'editora', 'edição', 'titulo', 'autor', 'autor', 'genero', 'preco_compra', 'preco_venda', 'quantidade']

class ContatoFornecedorForm(forms.ModelForm):
    class Meta:
        model = contato_fornecedor
        fields = ['first_name', 'email', 'telefone', 'fornecedor']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['Titulo', 'cod_funcionario', 'cod_cliente', 'Data', 'Valor', 'quantidade', 'situação']

class DevolucaoForm(forms.ModelForm):
    class Meta:
        model = Devolução
        fields = ['Codigo', 'Data', 'Motivo']
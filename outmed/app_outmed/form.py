
from django import forms
from django.forms import modelformset_factory
from .models import Cliente, Fornecedor, Funcionario, Pedido, contato_fornecedor, Devolução, Livros, End_Cliente, End_Fornecedor, Fone_Cliente, Funcionario, Fone_Funcionario


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'email']

class End_ClienteForm(forms.ModelForm):
    model  = End_Cliente
    fields = ['celular', 'fixo', 'cep', 'cidade', 'bairro', 'rua', 'numero']

class Fone_ClienteForm(forms.ModelForm):
    model  = Fone_Cliente
    fields = ['celular', 'fixo']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['first_name', 'email', 'cpf']

class Fone_FuncionarioForm(forms.ModelForm):
    model = Fone_Funcionario
    fields = ['celular', 'fixo']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['first_name', 'email', 'cnpj']

class End_Fornecedor(forms.ModelForm):
    model = End_Fornecedor
    fields = ['cidade', 'bairro', 'rua', 'numero', 'cep']

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
from django.shortcuts import render, redirect

from .form import ClienteForm, FornecedorForm, FuncionarioForm, LivroForm, ContatoFornecedorForm, PedidoForm, DevolucaoForm

from .models import Cliente, Fornecedor, Funcionario, Pedido, contato_fornecedor, Devolução, Livros

import sqlite3


def index(request):
    
    return render(request, 'index.html')

def login(request):
    return render(request, 'Pages/login.html')

def validaCep(request):
    return render(request, 'Pages/valida_Cep.html')

def cliente(request):
    form = ClienteForm()
    return render(request, 'Pages/clientes.html', {'form': form})

def fornecedor(request):
    form = FornecedorForm()
    return render(request, 'Pages/fornecedor.html', {'form': form})


#------------------CLIENTES------------------------------

def listar_cliente(request):
    cliente = Cliente.objects.all()
    
    return render(request, 'Pages/lista_cliente.html', {'cliente': cliente})

def criar_cliente(request):
    form = ClienteForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_cliente')
    return render(request, 'Pages/clientes.html', {'form': form})

def update_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('list_cliente')
    #OBS para o retorno abaixo deve ser tratado caso a atualização nao seja realizada
    return render(request,'clientes.html', {'form': form, 'cliente': cliente})

def delete_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('list_cliente')
    return render(request, 'clientes.html', {'cliente': cliente})
    
#------------------FORNECEDOR------------------------------
def listar_fornecedor(request):
    fornecedor = Fornecedor.objects.all()
    return render(request, 'Pages/listar_fornecedor.html', {'fornecedor': fornecedor})

def criar_fornecedor(request):
    form = FornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_fornecedor')
    return render(request, 'Pages/fornecedor.html', {'form': form})

def update_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    
    form = FornecedorForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')
    #OBS para o retorno abaixo deve ser tratado caso a atualização nao seja realizada
    return render(request,'fornecedor.html', {'form': form, 'fornecedor': fornecedor})

def delete_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('list_fornecedor')
    return render(request, 'fornecedor.html', {'fornecedor': fornecedor})


#------------------FUNCIONARIO------------------------------
def listar_funcionario(request):
    funcionario = Funcionario.objects.all()
    return render(request, 'Pages/listar_funcionario.html', {'funcionario': funcionario})

def criar_funcionario(request):
    form = FuncionarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_funcionario')
    return render(request, 'Pages/funcionario.html', {'form': form})

#--------------------------------------------------------------------------------------------------
#-------------------FALTA CRIAR AS FUNÇÕES DE DELTE E UPDATE DE FUNCIONÁRIO------------------------
#--------------------------------------------------------------------------------------------------

#------------------LIVROS------------------------------

def listar_livros(request):
    livros = Livros.objects.all()
    return render(request, 'Pages/listar_livros.html', {'livros': livros})

def criar_livro(request):
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, 'Pages/livros.html', {'form': form})

def remover_livro(request):
    Livros.objects.filter(ISBN=id).delete()
    return redirect('listar_livro')

#--------------------------------------------------------------------------------------------------
#-------------------FALTA CRIAR AS FUNÇÕES DE DELTE E UPDATE DE LIVROS-----------------------------
#--------------------------------------------------------------------------------------------------

#------------------CONTATO FORNECEDOR------------------------------

def listar_contato(request):
    contato = contato_fornecedor.objects.all()
    return render(request, 'Pages/listar_contato.html', {'contato': contato})

def criar_contato(request):
    form = ContatoFornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_contato')
    return render(request, 'Pages/contato.html', {'form': form})

#--------------------------------------------------------------------------------------------------
#-------------------FALTA CRIAR AS FUNÇÕES DE DELTE E UPDATE DE CONTATO FORNECEDOR-----------------------------
#--------------------------------------------------------------------------------------------------

#------------------CONTATO PEDIDO------------------------------
def listar_pedido(request):
    pedido = Pedido.objects.all()
    return render(request, 'Pages/listar_pedido.html', {'pedido': pedido})

def criar_pedido(request):
    form = PedidoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_pedido')
    return render(request, 'Pages/pedido.html', {'form': form})

#--------------------------------------------------------------------------------------------------
#-------------------FALTA CRIAR AS FUNÇÕES DE DELTE E UPDATE DE PEDIDO-----------------------------
#--------------------------------------------------------------------------------------------------

#------------------DEVOLUÇÃO-----------------------------------------------------------------------
def listar_devolucao(request):
    devolucao = Devolução.objects.all()
    return render(request, 'Pages/listar_devolucao.html', {'devolucao': devolucao})

def devolucao(request):
    form = DevolucaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_devolucao')
    return render(request, 'Pages/devolucao.html', {'form': form})










    



    
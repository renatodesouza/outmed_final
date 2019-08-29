from django.shortcuts import render, redirect

from .form import *

from .models import *



def index(request):
    return render(request, 'menu.html')

def cliente(request):
    form = ClienteForm()
    return render(request, 'clientes.html', {'form': form})

def listar_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'lista_cliente.html', {'cliente': cliente})

def criar_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_cliente')
    return render(request, 'clientes.html', {'form': form})
    
#def list_fornecedor(request):
#    return render(request, 'fornecedor.html')



    



    
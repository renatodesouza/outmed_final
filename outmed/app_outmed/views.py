from django.shortcuts import render, redirect

from .form import *

from .models import *



def index(request):
    return render(request, 'index.html')

def cliente(request):
    form = ClienteForm()
    return render(request, 'Pages/clientes.html', {'form': form})

def listar_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'Pages/lista_cliente.html', {'cliente': cliente})

def criar_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return render('listar_cliente')
    return redirect(request, 'Pages/clientes.html', {'form': form})
    
def new(request):
    return render(request, 'index.html')
    
#def list_fornecedor(request):
#    return render(request, 'fornecedor.html')



    



    
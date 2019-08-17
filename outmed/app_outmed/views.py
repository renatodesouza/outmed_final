from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView   
from django.shortcuts import render

from app_outmed.forms import forms

from .forms import *

from .models import *



def index(request):
    return render(request, 'menu.html')

def cliente(request):
    return render(request, 'clientes.html')
    
def createLivro(ListView):
    model = contato_fornecedor
    fields = ['first-name', 'email', 'telefone']


def fornecedor(request):

    return render(request, 'fornecedor.html')

def funcionario(request):

    return render(request, 'clientes.html')
    

def funcionario(request):
    
    return render(request, 'funcionario.html')
    



    
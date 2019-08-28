from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('cadastro/', views.cadastro, name='cadastro'),
    path('cliente/', views.criar_cliente, name='criar_cliente'),
    path('listar_cliente/', views.listar_cliente, name='listar_cliente'),
    path('fornecedor/', views.list_fornecedor, name='list_fornecedor'),
    #path('funcionario/', views.list_funcionario, name='list_funcionario'),
    
]
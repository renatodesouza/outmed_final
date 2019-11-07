from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    #path('cadastro/', views.cadastro, name='cadastro'),
    path('cliente/', views.cliente, name='cliente'),
    path('fornecedor/', views.fornecedor, name='fornecedor'),
    path('criar_cliente/', views.criar_cliente, name='criar_cliente'),
    path('listar_cliente/', views.listar_cliente, name='listar_cliente'),
    path('criar_fornecedor/', views.criar_fornecedor, name='criar_fornecedor'),
    path('listar_fornecedor/', views.listar_fornecedor, name='listar_fornecedor'),
    path('criar_funcionario/', views.criar_funcionario, name='criar_funcionario'),
    path('listar_funcionario/', views.listar_funcionario, name='listar_funcionario'),
    path('criar_livro/', views.criar_livro, name='criar_livro'),
    path('listar_livros/', views.listar_livros, name='listar_livros'),
    path('remover_livro/', views.remover_livro, name='remover_livro'),
    path('criar_contato/', views.criar_contato, name='criar_contato'),
    path('listar_contato/', views.listar_contato, name='listar_contato'),
    path('criar_pedido/', views.criar_pedido, name='criar_pedido'),
    path('listar_pedido/', views.listar_pedido, name='listar_pedido'),
    path('devolucao/', views.devolucao, name='devolucao'),
    path('listar_devolucao/', views.listar_devolucao, name='listar_devolucao'),
    path('validaCep/', views.validaCep, name='valida_Cep'),
    path('index/', views.index, name='index'),
    
]




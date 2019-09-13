from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('cadastro/', views.cadastro, name='cadastro'),
    path('cliente/', views.cliente, name='cliente'),
    path('criar_cliente/', views.criar_cliente, name='criar_cliente'),
    path('listar_cliente/', views.listar_cliente, name='listar_cliente'),
    path('listar_fornecedor/', views.listar_fornecedor, name='listar_fornecedor'),
    path('criar_fornecedor/', views.criar_fornecedor, name='criar_fornecedor'),
    path('criar_funcionario/', views.criar_funcionario, name='criar_funcionario'),
]
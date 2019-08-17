from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.cliente, name='clientes'),
    path('fornecedor/', views.fornecedor, name='fornecedor'),
    path('funcionario/', views.funcionario, name='funcionario'),
]
from django.db import models
from django.forms import ModelForm
from django.core.mail import send_mail
import datetime


class Cliente(models.Model):
    first_name = models.CharField("Nome", max_length=50)
    last_name = models.CharField("Sobrenome", max_length=80, default=None)
    email = models.CharField(max_length=70)
    celular = models.CharField('Celular', max_length=20, default=None)
    fixo = models.CharField('Fixo', max_length=20, default=None)
    cidade = models.CharField('Cidade', max_length=60, default=None)
    bairro = models.CharField('Bairro', max_length=60, default=None)
    rua = models.CharField('Rua', max_length=50, default=None)
    numero = models.CharField('Numero', max_length=10, default=None)
    cep = models.CharField('CEP', default=None, max_length=10)
    objects = models.Manager ()
    

    def __str__(self):
        return self.first_name


class Funcionario(models.Model):
    first_name = models.CharField("Nome", max_length=50)
    email = models.CharField(max_length=70)
    cpf = models.CharField("CPF", max_length=20, default=None)
    celular = models.CharField('Celular', max_length=20, default=None)
    fixo = models.CharField('Fixo', max_length=20, default=None)
    objects = models.Manager()

    def __str__(self):
        return self.first_name

class Fornecedor(models.Model):
    first_name = models.CharField("Nome", max_length=50)
    email = models.CharField(max_length=70)
    cnpj = models.CharField("CNPJ", max_length=20, default=None)
    cidade = models.CharField('Cidade', max_length=60, default=None)
    bairro = models.CharField('Bairro', max_length=60, default=None)
    rua = models.CharField('Rua', max_length=50, default=None)
    numero = models.CharField('Numero', max_length=10, default=None)
    cep = models.CharField('CEP', default=None, max_length=10)
    objects = models.Manager ()

    def __str__(self):
        return self.first_name

class contato_fornecedor(models.Model):
    first_name = models.CharField("Nome", max_length=50)
    email = models.CharField(max_length=70)
    telefone = models.CharField(max_length=15)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    objects = models.Manager ()

    def __str__(self):
        return self.first_name

class Livros(models.Model):
    ISBN = models.CharField(max_length=20)
    editora = models.CharField(max_length=50)
    edição = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=80, default=None)
    preco_compra = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    preco_venda = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    quantidade = models.IntegerField(default=None)
    objects = models.Manager ()

    def __str__(self):
        return self.titulo

class Pedido(models.Model):
    Titulo = models.ForeignKey('Livros', on_delete=models.CASCADE)
    cod_funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    cod_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    Data = models.DateField('Data da venda')
    Valor = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    situação = models.CharField(max_length=50, blank=True, null=True)
    objects = models.Manager ()


class Devolução(models.Model):
    Codigo = models.ForeignKey('Pedido', on_delete=models.CASCADE, default=None)
    Data = models.DateField('Data da venda')
    Motivo = models.CharField('Motivo', max_length=200)
    objects = models.Manager ()

    



    




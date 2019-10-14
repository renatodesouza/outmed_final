from django.contrib import admin

from .models import *

#senha admin do django usuario lucas senha 123

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'celular', 'fixo', 'cidade', 'bairro', 'rua', 'numero', 'cep' ]
    search_fields = ['first_name']

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'cnpj', 'cidade', 'bairro', 'rua', 'numero', 'cep']
    search_fields = ['first_name']

class EndFuncionarioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'cpf', 'celular', 'celular', 'fixo']
    search_fields = ['first_name']

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'telefone', 'fornecedor']
    search_fields = ['first_name']
    list_display_links = ['first_name', 'fornecedor']
    list_editable = ['email']

class LivroAdmin(admin.ModelAdmin):
    list_display = ['ISBN', 'editora', 'edição', 'titulo', 'autor', 'genero', 'preco_compra', 'preco_venda', 'quantidade']
    search_fields = ['ISBN', 'editora', 'titulo']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['Titulo', 'cod_funcionario', 'cod_cliente', 'Data', 'Valor', 'quantidade', 'situação']
    search_fields = ['Titulo', 'cod_funcionario', 'cod_cliente']
    list_display_links = ['cod_cliente']
    list_editable = ['situação']
    
class DevolucaoAdmin(admin.ModelAdmin):
    list_display = ['Codigo', 'Data', 'Motivo']
    list_display_links = ['Codigo']
    

    
admin.site.register(Funcionario, EndFuncionarioAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)

admin.site.register(contato_fornecedor, ContatoAdmin)

admin.site.register(Livros, LivroAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Devolução, DevolucaoAdmin)




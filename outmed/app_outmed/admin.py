from django.contrib import admin

from .models import *

#senha admin do django usuario lucas senha 123

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name']

class Fone_ClienteAdmin(admin.ModelAdmin):
    list_display = ['celular', 'fixo']

class End_ClienteAdmin(admin.ModelAdmin):
    list_display = ['cidade', 'bairro', 'rua', 'numero', 'cep']

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'cnpj']
    search_fields = ['first_name']

class End_FornecedorAdmin(admin.ModelAdmin):
    list_display = ['cidade', 'bairro', 'rua', 'numero', 'cep']

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'cpf']
    search_fields = ['first_name']

class Fone_FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['celular', 'fixo']
    
class Contato_FornecedorAdmin(admin.ModelAdmin):
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
    

    
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Fone_Funcionario, Fone_FuncionarioAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(End_Cliente, End_ClienteAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(End_Fornecedor, End_FornecedorAdmin)

admin.site.register(contato_fornecedor, Contato_FornecedorAdmin)

admin.site.register(Livros, LivroAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Devolução, DevolucaoAdmin)




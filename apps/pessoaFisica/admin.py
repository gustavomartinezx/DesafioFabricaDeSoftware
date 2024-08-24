from django.contrib import admin
from apps.pessoaFisica.models import Cliente, Funcionario

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'sexo', 'pais_residente')
    search_fields = ('nome', 'sobrenome', 'cpf')

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'sexo', 'cargo', 'salario')
    search_fields = ('nome', 'sobrenome', 'cpf', 'cargo')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
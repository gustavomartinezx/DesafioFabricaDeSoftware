from rest_framework import serializers

from apps.pessoaFisica.models import Cliente, Funcionario, Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model =   Pessoa
        fields = ['nome', 'sobrenome', 'cpf', 'pais_residente', 'sexo']

class ClienteSerializer(PessoaSerializer):
    class Meta(PessoaSerializer.Meta):
        model = Cliente
        fields = '__all__'

class FuncionarioSerializer(PessoaSerializer):
    class Meta(PessoaSerializer.Meta):
        model = Funcionario
        fields = '__all__'
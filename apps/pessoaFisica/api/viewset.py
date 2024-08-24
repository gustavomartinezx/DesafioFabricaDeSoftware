from rest_framework import viewsets

from apps.pessoaFisica.models import Cliente, Funcionario
from apps.pessoaFisica.api.serializer import ClienteSerializer, FuncionarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
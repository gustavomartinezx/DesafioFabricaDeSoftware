import requests

from rest_framework import viewsets
from apps.produto.models import Produto
from apps.produto.api.serializer import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        cliente = serializer.validated_data.get('comprador')
        if cliente:
            moeda = self.get_moeda(cliente.pais_residente)
            serializer.save(moeda=moeda)
        else:
            serializer.save()

    def get_moeda(self, pais):
        response = requests.get(f'https://restcountries.com/v3.1/name/{pais}?fullText=true')
        if response.status_code == 200:
            data = response.json()
            if data and 'currencies' in data[0]:
                return list(data[0]['currencies'].keys())[0]  
        return 'BRL'
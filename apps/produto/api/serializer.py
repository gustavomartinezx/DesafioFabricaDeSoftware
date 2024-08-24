from rest_framework import serializers
from apps.produto.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    moeda = serializers.CharField(read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'
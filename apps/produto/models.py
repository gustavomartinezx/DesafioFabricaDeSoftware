from django.db import models

from apps.pessoaFisica.models import Cliente, Funcionario

# Create your models here.
class Produto(models.Model):
    comprador = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE) 
    moeda = models.CharField(max_length=3, editable=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2)  
    imagem = models.ImageField()
    em_estoque = models.BooleanField(default=True)

    def __str__(self):
        return f'Produto: {self.id}'
    
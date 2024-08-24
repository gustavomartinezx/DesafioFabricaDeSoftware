from django.db import models

# Create your models here.
class Pessoa(models.Model):
    SEXO = [
        ('F', 'Feminino'),
        ('M', 'Masculino')
    ]

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')

    class Meta:
        abstract = True


class Cliente(Pessoa):
    pais_residente = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
class Funcionario(Pessoa):
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'funcionario'

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
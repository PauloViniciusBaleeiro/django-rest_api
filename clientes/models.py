from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.PositiveIntegerField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

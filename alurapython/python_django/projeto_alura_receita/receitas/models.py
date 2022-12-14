from django.db import models
from datetime import datetime


class Receita(models.Model):
    nome_receita = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
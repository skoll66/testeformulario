from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.


class Pedido(models.Model):
    Nome = models.CharField(max_length=10)
    Last_name =models.CharField(max_length=15)
    Salario = models.FloatField()
    data_nascimento = models.DateField(verbose_name='Data do Evento')
    cidade = models.CharField(max_length=10)
    Aprovacao = models.BooleanField()

    class Meta:
        db_table = 'pedido'

    def Aprovado(self):
        return bool(self.Aprovacao)

    def __str__(self):

        return self.id

    def get_data_evnto(self):
        return self.data_nascimento.strftime('%d/%m/%Y')
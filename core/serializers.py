from .models import Pedido
from rest_framework import serializers
from datetime import date

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class InsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido

        exclude = ['Aprovacao']
    def validate(self, data):
        """
        Check that the start is before the stop.
        """

        aniversario = data['data_nascimento']
        now = date.today()
        dif = now - aniversario
        rslt = (dif.days / 365.25)
        if data['Salario'] > 100000 and data['data_nascimento'] >18.0:
            data['Aprovacao']= True
        else:
            data['Aprovacao'] = False
        return data
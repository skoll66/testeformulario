from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from core.Dao import DaoMysql
from core.Dao.DaoMysql import insertUsuario,inserticket
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Pedido
from.serializers import CategoriaSerializer, InsertSerializer
from rest_framework.renderers import JSONRenderer

class solViewSet(ListAPIView):
    "Verifica todas as solicitações"
    queryset = Pedido.objects.all()
    serializer_class = CategoriaSerializer


class insertViewSet(CreateAPIView):
    "Insirar seus dados para a solicitação"
    queryset = Pedido.objects.all()
    serializer_class = InsertSerializer

SOLICITA = solViewSet.as_view()
INSERT = insertViewSet.as_view()
@api_view(['GET','POST'])

def home(request):
    "UTILIZE PARA Verificar o status da SUA SOLICITAÇÃO"
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        output = [{ 'ID':pedido.id,
                    'nome':pedido.Nome,
        }for pedido in pedidos]
        return Response(output)
    elif request.method == 'POST':
        id = request.data.get('ID')
        pedidos = Pedido.objects.filter(id = id)
        output = [{'ID': pedido.id,
                  'nome': pedido.Nome,
                  'Aprovação':pedido.Aprovacao
                  } for pedido in pedidos]
        return Response(output)
def ajaxPegaDados(request):
    try:
        if request:
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            dados = request.GET
            cpf =request.GET['Cpf']
            nome =request.GET['Nome']
            sobrenome = request.GET['Sobrenome']
            email = request.GET['Email']
            celular = request.GET['Celular']
            title = request.GET['title']
            texto = request.GET['texto']
            insertUsuario(cpf,sobrenome,nome,email)
            inserticket (cpf,texto,email,dt_string)
            data_converter_json = JsonResponse({'dados': dados, }, safe=False)
            #data_converter_json='ticketabertocomsucesso'
        return HttpResponse(data_converter_json)
        print(request)
    except Exception as ex:
        print(ex)


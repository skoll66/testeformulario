from django.contrib import admin
from core.models import Pedido
# Register your models here.
class EventoAdmin(admin.ModelAdmin):

    list_display = ('id','Nome','Last_name','data_nascimento','Salario','Aprovacao')
    list_filter = ('Nome','Aprovacao',)

admin.site.register(Pedido, EventoAdmin)

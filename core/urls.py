from django.urls import path,include
from rest_framework import routers
from .views import INSERT, SOLICITA, ajaxPegaDados, home




urlpatterns = [
    # path('', views.home, name='index'),

    path("api/",SOLICITA ),
    path("insert/",INSERT ),
    path('', home, name='index'),
    path('core/ajaxPegaDados/', ajaxPegaDados, name='ajaxPegaDados'),
]
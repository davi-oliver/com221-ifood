from django.urls import path
from ifood_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("abrirConta/", views.abrirConta, name="abrirConta"),
    path("cadastrarEndereco/", views.cadastrarEndereco, name="cadastrarEndereco"),
   # path("abrirConta/criarCliente/", views.criarCliente, name="criarCliente"),
]

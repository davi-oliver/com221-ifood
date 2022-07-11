from django.urls import path
from controle_bancario_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("abrirConta/", views.abrirConta, name="abrirConta"),
    path("emitirExtrato/", views.emitirExtrato, name="emitirExtrato"),
    path("emitirSaldo/", views.emitirSaldo, name="emitirSaldo"),
    path("encerrarConta/", views.encerrarConta, name="encerrarConta"),
    path("realizarDeposito/", views.realizarDeposito, name="realizarDeposito"),
    path("realizarSaque/", views.realizarSaque, name="realizarSaque"),
    path("gerenciarClientes/", views.gerenciarClientes, name="gerenciarClientes"),
   # path("abrirConta/criarCliente/", views.criarCliente, name="criarCliente"),
]

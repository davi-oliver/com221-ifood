from django.urls import path
from ifood_app import views

urlpatterns = [
    path("", views.abrirConta, name="abrirConta"),
    path("cadastrarEndereco/", views.cadastrarEndereco, name="cadastrarEndereco"),
    path("selecionarFornecedor/", views.selecionarFornecedor, name="selecionarFornecedor"),
    path("fazerPedido/", views.fazerPedido, name="fazerPedido"),
    path("selecionarProduto/", views.selecionarProduto, name="selecionarProduto"),
    path("pedidoRealizado/", views.pedidoRealizado, name="pedidoRealizado"),
]
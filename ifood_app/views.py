from datetime import datetime
import random
from http import client
import sys
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

from ifood_app.models import Endereco, Pedido, PessoaFisica


def home(request):
    return render(request, "ifood/abrirConta.html")

def abrirConta(request):
    if request.method == "POST":
        cliente = registrarCliente(request)
        return redirect("selecionarFornecedor")

    else:  
         return render(request, "ifood/abrirConta.html")    

def registrarCliente(request):
     cliente = PessoaFisica(nomePessoa = request.POST['nomePessoa'], telefonePessoa = request.POST['telefonePessoa'], cpfPessoa = request.POST['cpfPessoa'], dataNascimento = request.POST['dataNascimento'], senhaPessoa = request.POST['senhaPessoa'])
     cliente.registrarPessoa()
     return cliente



        
def fazerPedido(request):
    if request.method == "POST":
        pedido = registrarPedido(request)
        return redirect("pedidoRealizado")

    else:  
         return render(request, "ifood/fazerPedido.html")

def registrarPedido(request):
     cliente = Pedido(metodoPagamento = request.POST['metodoPagamento'], observacoes = request.POST['observacoes'], cupom = request.POST['cupom'])
     cliente.registrarPedido()
     return cliente




def cadastrarEndereco(request):
    if request.method == "POST":
        endereco = registroEndereco(request)
        return redirect("fazerPedido")
    else:  
         return render(request, "ifood/cadastrarEndereco.html")

def registroEndereco(request):
     endereco = Endereco(rua = request.POST['rua'], bairro = request.POST['bairro'], complemento = request.POST['complemento'], numero = request.POST['numero'], cep = request.POST['cep'])
     endereco.registrarEndereco()
     return endereco


def selecionarFornecedor(request):
    return render(request, "ifood/selecionarFornecedor.html")

def rotaPedido(request):
    return render(request, "ifood/fazerPedido.html")

def selecionarProduto(request):
    return render(request, "ifood/selecionarProduto.html")
 
def pedidoRealizado(request):
    return render(request, "ifood/pedidoRealizado.html")

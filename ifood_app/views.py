from datetime import datetime
import random
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

#importações dos modelos (classes) necessários para o UC Abrir Conta
from ifood_app.models import PessoaFisica

# Create your views here.

def home(request):
    #método executado quando o usuário está na interface (tela) inicial do sistema  home.html
    return render(request, "ifood/home.html")

def abrirConta(request):
    # verifica se a solicitação (request) contém dados (envio usando o metodo POST)
    if request.method == "POST":
        #1 - verificar se o cpf já existe e no caso de não existir, criar o cliente
        
        #2 - no caso do cliente não existir permitir a criação do cliente (objeto do tipo PessoaFisica)
            #passa como parâmetro os dados enviados no formulário
        cliente = registrarCliente(request)
        
        #3 - no caso do cliente existir, permitir a atualização de informações do cliente

        #cliente = modificarCliente(request)  #to-do: implementar o metodo

        #4 - realizar a abertura de conta para o cliente

        #6 - redireciona para a tela de realizar depósito, onde o usuário será redirecionado à interface de usuário do UC Realizar Depósito
        return redirect("cadastrarEndereco")

    else:  
        # a solicitação (request) não contém dados (solicitação feita usando o metodo GET)
        # dessa forma será mostrado para o usuario final o form de abertura de conta que está em abrirConta.html
         return render(request, "ifood/abrirConta.html")

def registrarCliente(request):
     #criação do cliente como instância da classe PessoaFisica definida no modelo de classes
     cliente = PessoaFisica(nomePessoa = request.POST['nomePessoa'], telefonePessoa = request.POST['telefonePessoa'], cpfPessoa = request.POST['cpfPessoa'], dataNascimento = request.POST['dataNascimento'], senhaPessoa = request.POST['senhaPessoa'])
     #registro do cliente no banco fazendo uso do método registrarPessoa() definido na classe PessoaFisica no modelo de classes
     cliente.registrarPessoa()
     return cliente


def cadastrarEndereco(request):
    return render(request, "ifood/cadastrarEndereco.html")
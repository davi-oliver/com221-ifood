from datetime import datetime
import random
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone

#importações dos modelos (classes) necessários para o UC Abrir Conta
from controle_bancario_app.models import contaComum, PessoaFisica

# Create your views here.

def home(request):
    #método executado quando o usuário está na interface (tela) inicial do sistema  home.html
    return render(request, "controle_bancario/home.html")

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
        conta = criarConta(request,cliente)

        #5 - emitir o cartão da conta
        emissao = emitirCartao(cliente,conta)

        #6 - redireciona para a tela de realizar depósito, onde o usuário será redirecionado à interface de usuário do UC Realizar Depósito
        return redirect("realizarDeposito")

    else:  
        # a solicitação (request) não contém dados (solicitação feita usando o metodo GET)
        # dessa forma será mostrado para o usuario final o form de abertura de conta que está em abrirConta.html
         return render(request, "controle_bancario/abrirConta.html")

def registrarCliente(request):
     #criação do cliente como instância da classe PessoaFisica definida no modelo de classes
     cliente = PessoaFisica(nomePessoa = request.POST['nomePessoa'], enderecoPessoa = request.POST['enderecoPessoa'], cepPessoa = request.POST['cepPessoa'], telefonePessoa = request.POST['telefonePessoa'], rendaPessoa = request.POST['rendaPessoa'], situacaoPessoa = 1, cpfPessoa = request.POST['cpfPessoa'], rgPessoa = request.POST['rgPessoa'], dataNascimento = request.POST['dataNascimento'])
     #registro do cliente no banco fazendo uso do método registrarPessoa() definido na classe PessoaFisica no modelo de classes
     cliente.registrarPessoa()
     return cliente

#criar conta
def criarConta(request,cliente):
    #dados da contaComum
        numeroConta = str(random.randint(1,500))
        aberturaConta = datetime.today().strftime('%Y-%m-%d')
        situacaoConta = '1'
        senhaConta = request.POST['senhaConta']  #to-do: implementar a encriptação da senha
        saldoConta = '0'
        #criação do objeto do tipo contaComum
        conta = contaComum(idCliente = cliente, numeroConta = numeroConta, aberturaConta = aberturaConta, situacaoConta = situacaoConta, senhaConta = senhaConta, saldoConta = saldoConta)
        conta.abrirConta()
        return conta.numeroConta

#emitir cartao
def emitirCartao(cliente,conta):
    #realizar a emissão do cartao
    return 0

def emitirExtrato(request):
    return render(request, "controle_bancario/emitirExtrato.html")

def emitirSaldo(request):
    return render(request, "controle_bancario/emitirSaldo.html")

def encerrarConta(request):
    return render(request, "controle_bancario/encerrarConta.html")

def realizarDeposito(request):
    return render(request, "controle_bancario/realizarDeposito.html")

def realizarSaque(request):
    return render(request, "controle_bancario/realizarSaque.html")

def gerenciarClientes(request):
    return render(request, "controle_bancario/gerenciarClientes.html")




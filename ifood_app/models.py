from distutils.archive_util import make_zipfile
from xml.parsers.expat import model
from django.db import models
from django.forms import CharField, Field
from django.utils import timezone
import datetime

# As classes do modelo do sistema são definidas neste arquivo  models.py

# ****** Definição da classe PessoaFisica
class PessoaFisica(models.Model):
    #lista de atributos com os tipos que deverão ser armazenados no banco
    nomePessoa = models.CharField(max_length=100)
    telefonePessoa = models.CharField(max_length=100)
    cpfPessoa = models.IntegerField( )
    dataNascimento = models.DateField( )
    senhaPessoa = models.CharField(max_length=100)

    # ********  Métodos da classe ************

    def registrarPessoa(self):
        self.save()
    
    #def validarCpf(self, cpf):
    
    #def consultarCpf(self, cpf):

# ****** Definição da classe Endereço
class Endereco(models.Model):
    #lista de atributos com os tipos que deverão ser armazenados no banco
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)

    # ********  Métodos da classe ************

    def registrarEndereco(self):
        self.save()

# ****** Definição da classe Endereço
class Pedido(models.Model):
    #lista de atributos com os tipos que deverão ser armazenados no banco
    metodoPagamento = models.CharField(max_length=100)

    # ********  Métodos da classe ************

    def registrarPedido(self):
        self.save()

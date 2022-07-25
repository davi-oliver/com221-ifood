from distutils.archive_util import make_zipfile
from xml.parsers.expat import model
from django.db import models
from django.forms import CharField, Field
from django.utils import timezone
import datetime

class PessoaFisica(models.Model):
    nomePessoa = models.CharField(max_length=100)
    telefonePessoa = models.CharField(max_length=100)
    cpfPessoa = models.IntegerField( )
    dataNascimento = models.DateField( )
    senhaPessoa = models.CharField(max_length=100)

    def registrarPessoa(self):
        self.save()
    
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)

    def registrarEndereco(self):
        self.save()

class Pedido(models.Model):
    metodoPagamento = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=100)
    cupom = models.CharField(max_length=100)

    def registrarPedido(self):
        self.save()

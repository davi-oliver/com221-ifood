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
    enderecoPessoa = models.CharField(max_length=300)
    cepPessoa = models.IntegerField( )
    telefonePessoa = models.CharField(max_length=100)
    rendaPessoa = models.FloatField( )
    situacaoPessoa = models.IntegerField(default=1)
    cpfPessoa = models.IntegerField( )
    rgPessoa = models.CharField(max_length=10)
    dataNascimento = models.DateField( )

    # ********  Métodos da classe ************

    def registrarPessoa(self):
        self.save()
    
    #def validarCpf(self, cpf):
    
    #def consultarCpf(self, cpf):


# ****** Definição da classe contaComum 
class contaComum(models.Model):
    #lista de atributos com os tipos que deverão ser armazenados no banco
    idCliente = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE)  # relacionamento entre classes: 1 pessoa Fisica tem 1,* contas
    numeroConta = models.IntegerField()
    aberturaConta = models.DateField( )
    fechamentoConta = models.DateField(null=True)
    situacaoConta = models.IntegerField() # 1, 0
    senhaConta = models.CharField(max_length=30)
    saldoConta = models.IntegerField()

    # ********  Métodos da classe ************

    def abrirConta(self):
        self.save()
        
    #def consultarConta(numeroConta):
    
    #def emitirSaldo(numeroConta):

# ****** Definição da classe movimento
class movimento(models.Model):
    #lista de atributos com os tipos que deverão ser armazenados no banco
    conta = models.ForeignKey(contaComum, on_delete=models.CASCADE)  # relacionamento entre classes: 1 conta tem 1,* movimentos
    tipoMovimento = models.IntegerField() # 1, 2, 3
    dataMovimento = models.DateTimeField()
    horaMovimento = models.TimeField()
    valorMovimento = models.FloatField()

    # ********  Métodos da classe ************

    #def registrarMovimento():
    
    #def consultarMovimento():


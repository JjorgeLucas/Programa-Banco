from cliente import *
from contas import *

class Banco():
    def __init__(self, NomeBanco, ListaClientes, ListaContas):
        self.NomeBanco = NomeBanco
        self.ListaClientes = ListaClientes
        self.ListaContas = ListaContas
    def NovoCliente(self, nome, CPF):
        cliente = str(Cliente(nome, CPF))
        self.ListaClientes.append(cliente)
    def NovaConta(self, titulares, numero, saldo = 0):
        conta = str(Conta(titulares, numero, saldo))
        self.ListaContas.append(conta)
    def Contas(self):
        return self.ListaContas

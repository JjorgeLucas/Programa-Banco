class Conta:
    def __init__(self, titulares, numero, saldo = 0):
        self.titulares = titulares #uma lista de clientes (CPF e/ou nome)
        self.numero = numero
        self.saldo = saldo
        self.extrato = [saldo]

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(-valor)

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append(valor)
    def ImprimeExtrato(self):
        print('-----------------------------------------------------------------------------------------------')
        print('Extrato:')
        saldo = 0
        for op in self.extrato:
            saldo += op
            if op >= 0:
                print(f"""Depósito de R${op:10.2f}      |█|Saldo           R${saldo:10.2f}.""")
                print('█')
            else:
                print(f"""Saque de    R${-op:10.2f}      |█|Saldo           R${saldo:10.2f}.""")
                print('█')
        print(f'Saldo atual:R${self.saldo:10.2f}')
        print('-----------------------------------------------------------------------------------------------')
    
    def resumo(self):
        print(f"""
Titulares:   {self.titulares}   Número da conta:   %s   Saldo:   %10.2f
""" % (self.numero, self.saldo))

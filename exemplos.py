from cliente import *
from contas import *
from banco import *


#Clientes
c1 = Cliente('jao', 123)
c2 = Cliente('JL',456)
c3 = Cliente('Bia',789)
c4 = Cliente('Leo',120)

#Contas
C1 = Conta([str(c1)], 1029 ,100)
C23 = Conta([str(c2),str(c3)], 5823 ,750)

#Bancos
B1 = Banco('MyBank',[str(c1),str(c2),str(c3)],[str(C1),str(C23)])
B2 = Banco('YourBank',[str(c4)],[])

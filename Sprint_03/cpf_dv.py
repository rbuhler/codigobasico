"""
A declaração import permite acesso a código em outro módulo/arquivo
"""
import sys
"""
O código abaixo é uma função que é implementada apenas uma vez e pode ser 
acessada quantas vezes forem necessárias.
"""
def ajuste(digito):
    if (digito == 10):
        digito = 0
    return digito

"""
A partir daqui temos nosso algoritmo para o cálculo e apresentação 
do CPF completo.
"""
numeroCpf = sys.argv[1]
calcDig1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

contadorCPF = 8
contador = sutotal = total = 0

# 1o passo
while contador <= contadorCPF:
    subTotal = int(numeroCpf[contador]) * calcDig1[contador]
    total = total + subTotal
    contador = contador + 1
print("1o passo Total : %i" % total)

# 2o passo
primeiroDigito = [ajuste((total * 10) % 11)]
print("\t" "Primeiro digito : %i" % primeiroDigito[0])
numeroCpf += str(primeiroDigito[0])
print("2o passo CPF: %s" % numeroCpf)

contador = 0
subTotal = 0
total = 0

# 3o passo
while contador <= contadorCPF:
    subTotal = int(numeroCpf[contador + 1]) * calcDig1[contador]
    total = total + subTotal
    contador = contador + 1
print("3o passo Total : %i" % total)

# 4o passo
segundoDigito = [ajuste((total * 10) % 11)]
print("\t" "Segundo digito : %i" % segundoDigito[0])
numeroCpf += str(segundoDigito[0])
print("4o passo CPF : %s" % numeroCpf)
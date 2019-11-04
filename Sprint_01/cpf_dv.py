"""
A declaração import permite acesso a código em outro módulo/arquivo
"""
import sys

numeroCpf = sys.argv[1]
calcDig1 = [10, 9,8,7,6,5,4,3,2]

# multiplicar cada número do cpf por um fator
# este fator começa em 10 e diminui em 1 ponto a cada interação
# cpf posição 1 multiplica por 10
# cpf posição 2 multiplica por 9
# ...

contadorDigito1 = 8
contador = 0
subTotal = 0
total = 0
while contador <= contadorDigito1:
    subTotal = int(numeroCpf[contador]) * calcDig1[contador]
    total = total + subTotal
    contador = contador + 1
print("Total : %i" % total)
# O primeiro dígito é o resto da divisão do total calculado por 11
primeiroDigito = [(total * 10) % 11]
print("Primeiro digito : %i" % primeiroDigito[0])
numeroCpf += str(primeiroDigito[0])

contadorDigito2 = 8
contador = 0
subTotal = 0
total = 0
print("Tamanho: %i" % len(numeroCpf))
print(numeroCpf)

while contador <= contadorDigito2:
    subTotal = int(numeroCpf[contador+1]) * calcDig1[contador]
    total = total + subTotal
    contador = contador + 1

print("Total : %i" %total)
# O segundo dígito é o resto da divisão do total calculado por 11
segundoDigito = [(total * 10) % 11]
print("Primeiro digito : %i" % segundoDigito[0])
numeroCpf += str(segundoDigito[0])

print("CPF : %s" % numeroCpf)
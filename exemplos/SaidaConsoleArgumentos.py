import sys

argItems = sys.argv
argQuantidade = len(sys.argv) - 1

contador = 0
while contador < argQuantidade:
    print("Argumento %i : %s" % (contador, argItems[contador]))
    contador = contador + 1

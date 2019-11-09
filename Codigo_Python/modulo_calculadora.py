def soma(numero1, numero2):
    soma_total = numero1 + numero2

    return soma_total

def subtração(numero1, numero2):
    sub_total = 0

    return sub_total
# divisao
# multiplicacao
# potência

def eh_primo(numero):
    resultado = False
    contador = 2
    while contador <= numero:
        resto = numero % contador
        if resto == 0:
            if contador == numero:
                resultado = True
            else:
                resultado = False
                break
        else:
            resultado = True
        contador += 1
    return resultado
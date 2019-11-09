
numero_string = "883769820"
digito = "87"
digito_calculado = ""
soma = 0

fatores = [10, 9, 8, 7 , 6, 5, 4, 3, 2]
contador = 0

# passo número 1
for fator in fatores:
    soma = soma + (int(numero_string[contador]) * fator)
    contador += 1

# passo número 2
multiplicacao = soma * 10
digito_1 = multiplicacao % 11
if digito_1 > 9:
    digito_1 = 0

numero_string = numero_string + str(digito_1)

# passo 3
contador = 1
soma = 0
multiplicacao = 0
for fator in fatores:
    soma = soma + (int(numero_string[contador]) * fator)
    contador += 1

# passo 4
multiplicacao = soma * 10
digito_2 = multiplicacao % 11

if digito_2 > 9:
    digito_2 = 0

numero_string = numero_string + str(digito_2)

digito_calculado = str(digito_1) + str(digito_2)

if digito == digito_calculado:
    print("sucesso")
else:
    print("derrota")
"""
Aqui temos testes de uma condição.
Se o teste tiver resultado verdadeiro a linhas seguintes serão executadas.
Caso contrário as lihas do bloco "else" são executadas.
Apenas um bloco é executado a cada teste.
"""

# Neste exemplo a condição é verdadeira então o 1o bloco é executado
print("Primeiro teste")
if 1 + 1 == 2:
    print("A condição é verdadeira.")
else:
    print("A condição é falsa.")

# Já neste outro caso a condição não é verdadeira, com isso o bloco "else" é executado
print('\n' + "Segundo teste")
if 1 + 1 == 3:
    print("A condição é verdadeira.")
else:
    print("A condição é falsa.")

# Neste caso foi executada uma operação e o resultado armazenado em uma variável.
# O teste da condição é feito a partir do resultado da operação armazenado nesta variável

resultado = 10 > 20

print('\n' + "Conteúdo da variável : ")
print(resultado)

if resultado:
    print("O resultado do teste é Verdadeiro")
else:
    print("O resultado do teste é Falso")

# Em alguns casos é necessário fazer mais testes, pois temos
# mais condições a serem testadas

valor = 30
print('\n' + "Teste de multiplas condições.")
print("Valor da variável " + str(valor))

if valor > 29:
    print("Variável com valor maior do que 29   .")
elif valor == 30:
    print("Variável com valor igual a 30.")
else:
    print("Variável com valor diferente das condições anteriores.")

# Expressão ternária
print("Expressão Ternária Verdadeira") if (1 + 1 == 2) else print("Expressão Ternária Falsa")

a = "Expressão Ternária Verdadeira" if (1 + 1 == 2) else "Expressão Ternária Falsa"
print(a)
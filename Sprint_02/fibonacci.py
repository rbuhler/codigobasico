def fibonacci(quantidade):
    lista = []
    fibo_a = 0
    fibo_b = 1
    fibo_c = 0
    contador: int = 2

    lista += [fibo_a]
    lista += [fibo_b]

    if quantidade < 2:
        quantidade = 2

    while contador < quantidade:
        contador += 1
        fibo_c = fibo_b + fibo_a
        lista += [fibo_c]
        fibo_a = fibo_b
        fibo_b = fibo_c

    return lista


print(fibonacci(10))
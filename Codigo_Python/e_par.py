def e_par(valor):
    resultado = True
    resto = valor % 2

    if resto > 0:
        resultado = False
    else:
        resultado = True

    return resultado

if e_par( 3 ):
    print("E par")
else:
    print("E Impar")
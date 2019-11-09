import modulo_calculadora

def hipotenusa(parametro1, parametro2):
    quadrado1 = parametro1 ** 2
    quadrado2 = parametro2 ** 2

    soma = modulo_calculadora.soma(quadrado1, quadrado2)
    hipotenusa = soma ** (0.5)

    return hipotenusa
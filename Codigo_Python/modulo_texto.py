def remove_espacos(texto):
    tamanho = len(texto)
    texto_novo = ""

    contador = 0
    while contador < tamanho:
        letra = texto[contador]

        if letra != chr(32):
            texto_novo = texto_novo + letra.lower()
        contador += 1

    return texto_novo


def eh_palindrome(texto):
    resultado = True
    oxt= ""
    texto = remove_espacos(texto)

    tamanho = len(texto)

    while tamanho > 0:
       oxt = oxt + texto[tamanho-1]
       tamanho -= 1

    if oxt == texto:
        resultado = True
    else:
        resultado = False

    return resultado

"""
Quando geramos uma saída de texto seja para o console ou
para um arquivo podemos inserir o que chamamos de caracteres
"não imprimíveis". Estes são usados para formatar esta saída
e não são visíveis no resultado final mas sim seu efeito.
"""
# Antes é preciso mostrar que é possível reunir textos e caracteres usando o sinal "+"
print("Primeiro texto. " + "A seguir um caracter -> " + 'X' + " <- repare que o resultado final é um texto único.")

# Em alguns casos é necessário reunir outros tipos de dados a textos.
# Neste caso é necessário transformar estes outos tipos de dados em texto.
# Para isso é chamada uma função específica que executa esta transformação e
# retorna um texto equivalente ao conteúdo da variável, isto se chama "casting".

print('\n'+"Impressão de uma variável numérica juntamente com texto.")
texto = "O valor da variável numeral é "
numeral = 150
print(texto + str(numeral))

# Agora sim exemplos de dois "caracteres não imprimíveis"
print('\n' + "* Primeira linha.")
print('\t' + "* Linha com o um espaço de tabulação.")
print("* Terceira linha")
print('\n' + "* Quarta linha com uma quebra de linha antes")
print("* Quinta linha")
print("* Sexta linha com uma quebra de linha após." + '\n')
print("* Sétima linha")
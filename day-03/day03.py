def remover_caracteres_especiais(texto):
    # Remove espaços em branco, pontuações e caracteres especiais
    return ''.join(e for e in texto if e.isalnum())

def remover_acentos(texto):
    # Substitui caracteres acentuados por caracteres sem acento
    import unidecode
    return unidecode.unidecode(texto)

def verificar_palindromo(frase):
    # Converte a frase para letras minúsculas e remove caracteres especiais e acentos
    frase = remover_acentos(frase.lower())
    frase = remover_caracteres_especiais(frase)

    # Inverte a frase
    frase_invertida = frase[::-1]

    # Verifica se a frase invertida é igual à original
    if frase == frase_invertida:
        return True
    else:
        return False

# Solicita ao usuário a entrada da palavra ou frase
entrada = input("Digite uma palavra ou frase: ")

# Verifica se a entrada é um palíndromo e imprime o resultado
if verificar_palindromo(entrada):
    print(f"{entrada} é um palíndromo!")
else:
    print(f"{entrada} não é um palíndromo.")


# Será nescessário instalar o modulo "unicode", para instalar;
# pip install unidecode
    
# def remover_caracteres_especiais(texto):: Define uma função chamada remover_caracteres_especiais que recebe uma string texto como argumento.
# return ''.join(e for e in texto if e.isalnum()): Utiliza list comprehension para manter apenas os caracteres alfanuméricos da string texto e, em seguida, junta esses caracteres de volta em uma string.
# def remover_acentos(texto):: Define uma função chamada remover_acentos que recebe uma string texto como argumento.
# import unidecode: Importa a biblioteca unidecode para remover acentos de caracteres.
# return unidecode.unidecode(texto): Utiliza a função unidecode para remover acentos da string texto.
# def verificar_palindromo(frase):: Define uma função chamada verificar_palindromo que recebe uma string frase como argumento.
# frase = remover_acentos(frase.lower()): Converte a string frase para letras minúsculas e remove acentos.
# frase = remover_caracteres_especiais(frase): Remove espaços em branco, pontuações e caracteres especiais da string frase.
# frase_invertida = frase[::-1]: Inverte a string frase.
# if frase == frase_invertida:: Verifica se a string original é igual à sua versão invertida.
# return True: Retorna True se for um palíndromo.
# return False: Retorna False se não for um palíndromo.
# entrada = input("Digite uma palavra ou frase: "): Solicita ao usuário a entrada da palavra ou frase.
# if verificar_palindromo(entrada):: Chama a função verificar_palindromo com a entrada do usuário e verifica se é um palíndromo.
# print(f"{entrada} é um palíndromo!"): Imprime a mensagem indicando que a entrada é um palíndromo.
# else:: Caso contrário,
#print(f"{entrada} não é um palíndromo."): Imprime a mensagem indicando que a entrada não é um palíndromo.

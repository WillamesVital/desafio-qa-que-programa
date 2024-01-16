def contar_palavras(texto):
    # Usa a função split() para dividir o texto em palavras
    palavras = texto.split()
    
    # Retorna o número de palavras no texto
    return len(palavras)

# Solicita ao usuário a entrada do texto
texto = input("Digite um texto: ")

# Obtém o número de palavras no texto chamando a função contar_palavras
numero_palavras = contar_palavras(texto)

# Imprime o resultado
print(f"O texto possui {numero_palavras} {'palavras' if numero_palavras != 1 else 'palavra'}.")

# def contar_palavras(texto):: Define uma função chamada contar_palavras que recebe uma string texto como argumento.
# palavras = texto.split(): Usa a função split() para dividir o texto em palavras. Por padrão, split() separa o texto nas ocorrências de espaços em branco.
# return len(palavras): Retorna o número de palavras no texto, que é o comprimento da lista de palavras obtidas.
# texto = input("Digite um texto: "): Solicita ao usuário a entrada de um texto.
# numero_palavras = contar_palavras(texto): Chama a função contar_palavras para obter o número de palavras no texto.
# print(f"O texto possui {numero_palavras} {'palavras' if numero_palavras != 1 else 'palavra'}."): Imprime o resultado, considerando a forma plural ou singular da palavra "palavra" com base na contagem.
import random

def gerar_numeros_mega_sena():
    # Inicializa uma lista vazia para armazenar os números
    numeros_mega_sena = []

    # Gera 6 números aleatórios sem repetições
    while len(numeros_mega_sena) < 6:
        numero_aleatorio = random.randint(1, 60)

        # Verifica se o número já foi gerado antes de adicionar à lista
        if numero_aleatorio not in numeros_mega_sena:
            numeros_mega_sena.append(numero_aleatorio)

    # Retorna a lista de números gerados
    return numeros_mega_sena

# Chama a função para gerar os números da Mega Sena
numeros_mega_sena = gerar_numeros_mega_sena()

# Imprime a lista de números gerados
print("Números da Mega Sena:")
print(numeros_mega_sena)

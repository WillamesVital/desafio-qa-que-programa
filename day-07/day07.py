import time

def temporizador_regressivo(tempo_total):
    tempo_restante = tempo_total
    while tempo_restante > 0:
        print(f"Tempo restante: {tempo_restante} segundos")
        time.sleep(1)
        tempo_restante -= 1
    print("Tempo esgotado!")

def contador_progressivo(tempo_total):
    tempo_passado = 0
    while tempo_passado < tempo_total:
        print(f"Tempo passado: {tempo_passado} segundos")
        time.sleep(1)
        tempo_passado += 1
    print("Contagem concluída!")

def main():
    print("Escolha uma opção:")
    print("1. Temporizador Regressivo")
    print("2. Contador Progressivo")

    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1 or escolha == 2:
        tempo_total = int(input("Digite o tempo desejado em segundos: "))

        if escolha == 1:
            temporizador_regressivo(tempo_total)
        else:
            contador_progressivo(tempo_total)
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()

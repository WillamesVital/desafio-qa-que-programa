def km_para_milhas(km):
    return km * 0.621371

def milhas_para_km(milhas):
    return milhas * 1.60934

def metros_para_pes(metros):
    return metros * 3.28084

def pes_para_metros(pes):
    return pes * 0.3048

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função para realizar a conversão de unidades
def converter_unidades():
    print("Escolha a conversão de unidades:")
    print("1. Quilômetros para Milhas")
    print("2. Milhas para Quilômetros")
    print("3. Metros para Pés")
    print("4. Pés para Metros")
    print("5. Celsius para Fahrenheit")
    print("6. Fahrenheit para Celsius")

    escolha = int(input("Digite o número da opção desejada: "))

    if escolha in range(1, 7):
        valor = float(input("Digite o valor a ser convertido: "))

        if escolha == 1:
            resultado = km_para_milhas(valor)
            unidade_origem = "Quilômetros"
            unidade_destino = "Milhas"
        elif escolha == 2:
            resultado = milhas_para_km(valor)
            unidade_origem = "Milhas"
            unidade_destino = "Quilômetros"
        elif escolha == 3:
            resultado = metros_para_pes(valor)
            unidade_origem = "Metros"
            unidade_destino = "Pés"
        elif escolha == 4:
            resultado = pes_para_metros(valor)
            unidade_origem = "Pés"
            unidade_destino = "Metros"
        elif escolha == 5:
            resultado = celsius_para_fahrenheit(valor)
            unidade_origem = "Celsius"
            unidade_destino = "Fahrenheit"
        elif escolha == 6:
            resultado = fahrenheit_para_celsius(valor)
            unidade_origem = "Fahrenheit"
            unidade_destino = "Celsius"

        print(f"{valor} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}.")
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 6.")

# Chama a função para converter unidades
converter_unidades()

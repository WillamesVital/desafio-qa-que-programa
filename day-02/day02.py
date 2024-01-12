# Solicita ao usuário que insira o primeiro número
num1_str = input("Digite o primeiro número: ")

# Converte a entrada do usuário para um número float
num1 = float(num1_str)

# Solicita ao usuário que escolha a operação desejada
operacao = input("Escolha a operação (+, -, *, /): ")

# Solicita ao usuário que insira o segundo número
num2_str = input("Digite o segundo número: ")

# Converte a entrada do usuário para um número float
num2 = float(num2_str)

# Realiza a operação escolhida
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    # Verifica se o segundo número é zero para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Não é possível dividir por zero.")
        resultado = None  # Define resultado como None em caso de erro
else:
    print("Operação inválida.")
    resultado = None  # Define resultado como None em caso de operação inválida

# Exibe o resultado se não houver erros
if resultado is not None:
    print(f"O resultado da operação é: {resultado}")







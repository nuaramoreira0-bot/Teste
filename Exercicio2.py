def verifica_fibonacci(numero):
    if numero < 0:
        print(f"O número {numero} é negativo e não pertence à sequência de Fibonacci padrão.")
        return
    if numero == 0 or numero == 1:
        print(f"O número {numero} **PERTENCE** à sequência de Fibonacci.")
        return
    a, b = 0, 1
    while a < numero:
        proximo_termo = a + b
        a = b
        b = proximo_termo
    if a == numero:
        print(f"O número {numero} **PERTENCE** à sequência de Fibonacci!")
    else:
        print(f"O número {numero} **NÃO PERTENCE** à sequência de Fibonacci.")

numero_alvo_a = 55
print(f"Verificação para o número {numero_alvo_a}:")
verifica_fibonacci(numero_alvo_a)

print("-" * 30)
numero_alvo_b = 6
print(f"Verificação para o número {numero_alvo_b}:")
verifica_fibonacci(numero_alvo_b)

print("-" * 30)

try:
    entrada = input("Digite um número inteiro positivo para verificar na sequência de Fibonacci: ")
    numero_alvo_c = int(entrada)
    print(f"Verificação para o número {numero_alvo_c}:")
    verifica_fibonacci(numero_alvo_c)
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
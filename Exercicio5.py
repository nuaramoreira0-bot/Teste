def inverte_string(s):
    caracteres = list(s)
    i = 0
    j = len(caracteres) - 1

    while i < j:
        temp = caracteres[i]
        caracteres[i] = caracteres[j]
        caracteres[j] = temp


        i += 1
        j -= 1

    string_invertida = "".join(caracteres)

    return string_invertida

string_original_1 = "Target Sistemas"
resultado_1 = inverte_string(string_original_1)

print(f"Original (1): {string_original_1}")
print(f"Invertida (1): {resultado_1}")

print("-" * 30)

try:
    string_original_2 = input("Digite a string que deseja inverter: ")
    resultado_2 = inverte_string(string_original_2)

    print(f"Original (2): {string_original_2}")
    print(f"Invertida (2): {resultado_2}")

except EOFError:
    print("\n[Não foi possível ler a entrada do usuário neste ambiente.]")
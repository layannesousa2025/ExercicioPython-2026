numero = int(input("Digite um número: "))

soma = 0
i = 1

while i < numero:
    if numero % i == 0:
        soma += i
    i += 1

if soma == numero:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")

# Função que calcula a média ponderada de duas notas
def media_ponderada(nota1, nota2, peso1, peso2):
    return ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)


# Exemplo de uso
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

# Calcula a média ponderada
resultado = media_ponderada(nota1, nota2, peso1, peso2)
print("A média ponderada é:", resultado)

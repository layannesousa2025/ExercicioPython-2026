
# Programa que calcula a média de duas notas
numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))

# Função que calcula a média de duas notas
def media (nota1,nota2):
    media = (nota1 + nota2) / 2
    return media


#printa a média das notas
print("A média das notas é:", media(numero1, numero2))
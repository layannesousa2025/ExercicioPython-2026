# Função que calcula o valor do desconto
def valor_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    return desconto


# Exemplo de uso
preco = float(input("Digite o valor do item: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcula o valor do desconto
desconto = valor_desconto(preco, percentual_desconto)
print("O valor do desconto é: R$", desconto)

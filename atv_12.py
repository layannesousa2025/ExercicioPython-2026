fatorial= 1

n= int(input("Digite um número: "))
for i in range(1,n+1):
    fatorial*=i
print("O fatorial de", n, "é", fatorial)
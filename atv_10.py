numero = 2

while numero <= 78000:
    divisor = 2
    primo = True

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1

    if primo:
        print(numero)

    numero += 1
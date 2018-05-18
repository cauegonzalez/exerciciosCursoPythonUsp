numero = int(input("Digite um número inteiro: "))

ePrimo = False
i = 1
div = 0

while (i <= numero) and (div < 3):
    if (numero % i == 0):
        div = div + 1
    i = i + 1

if (div == 2):
    ePrimo = True;

if (ePrimo):
    print('primo')
else:
    print('não primo')
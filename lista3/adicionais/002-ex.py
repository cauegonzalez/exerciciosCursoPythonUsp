import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b **2 - 4 * a * c)

if delta < 0:
    print('esta equação não possui raízes reais')
else:
    raiz = ((b * -1) + math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print('a raiz desta equação é', raiz)
    else:
        raiz2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
        if raiz2 > raiz:
            print('as raízes da equação são', raiz,'e',raiz2)
        else:
            print('as raízes da equação são', raiz2,'e',raiz)
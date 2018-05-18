import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b **2 - 4 * a * c)

print ('delta = ',delta)

if delta < 0:
    if b > 0:
        if (c > 0):
            print('A equação ', a,'x^2 +', b,'x +', c,'não possui raiz real')
        else:
            print('A equação ', a,'x^2 +', b,'x', c,'não possui raiz real')
    else:
        if (c > 0):
            print('A equação ', a,'x^2', b,'x +', c,'não possui raiz real')
        else:
            print('A equação ', a,'x^2', b,'x', c,'não possui raiz real')
elif delta == 0:
    raiz = ((b * -1) + math.sqrt(delta)) / (2 * a)
    if b > 0:
        if (c > 0):
            print('A equação ', a,'x^2 +', b,'x +', c,'possui a raiz', raiz)
        else:
            print('A equação ', a,'x^2 +', b,'x', c,'possui a raiz', raiz)
    else:
        if (c > 0):
            print('A equação ', a,'x^2', b,'x +', c,'possui a raiz', raiz)
        else:
            print('A equação ', a,'x^2', b,'x', c,'possui a raiz', raiz)
else:
    raiz = ((b * -1) + math.sqrt(delta)) / (2 * a)
    raiz2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
    if b > 0:
        if (c > 0):
            print('A equação ', a,'x^2 +', b,'x +', c,'possui as raizes', raiz,'e',raiz2)
        else:
            print('A equação ', a,'x^2 +', b,'x', c,'possui as raizes', raiz,'e',raiz2)
    else:
        if (c > 0):
            print('A equação ', a,'x^2', b,'x +', c,'possui as raizes', raiz,'e',raiz2)
        else:
            print('A equação ', a,'x^2', b,'x', c,'possui as raizes', raiz,'e',raiz2)
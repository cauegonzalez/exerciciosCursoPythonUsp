import math

def calculaDelta(a, b, c):
    return (b **2 - 4 * a * c)

def bhaskara(a, b, delta):
    raiz = ((b * -1) + math.sqrt(delta)) / (2 * a)
    return raiz

def bhaskara2(a, b, delta):
    raiz = ((b * -1) - math.sqrt(delta)) / (2 * a)
    return raiz

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = calculaDelta(a, b, c)

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
    raiz = bhaskara(a, b, delta)
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
    raiz = bhaskara(a, b, delta)
    raiz2 = bhaskara2(a, b, delta)
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
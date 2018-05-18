import math

def soma_hipotenusas(x):
    i = 0
    soma = 0
    while i <= x:
        if é_hipotenusa(i):
            soma = soma + i
        i = i + 1
    return soma

def é_hipotenusa(h):
    i = 1

    while i < h:
        a = math.sqrt(h**2 - i**2)
        b = math.sqrt(h**2 - a**2)

        if ((a - int(a)) == 0.0) and ((b - int(b)) == 0.0):
            return True

        i = i + 1

    return False

def test_soma_hipo():
    assert soma_hipotenusas(25) == 105
    assert soma_hipotenusas(26) == 131

def test_hipo():
    assert é_hipotenusa(5) == True
    assert é_hipotenusa(1) == False
    assert é_hipotenusa(26) == True

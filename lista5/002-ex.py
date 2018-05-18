def ePrimo(numero):
    i = 1
    div = 0

    while (i <= numero) and (div < 3):
        if (numero % i == 0):
            div = div + 1
        i = i + 1

    if (div == 2):
        return True
    return False

def maior_primo(n):
    if (ePrimo(n)):
        return n

    i = n
    while (i > 1):
        i = i - 1
        if (ePrimo(i)):
            return i

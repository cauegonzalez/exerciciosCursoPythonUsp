def isPrimo(x):
    fator = 2
    while x % fator != 0 and fator < x / 2:
        fator = fator + 1
    if x > 2 and x % fator == 0:
        return False
    else:
        return True

def n_primos(n):
    i = 2
    quantidadePrimos = 0

    while i > 1 and i <= n:
        if isPrimo(i):
            quantidadePrimos = quantidadePrimos + 1
        i = i + 1

    return quantidadePrimos

def isPrimo(x):
    fator = 2
    while x % fator != 0 and fator < x / 2:
        fator = fator + 1
    if x > 2 and x % fator == 0:
        return False
    else:
        return True

n = 2

while n > 1:
    n = int(input('Digite um número inteiro > 1 (ou 1 para sair): '))

    if isPrimo(n):
        print('{} é primo!'.format(n))
    else:
        print('{} não é primo!'.format(n))

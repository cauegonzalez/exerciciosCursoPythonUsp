def calculoBinomial(n, k):
    return fatorial(n)/(fatorial(k) * fatorial(n - k))

def fatorial(n):
    if (n == 1) or (n == 0):
        return 1
    return fatorial(n - 1) * n

n = int(input('Digite o número inteiro n: '))
k = int(input('Digite o número inteiro k: '))

print(calculoBinomial(n, k))

lista = []
n = int(input('Digite um número: '))
while n != 0:
    lista.append(n)
    n = int(input('Digite um número: '))

print()
i = len(lista)

while i > 0:
    print(lista[i-1])
    i = i - 1
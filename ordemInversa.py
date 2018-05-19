
lista = []
n = int(input('Digite um número (zero para parar): '))
while n != 0:
    lista.append(n)
    n = int(input('Digite um número (zero para parar): '))


i = len(lista)

while i > 0:
    print(lista[i-1], end = ', ')
    i = i - 1
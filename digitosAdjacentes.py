numero = int(input('Digite um número inteiro: '))

encontrouAdjacenteIgual = False
primeiro = numero % 10

while numero != 0 and not encontrouAdjacenteIgual:
    numero = numero // 10
    segundo = numero % 10

    if (primeiro == segundo):
        encontrouAdjacenteIgual = True
    else:
        primeiro = segundo

if encontrouAdjacenteIgual:
    print('Neste número existem 2 dígitos adjacentes iguais:', primeiro, segundo)
else:
    print('Neste número não existem 2 dígitos adjacentes iguais')
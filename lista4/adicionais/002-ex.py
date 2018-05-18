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
    print('sim')
else:
    print('não')
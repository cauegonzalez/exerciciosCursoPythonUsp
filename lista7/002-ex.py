largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

i = j = 1
while i <= altura:
    while j <= largura:
        if i == 1 or i == altura or j == 1 or j == largura:
            print('#', end = '')
        else:
            print(' ', end = '')
        j = j + 1
    print()
    j = 1
    i = i + 1
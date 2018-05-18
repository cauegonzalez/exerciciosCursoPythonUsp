def troca(x, y):
    aux = x
    x = y
    y = aux

# x = 10
# y = 20
# troca (x,y)
# print("x =", x,"e y =",y)

def desenha(linha):
    while linha > 0:
        coluna = 1
        while coluna <= linha:
            print('*', end = "")
            coluna = coluna + 1
        print()
        linha = linha - 1

# desenha(5)

# x = 2
# cont = 0
# while x >= 0:
#     y = 0
#     while y <= 4:
#         cont = cont + 1
#         y = y - 1
#     x = x - 1

x = 2
cont = 0
while x >= 0:
    y = 0
    while y >= 4:
        cont = cont + 1
        #comando qualquer
        y = y + 1
    x = x - 1

print(cont)
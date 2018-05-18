import math

x1 = int(input('Digite o número correspondente à coordenada x do primeiro ponto: '))
y1 = int(input('Digite o número correspondente à coordenada y do primeiro ponto: '))
x2 = int(input('Digite o número correspondente à coordenada x do segundo ponto: '))
y2 = int(input('Digite o número correspondente à coordenada y do segundo ponto: '))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if (distancia > 10):
    print('longe')
else:
    print('perto')
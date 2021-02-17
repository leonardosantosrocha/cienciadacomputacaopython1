import math

x1 = int(input('Digite X1: '))
y1 = int(input('Digite Y1: '))
x2 = int(input('Digite X2: '))
y2 = int(input('Digite Y2: '))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if distancia >= 10:
    print('longe')
else:
    print('perto')
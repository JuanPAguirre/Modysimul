g = int(input('Ingrese un valor positivo para g: '))
k = int(input('Ingrese un valor positivo para k: '))
X0 = int(input('Ingrese un valor inicial impar: '))
iteraciones = int(input('Ingrese el número de iteraciones: '))

while g < 0:
    g = int(input("g es negativo, ingrese un valor positivo para g: "))

while k < 0:
    k = int(input("k es negativo, ingrese un valor positivo para k: "))

while X0 % 2 == 0 or X0 < 0:
    X0 = int(input("X0 es par o negativo, ingrese un valor inicial impar: "))

m=2**g
#Aca se selecciona con que a se desea trabajar si con +3 o +5
#a=8*k+3
a=8*k+5

for i in range(iteraciones):
    X=X0
    X0=(a*X0)%m
    r=X0/(m-1)

    print('X' + str(i+1) + ' = ' + str(X0) + ' |  r' + str(i+1) + ' = ' + str(r)) 

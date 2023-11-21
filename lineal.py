g = int(input('Ingrese un valor positivo para g: '))
k = int(input('Ingrese un valor positivo para k: '))
c = int(input('Ingrese un valor positivo para c (No puede ser divisible por 2): '))
X0 = int(input('Ingrese el valor inicial: '))
iteraciones = int(input('Ingrese el número de iteraciones: '))

while g < 0:
    g = int(input("g es negativo, ingrese un valor positivo para g: "))

while k < 0:
    k = int(input("k es negativo, ingrese un valor positivo para k: "))

while c % 2 == 0 or c < 0:
    c = int(input("c es divisible por 2 o es negativo, ingrese un valor para c: "))

while X0 < 0:
    X0 = int(input("X0 es negativo, ingrese un valor inicial: "))

m=2**g
a=4*k+1

for i in range(iteraciones):
    X=X0
    X0=(a*X+c)%m
    r=X0/(m-1)

    print('X' + str(i+1) + ' = ' + str(X0) + ' |  r' + str(i+1) + ' = ' + str(r)) 

g = int(input('Ingrese el valor de g: '))
c = int(input('Ingrese un valor impar positivo para c: '))
a = int(input('Ingrese un valor par positivo para a: '))
b = int(input('Ingrese un valor positivo para b (cumpliendo que: (b-a)mod(4)=1): '))
X0 = int(input('Ingrese el valor inicial < m: '))
iteraciones = int(input('Ingrese el número de iteraciones: '))

m=2**g

while c % 2 == 0 or c < 0:
    c = int(input("c es par o negativo, ingrese un valor impar positivo: "))

while a % 2 !=0 or a < 0:
    a = int(input("a es impar o negativo , ingrese un valor par: "))

while (b - a) % 4 != 1 or b < 0:
    b = int(input("b no cumple la condición o es negativo, ingrese un valor positivo para b (cumpliendo que: (b-a)mod(4)=1): "))

while X0 > m or X0 < 0:
    X0 = int(input("X0 no es mayor a m o es negativo, ingrese un valor inicial < m: "))

for i in range(iteraciones):
    X0=(a*X0**2 + b*X0 + c)%m
    r=X0/(m-1)

    print('X' + str(i+1) + ' = ' + str(X0) + ' |  r' + str(i+1) + ' = ' + str(r)) 

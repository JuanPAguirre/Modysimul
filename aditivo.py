m = int(input('Ingrese el valor de m: '))
print('Ingrese los 5 valores semillas:')
X0 = int(input('X0: '))
X1 = int(input('X1: '))
X2 = int(input('X2: '))
X3 = int(input('X3: '))
X4 = int(input('X4: '))
iteraciones = int(input('Ingrese el número de iteraciones: '))

for i in range(iteraciones):
    X=(X0+X4)%m
    r=X/(m-1)
    print('X' + str(i+1) + ' = ' + str(X) + ' |  r' + str(i+1) + ' = ' + str(r)) 
    X0=X1
    X1=X2
    X2=X3
    X3=X4
    X4=X

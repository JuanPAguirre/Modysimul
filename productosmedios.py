X0 = int(input('Ingrese el 1er valor de 4 dígitos: '))
X1 = int(input('Ingrese el 2do valor de 4 dígitos: '))
D = int(input('Ingrese la cantidad de dígitos: '))
iteraciones = int(input('Ingrese el número de iteraciones: '))
i=0
for i in range(iteraciones):
    X=X0*X1
    Xlen = len(str(X))
    
    if Xlen == 8:
        s = str(X)
        t = s[2:6]
        v = int(t)
        r = v/(10**D)
    else:
        if Xlen != 8:
            s = str(X)
            t = s[2:6]
            v = int(t)
            r = v/(10**D)
    print('Y' + str(i+1) + ' = ' + str(X) + ' | X' + str(i+1) + ' = ' + str(v) + ' | r' + str(i+1) + ' = ' + str(r))   
    X0=X1
    X1=v
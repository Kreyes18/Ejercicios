##Diseñe un algoritmo e impleméntelo con Python para resolver sistemas de
##ecuaciones lineales 2x2. Su programa debe recibir los coeficientes de las
##2 ecuaciones, verificar si tiene solución y mostrar el resultado de sus raíces.
Eleccion='si'
while Eleccion=='si':
    print('Calculadora de sistemas de ecuaciones lineales')
    op=int(input('Ingrese el numero de la operacion deseada\n1.Sistema 2x2\n2.Salir\n'))
    match op:
        case 1:
            a=float(input('De la primera ecuacion ingrese el numero que acompaña la x(Ax+-By=c):'))
            b=float(input('De la primera ecuacion ingrese el numero que acompaña la y(Ax+-By=c):'))
            c=float(input('De la primera ecuacion ingrese el numero c(Ax+By=c):'))
            d=float(input('De la segunda ecuacion ingrese el numero que acompaña la x(Ax+-By=c):'))
            e=float(input('De la segunda ecuacion ingrese el numero que acompaña la y(Ax+-By=c):'))
            f=float(input('De la segunda ecuacion ingrese el numero c(Ax+By=c):'))
            det=(a*e)-(b*d)
            if det==0:
                print('El sistema tiene infinitas soluciones o no tiene solucion')
                
            else:
                x=((c*e)-(f*d))/det
                y=((f*a)-(c*b))/det
                print('El valor de x en este sistema es:',x,' y el valor de y es:',y)
            Eleccion=input('Si desea seguir utilizando la calculadora ingrese Si\n')
            Eleccion=Eleccion.lower()
        case 2:
            print('Saliendo del programa.....')
            exit()
        case _:
            print('Incorrecta eleccion saliendo del programa')
            exit()

a='si'
while a=='si':
    op=int(input('Bienvenido al sistema que tipo de circuito es\n1.Serie\n2.Paralelo\n3.Salir\n'))
    match op:
        case 1:
            resis=[]
            n=int(input('Digite el numero de resistencias(minimo 2):'))
            while n<2:
                n=int(input('Digite el numero de resistencias(minimo 2):'))
            DC=float(input('Digite el valor de la fuente de voltaje en voltios:'))
            for i in range(n):
                print('Digite el valor de la resistencia en ohms ',i+1)
                resi=float(input())
                resis.append(resi)
            rest=sum(resis)
            Corri=DC/resis[0]
            print('El valor de la resistencia equivalente es en ohms: ',rest,' , el valor de la potencia es en voltios:',DC,' y el valor de la corriente es en amperios:',Corri)
            t=float(input('Para la energia consumida digite el tiempo trasncurrido en minutos:'))
            Ener=DC*t
            print('El valor de la energia es:',Ener)
            a=input('Si desea seguir digite si')
            a=a.lower()
        case 2:
            resis=[]
            resi=0
            n=int(input('Digite el numero de resistencias(minimo 2):'))
            while n<2:
                n=int(input('Digite el numero de resistencias(minimo 2):'))
            DC=float(input('Digite el valor de la fuente de voltaje en voltios:'))
            for i in range(n):
                print('Digite el valor de la resistencia en ohms ',i+1)
                resi+=1/float(input())
                resis.append(resi**-1)
            rest=resi**-1
            Corri=DC/resis[0]
            print('El valor de la resistencia equivalente es en ohms: ',rest,' , el valor de la potencia es en voltios:',DC,' y el valor de la corriente es en amperios:',Corri)
            t=float(input('Para la energia consumida digite el tiempo trasncurrido en minutos:'))
            Ener=DC*t
            print('El valor de la energia es:',Ener)
            a=input('Si desea seguir digite si')
            a=a.lower()
        case 3:
            print('Saliendo del programa')
            exit()
        case _:
            print('Saliendo del programa')
            exit()

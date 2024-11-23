import csv

def csv1mostrar():
    with open('csv1.csv', 'r',  newline='') as csv1:
        mostrar=csv.reader(csv1, delimiter=';')
        for i in mostrar:
            print(f'CODIGO:{i[0]},NOMBRE:{i[1]},EDAD:{i[2]}')

def csv2mostrar():
    with open('csv2.csv', 'r',  newline='') as csv2:
        mostrar=csv.reader(csv2, delimiter=';')
        for i in mostrar:
            print(f'CODIGO:{i[0]},NOMBRE:{i[1]},EDAD:{i[2]}')

def csv3mostrar():
    with open('csv3.csv', 'r',  newline='') as csv3:
        mostrar=csv.reader(csv3, delimiter=';')
        for i in mostrar:
            print(f'CODIGO:{i[0]},NOMBRE:{i[1]},EDAD:{i[2]}')

def csv1():
    with open('csv1.csv', 'a',  newline='') as i:
        escri=csv.writer(i, delimiter=';') 
        CODIGO=input('Digite el codigo del estudiante: \n')  
        NOMBRE=input('Digite el nombre del estudiante: \n')
        EDAD=int(input('Digite la edad del estudiante: \n'))
        escri.writerow([CODIGO,NOMBRE,EDAD])
    print('Datos almacenados con éxito\n')
    opc=input('Digite:\n\t1.Para añadir otro elemto\n\t2.Para ver el csv\n\t3.Salir al menu: \n')
    if(opc=='1'):
            with open('csv1.csv', 'a',  newline='') as i:
                csv1()
    elif(opc=='2'):
        csv1mostrar()
    elif(opc=='3'):
        menu()

def csv2():
    with open('csv2.csv', 'r',  newline='') as csv2:
        mostrar=csv.reader(csv2, delimiter=';')
        for i in mostrar:
            print(f'CODIGO:{i[0]},NOMBRE:{i[1]},EDAD:{i[2]}')
    opc=input('Digite:\n\t1.Para ver de nuevo el csv\n\t2.Salir:\n')
    if opc=='1':
        csv2mostrar()
    elif opc=='2':
        menu()

def csv3():
        # Leer las filas del archivo CSV
    with open('csv3.csv', 'r', newline='') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=';')
        filas = list(lector)  # Convertir las filas en una lista para modificar

    # Modificar el valor
    elemento_amodificar=input('Digite el nombre a modificar: \n')
    for fila in filas:  # Iterar sobre cada fila
        if fila[1] == elemento_amodificar: 
            elemento = input('Digite el nuevo nombre:\n')
            fila[1] = elemento  # Modificar el nombre
            print('Nombre registrado')
            break  # Terminar la búsqueda después de la primera coincidencia
        else:
            print('Nombre no encontrado')
            csv3()

    # Sobrescribir el archivo CSV con los datos modificados
    with open('csv3.csv', 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv, delimiter=';')
        escritor.writerows(filas)  # Sobrescribir con las filas modificadas
        opc=input('Digite:\n\t1.Para ver el csv\n\t2.Salir\n')
    if opc=='1':
        csv3mostrar()
    elif opc=='2':
        menu()

def menu():
    while True:
        opc=input('Digite:\n\t1.para hacer el csv1\n\t2.para ver el csv2\n\t3.para modificar el csv3\n') 
        if(opc=='1'):
            csv1()
        elif(opc=='2'):
            csv2()
        elif(opc=='3'):
            csv3()
        else:
            print('opcion incorrecta')


while True:
    menu()
import csv

admin = {"admin":'1234'}
profes = {}
estudiantes = {}
asignaturas =[]

def Academico():
    print("Bienvenido a academico")
    h_usuarios = int(input("Marque para crear \n1. Profes \n2. Estudiantes \n3. Asignaturas\n"))
    if h_usuarios == 1:
        with open('ejemplo9.csv','a', newline='',) as i:
            escri=csv.writer(i,delimiter=';')
            usu =input("Ingrese el nuevo usuario: ")
            contra = int(input("Ingrese la contraseña para el nuevo usuario: "))
            profes[usu]=contra
            escri.writerow([usu,contra])
        print("Usuario almacenado")
        Academico()
    elif h_usuarios==2:
        with open('ejemplo9.csv','a', newline='',) as i:
            escri=csv.writer(i,delimiter=';')
            usu =input("Ingrese el nuevo usuario: ")
            contra = int(input("Ingrese la contraseña para el nuevo usuario: "))
            estudiantes[usu]=contra
            escri.writerow([usu,contra])
        print("Usuario almacenado")
        Academico()
    elif h_usuarios==3:
        with open('asigejemplo9.csv','a', newline='',) as i:
            escri=csv.writer(i,delimiter=';')
            asig =input("Ingrese la nueva asignatura: ")
            asignaturas.append(asig)
            escri.writerow([asig])
        print("Asignatura almacenada")
        Academico()
    else:
        exit()
def Convivencia():
    print("Convivencia")


def Biblioteca ():
    print("biblioteca")

def Votaciones():
    print("Bienvenido a votaciones")
    Opcion=int(input('Que desea hacer: \n1.Abrir/Cerrar votaciones\n2.Ingresar candidatos\n'))
    if Opcion==1:
        Abrir=0
    elif Opcion==2:
        with open('votacion.csv','a', newline='',) as i:
            escri=csv.writer(i,delimiter=';')
            Candi =input("Ingrese un nuevo candidato: ")
            asignaturas.append(Candi)
            escri.writerow([Candi])


def Acceso():
    print('Bienvenido al menú de acceso: \n1. Administrativo \n2. Profe \n3. Estudiante\n')
    opcion = int(input())
    if opcion == 1:
        print("Bienvenido Admin")
        usu = input("Ingrese su usuario: ")
        contra = input("Ingrese su contraseña: ")
        if usu in admin and contra == admin[usu]:
            print("ok")
            modulo = int(input("A que modulo quiere ir: \n1. Academico\n2. Votaciones \n4. Biblioteca\n"))
            if modulo ==1:
                Academico()
            elif modulo ==2:
                Votaciones()
            elif modulo == 3:
                Biblioteca()
            else:
                print("Dato erroneo")
                
        else:
            print("Dato erroneo")
Acceso()
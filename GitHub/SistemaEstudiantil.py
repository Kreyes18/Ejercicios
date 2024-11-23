import csv

admin = {"admin":1234}
profes = {}
estudiantes = {}
asignaturas =[]

def Academico():
    print("acad")
    h_usuarios = int(input("Marque 1. Profes 2. Estudiantes 3. Asignaturas"))
    if h_usuarios == 1:
        h_usuarios=int(input('Marque \n1.Nuevo Usuario\n2.Usuario existente'))
        if h_usuarios == 1:
            usu =input("Ingrese el nuevo usuario: ")
            contra = int(input("Ingrese la contraseña para el nuevo usuario: "))
            profes[usu]=contra
            print("Usuario almacenado")
        else:
            usu=input('Ingrese su usuario')
            contra = int(input('Ingrese su contraseña'))
            if usu in profes and contra== profes(usu):
                print("ok")
                modulo = int(input("A que modulo quiere ir: 1. Academico, 2. Convivencia 3. Votaciones 4. Biblio"))
                if modulo ==1:
                    Academico()
                elif modulo ==2:
                    Convivencia()
                elif modulo ==3:
                    Votaciones()
                elif modulo == 4:
                    Biblioteca()
                else:
                    print("Dato erroneo")
        Academico()
        

def Convivencia():
    print("Convivencia")


def Biblioteca ():
    print("biblioteca")

def Votaciones():
    print("Votaciones")

def Acceso():
    print('Bienvenido al menú de acceso: 1. Administrativo 2. Profe 3. Estudiante')
    opcion = int(input())
    if opcion == 1:
        print("Bienvenido Admin")
        usu = input("Ingrese su usuario: ")
        contra = int(input("Ingrese su contraseña: "))
        if usu in admin and contra == admin[usu]:
            print("ok")
            modulo = int(input("A que modulo quiere ir: 1. Academico, 2. Convivencia 3. Votaciones 4. Biblio"))
            if modulo ==1:
                Academico()
            elif modulo ==2:
                Convivencia()
            elif modulo ==3:
                Votaciones()
            elif modulo == 4:
                Biblioteca()
            else:
                print("Dato erroneo")
                
        else:
            print("Dato erroneo")
        
Acceso()
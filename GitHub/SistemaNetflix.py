import csv
k_usua={'k_admin':'1234Kr'}
k_perf={}
import re

def validar_contraseña(contraseña):
    # Expresión regular para verificar que la contraseña tiene 6 caracteres, incluyendo al menos una letra y un número
    patron = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6}$'
    return re.match(patron, contraseña) is not None
def k_agregarcontenido():
    with open('contenido.csv','a', newline='',) as i:
            escri=csv.writer(i,delimiter=';')
            k_nombre =input("Ingrese el nombre : ")
            k_genero=input('Ingrese el genero: ')
            escri.writerow([k_nombre,k_genero])
    print("Pelicula o serie almacenada")
def k_menuadmin():
    print("Bienvenido")
    k_b=int(input('Digite que quiere hacer \n1.Agregar contenido\n2.Eliminar contenido\n3.Actualizar contenido\n'))
    if k_b==1:
        k_agregarcontenido()
    elif k_b==2:
        k_eliminar=1
    elif k_b==3:
        k_actualizarcont=1
def k_iniciar():
    k_a=int(input('1.Usuario\n2.Admin\n'))
    if k_a==1:
        k_ing = input("Ingrese su usuario o correo: ")
        k_contra = input("Ingrese su contraseña: ")
        if (k_ing in k_usua or k_ing in k_usua) and k_contra == k_usua[k_ing]:
            print("Bienvenido")
            k_ini()
    elif k_a==2:
        k_admin = input("Ingrese su usuario o correo: ")
        k_contra = input("Ingrese su contraseña: ")
        if k_admin in k_usua and k_contra == k_usua[k_admin]:
            k_menuadmin()
        else:
            k_iniciar()
    else:
        menu()
def k_crear():
    with open('usuarios.csv','a', newline='',) as i:
            escri=csv.writer(i,delimiter=';')
            k_usu =input("Ingrese su nombre : ")
            k_correo=input('Ingrese su correo: ')
            k_contra = input("Ingrese la contraseña para el nuevo usuario(6 caracteres entre numeros y letras): ")
            validar_contraseña(k_contra)
            while True:
                contraseña = input("Ingresa una contraseña (6 caracteres, al menos una letra y un número): ")
                if validar_contraseña(contraseña):
                    print("Contraseña válida")
                    break
                else:
                    print("Contraseña inválida. Inténtalo de nuevo.")
            k_usua[k_usu]=k_contra
            k_usua[k_correo]=k_contra
            escri.writerow([k_usu,k_contra,k_correo])
    print("Usuario almacenado")
    menu()
def k_pagos():
    k_a=int(input('Que desea hacer \n1.Planes de subcricion\n2.Sistema de pagos\n3.Historial de pagos'))
    if k_a==1:
        k_c=int(input('Que plan deseas ver \n1.Estandar\n2.Medio rico\n3.Millonario'))
        if k_c==1:
            print('Este plan te deja visualizar las peliculas o series que superen los 30 dias de lanzamiento')
            print('Este plan tiene un valor de $5000')
        elif k_c==2:
            print('Este plan te permite ver cualquier pelicula o serie en nuestro repertorio pero no a la maxima calidad')
            print('Este plan tiene un valor de $50000')
        elif k_c==3:
            print('Este paquete cuenta con la maxima calidad y todo nuestro repertorio ademas de 3 meses de suscripcion al curso de programacion del profe hector')
            print('Este plan tiene un valor de $100000')
    elif k_a==2:
        print('En Protflix existen diferentes metodos de pago como lo son credito y debito')
        k_b=int(input('1.Credito\n2.Debito\n'))
        if k_b==1:
            k_num=int('Digite el numero de tarjeta')
            k_clave=int(input('Digite la clave'))
            k_fecha=int(input('Digite la fecha'))
            print('CUIDADO NO TE ALCANZA PARA PAGAR NINGUNA SUBCRICION REVISA Y TU CARTERA')
        elif k_b==2:
            k_num=int('Digite el numero de tarjeta')
            k_clave=int(input('Digite la clave'))
            k_fecha=int(input('Digite la fecha'))
            print('CUIDADO NO TE ALCANZA PARA PAGAR NINGUNA SUBCRICION REVISA Y TU CARTERA')
    elif k_a==3:
        print('Su ultimo pago fue el XX/XX/XXXX por un valor de $3000')
def k_menuper():
    k_a=int(input('A donde se dirige\n1.Pagos\n2.Busqueda\n3.Salir de Protflix'))
    if k_a==1:
        k_pagos()
    elif k_a==2:
        k_busqueda=1
    elif k_a==3:
        print('Saliendo del programa')
        exit()
    else:
        exit()
def k_admini():
    with open('perfiles.csv','a', newline='',) as i:
            k_a=int(input('Marque la opcion deseada\n1.Crear perfil\n2.Iniciar perfil\n'))
            if k_a==1:
                escri=csv.writer(i,delimiter=';')
                k_per =input("Ingrese el nombre : ")
                k_contraper = input("Ingrese la contraseña para el perfil del 6 caracteres entre numeros y letras: ")
                validar_contraseña(k_contraper)
                while True:
                    contraseña = input("Ingresa una contraseña (6 caracteres, al menos una letra y un número): ")
                    if validar_contraseña(contraseña):
                        print("Contraseña válida")
                        break
                    else:
                        print("Contraseña inválida. Inténtalo de nuevo.")
                k_perf[k_per]=k_contraper
                escri.writerow([k_per,k_contraper])
                print("Perfil almacenado")
            elif k_a==2:
                print("Bienvenido usuario")
                k_per = input("Ingrese el perfil: ")
                k_contraper = input("Ingrese su contraseña: ")
                if k_per in k_perf  and k_contraper == k_perf[k_per]:
                    print("Bienvenido")
                    k_menuper()
                else:
                    print('Datos erroneos,volviendo al menu')
                    k_admini()
            else:
                print('Datos erroneos,volviendo al menu')
                k_admini()
def k_actualizar():
    k_a=int(input('Decida que quiere actualizar\n1.Correo\n2.Contraseña'))
    if k_a==1:
        k_correonue=input('Escriba el correo nuevo')
        if k_correo in k_usua:
            k_correo=k_correonue
        k_ini()
    elif k_a==2:
        k_contranue=input('Escriba la contraseña nueva')
        validar_contraseña(k_contranue)
        while True:
            contraseña = input("Ingresa una contraseña (6 caracteres, al menos una letra y un número): ")
            if validar_contraseña(contraseña):
                print("Contraseña válida")
                if k_contra in k_usua:
                    k_contra=k_contranue
                    k_ini()
            else:
                print("Contraseña inválida. Inténtalo de nuevo.")
def k_elimi():
    k_a=int(input('Esta seguro de eliminar la cuenta\n1.Si\n2.No'))
    if k_a==1:
        k_usu=input('Digite su usuario')
        k_correo=input('Digite su correo')
        k_usua.pop(k_usu)
        k_usua.pop(k_correo)
        print('Cuenta eliminada')
    elif k_a==2:
        print('Dirigiendo a el menu')
        k_ini()
def k_ini():
    k_a=int(input('Marque la opcion deseada\n1.Administracion de perfiles\n2.Actualizar informacion\n3.Eliminar cuenta'))
    if k_a==1:
        k_admini()
    elif k_a==2:
        k_actualizar()
    elif k_a==3:
        k_elimi()
    else:
        print('dato erroneo volviendo al menu')
        k_ini()
def menu():
    k_op=1
    while k_op==1:
        k_a=int(input('Bienvenido a Protflix\n1.Crear Usuario\n2.Iniciar sesion\n3.Salir\n'))
        if k_a==1:
            k_crear()
        elif k_a==2:
            k_iniciar()
        elif k_a==3:
            exit()
        else:
            print('Dato erroneo vuelva a intentarlo')
menu()
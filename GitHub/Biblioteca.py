import datetime as dt
import pandas as pd
import os
import re
from datetime import datetime, timedelta
class Biblioteca():
    def _init_(self):
        self.libros_file = 'Libros.csv'
        self.prestamos_file = 'Prestamos.csv'
        self.usuarios_file = 'Usuarios.csv'
        self.mostrar_usuarios_con_deudas()
    def mostrar_usuarios_con_deudas(self):
        if os.path.exists(self.prestamos_file):
            prestamos = pd.read_csv(self.prestamos_file)
            if not prestamos.empty:
                print("Usuarios con préstamos o deudas:")
                print(prestamos[['USUARIO', 'FECHA_ENTREGA']])
            else:
                print("No hay usuarios con préstamos pendientes.")
        else:
            print("No existe el archivo de préstamos.")
    def Prestar_libro(self):
        if os.path.exists(self.libros_file):
            libros_existentes = pd.read_csv(self.libros_file)
            libros_disponibles = libros_existentes[libros_existentes['CANTIDAD'] > 0]
            if not libros_disponibles.empty:
                print("Libros disponibles para prestar:")
                print(libros_disponibles[['CODIGO', 'AUTOR', 'TEMA', 'CANTIDAD', 'PRECIO']])
                codigo_prestamo = input("Ingrese el código del libro que desea prestar: ")
                if codigo_prestamo in libros_disponibles['CODIGO'].values:
                    libros_existentes.loc[libros_existentes['CODIGO'] == codigo_prestamo, 'CANTIDAD'] -= 1
                    if 'PRESTADO' not in libros_existentes.columns:
                        libros_existentes['PRESTADO'] = 0
                    libros_existentes.loc[libros_existentes['CODIGO'] == codigo_prestamo, 'PRESTADO'] += 1
                    fecha_prestamo = datetime.now()
                    fecha_entrega = fecha_prestamo + timedelta(days=15)
                    prestamos_df = pd.DataFrame({'CODIGO': [codigo_prestamo],'FECHA_PRESTAMO': [fecha_prestamo.strftime("%Y-%m-%d")],'FECHA_ENTREGA': [fecha_entrega.strftime("%Y-%m-%d")],'USUARIO': [input("Ingrese su nombre de usuario: ")]})
                    if os.path.exists(self.prestamos_file):
                        prestamos_existentes = pd.read_csv(self.prestamos_file)
                        prestamos_df = pd.concat([prestamos_existentes, prestamos_df], ignore_index=True)
                    prestamos_df.to_csv(self.prestamos_file, index=False)
                    libros_existentes.to_csv(self.libros_file, index=False)
                    print(f"El libro con código {codigo_prestamo} ha sido prestado. Debe ser devuelto antes de {fecha_entrega.strftime('%Y-%m-%d')}.")
                else:
                    print("El código ingresado no corresponde a un libro disponible.")
            else:
                print("No hay libros disponibles para prestar.")
        else:
            print("No existe el archivo de libros.")
class Usuario():
    def Prestar_libro(self):
        if os.path.exists('Libros.csv'):
            libros_existentes = pd.read_csv('Libros.csv')
            libros_disponibles = libros_existentes[libros_existentes['CANTIDAD'] > 0]
            if not libros_disponibles.empty:
                print("Libros disponibles para prestar:")
                print(libros_disponibles[['CODIGO', 'AUTOR', 'TEMA', 'CANTIDAD', 'PRECIO']])
                codigo_prestamo = input("Ingrese el código del libro que desea prestar: ")
                nombre_usuario = input("Ingrese su nombre: ") 
                if codigo_prestamo in libros_disponibles['CODIGO'].values:
                    libros_existentes.loc[libros_existentes['CODIGO'] == codigo_prestamo, 'CANTIDAD'] -= 1
                    if 'PRESTADO' not in libros_existentes.columns:
                        libros_existentes['PRESTADO'] = 0
                    libros_existentes.loc[libros_existentes['CODIGO'] == codigo_prestamo, 'PRESTADO'] += 1
                    fecha_prestamo = datetime.now()
                    fecha_entrega = fecha_prestamo + timedelta(days=15)
                    prestamos_df = pd.DataFrame({'CODIGO': [codigo_prestamo],'FECHA_PRESTAMO': [fecha_prestamo.strftime("%Y-%m-%d")],'FECHA_ENTREGA': [fecha_entrega.strftime("%Y-%m-%d")],'USUARIO': [nombre_usuario]  })
                    if os.path.exists('Prestamos.csv'):
                        prestamos_existentes = pd.read_csv('Prestamos.csv')
                        prestamos_df = pd.concat([prestamos_existentes, prestamos_df], ignore_index=True)
                    prestamos_df.to_csv('Prestamos.csv', index=False)
                    libros_existentes.to_csv('Libros.csv', index=False)
                    print(f"El libro con código {codigo_prestamo} ha sido prestado. Debe ser devuelto antes de {fecha_entrega.strftime('%Y-%m-%d')}.")
                else:
                    print("El código ingresado no corresponde a un libro disponible.")
            else:
                print("No hay libros disponibles para prestar.")
        else:
            print("No existe el archivo de libros.")
    def Consultar_prestamos(self):
        if os.path.exists('Prestamos.csv'):
            prestamos = pd.read_csv('Prestamos.csv')
            print("Listado de préstamos:")
            print(prestamos[['CODIGO', 'FECHA_PRESTAMO', 'FECHA_ENTREGA']])
        else:
            print("No hay registros de préstamos.")
class Administrador():
    def Crear_libros(self):
        self.CODIGO = input('Digite el código alfanumérico: ').strip()
        if re.match(r'^[a-zA-Z0-9]+$', self.CODIGO):
            self.AUTOR = input('Digite el autor: ')
            self.TEMA = input('Digite el tema: ')
            self.NUM_PAG = int(input('Digite el número de páginas: '))
            self.CANTIDAD = int(input('Digite la cantidad de ejemplares: '))
            self.PRECIO = float(input('Digite el precio de cada libro: '))
            nuevo_libro = pd.DataFrame({'CODIGO': [self.CODIGO],'AUTOR': [self.AUTOR],'TEMA': [self.TEMA],'NUM_PAG': [self.NUM_PAG],'CANTIDAD': [self.CANTIDAD],'PRECIO': [self.PRECIO]})
            if os.path.exists('Libros.csv'):
                libros_existentes = pd.read_csv('Libros.csv')
                self.LIBROS = pd.concat([libros_existentes, nuevo_libro], ignore_index=True)
            else:
                self.LIBROS = nuevo_libro
            self.LIBROS.to_csv('Libros.csv', index=False)
            print('Libro creado con éxito')
        else:
            print("Código inválido. Debe ser alfanumérico.")
            self.Crear_libros()
    def Editar(self):
        codigo = input("Ingrese el código del libro que desea editar: ")
        if os.path.exists('Libros.csv'):
            libros_existentes = pd.read_csv('Libros.csv')
            if codigo in libros_existentes['CODIGO'].values:
                nuevo_codigo = input("Ingrese el nuevo código: ")
                nuevo_autor = input("Ingrese el nuevo autor: ")
                nuevo_tema = input("Ingrese el nuevo tema: ")
                nuevo_num_pag = input("Ingrese el nuevo número de páginas: ")
                nuevo_cantidad = input("Ingrese la nueva cantidad de ejemplares: ")
                nuevo_precio = input("Ingrese el nuevo precio de cada libro: ")
                libros_existentes.loc[libros_existentes['CODIGO'] == codigo, ['CODIGO', 'AUTOR', 'TEMA', 'NUM_PAG', 'CANTIDAD', 'PRECIO']] = [nuevo_codigo, nuevo_autor, nuevo_tema, nuevo_num_pag, nuevo_cantidad, nuevo_precio]
                libros_existentes.to_csv('Libros.csv', index=False)
                print("Datos actualizados con éxito.")
            else:
                print("El libro con el código especificado no existe.")
    def Eliminar(self):
        codigo_eliminar = input("Ingrese el código del libro que desea eliminar: ")
        if os.path.exists('Libros.csv'):
            libros_existentes = pd.read_csv('Libros.csv')
            if codigo_eliminar in libros_existentes['CODIGO'].values:
                libros_actualizados = libros_existentes[libros_existentes['CODIGO'] != codigo_eliminar]
                libros_actualizados.to_csv('Libros.csv', index=False)
                print("Libro eliminado con éxito.")
            else:
                print("El libro con el código especificado no existe.")
        else:
            print("No existe el archivo de libros.")
    def Crear_Estud(self):
        self.nombre = input("Ingrese su nombre: ")
        self._clave = input("Ingrese su clave: ")
        nuevo_usuario = pd.DataFrame({'NOMBRE': [self.nombre],'CLAVE': [self._clave]})
        if os.path.exists('Usuarios.csv'):
            usuarios_existentes = pd.read_csv('Usuarios.csv')
            self.USUARIOS = pd.concat([usuarios_existentes, nuevo_usuario], ignore_index=True)
        else:
            self.USUARIOS = nuevo_usuario
        self.USUARIOS.to_csv('Usuarios.csv', index=False)
        print("Usuario creado con éxito.")
# a=Usuario()
# a.Prestar_libro()
# a.Consultar_prestamos()
# b=Administrador()
# b.Crear_libros()
# b.Editar()
# b.Eliminar()
# b.Crear_Estud()
# c=Biblioteca()
# c.mostrar_usuarios_con_deudas()
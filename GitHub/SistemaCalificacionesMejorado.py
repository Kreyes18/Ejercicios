import csv
from datetime import datetime

# Función para leer datos desde un archivo CSV
def leer_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            datos.append(fila)
    return datos

# Función para escribir datos en un archivo CSV
def guardar_csv(nombre_archivo, datos, campos):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(datos)

# Función para registrar estudiantes
def registrar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    estudiantes.append({'nombre': nombre, 'curso': curso})
    guardar_csv('estudiantes.csv', estudiantes, ['nombre', 'curso'])

# Función para registrar calificaciones
def registrar_calificaciones(calificaciones):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    asignatura = input("Ingrese la asignatura: ")
    nota_saber = float(input("Ingrese la nota de saber (40%): "))
    nota_saber_hacer = float(input("Ingrese la nota de saber hacer (50%): "))
    nota_ser = float(input("Ingrese la nota de ser (10%): "))
    calificaciones.append({
        'nombre_estudiante': nombre_estudiante,
        'asignatura': asignatura,
        'nota_saber': nota_saber,
        'nota_saber_hacer': nota_saber_hacer,
        'nota_ser': nota_ser
    })
    guardar_csv('calificaciones.csv', calificaciones, ['nombre_estudiante', 'asignatura', 'nota_saber', 'nota_saber_hacer', 'nota_ser'])

# Función para registrar asistencia
def registrar_asistencia(asistencia):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    asignatura = input("Ingrese la asignatura: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    asistio = input("¿Asistió? (1 para sí, 0 para no): ")
    asistencia.append({
        'nombre_estudiante': nombre_estudiante,
        'asignatura': asignatura,
        'fecha': fecha,
        'asistencia': asistio
    })
    guardar_csv('asistencia.csv', asistencia, ['nombre_estudiante', 'asignatura', 'fecha', 'asistencia'])

# Función para gestionar la biblioteca
def gestionar_biblioteca(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    biblioteca.append({'titulo': titulo, 'autor': autor, 'cantidad': cantidad})
    guardar_csv('biblioteca.csv', biblioteca, ['titulo', 'autor', 'cantidad'])

# Función para registrar votaciones
def registrar_votaciones(votaciones):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    candidato = input("Ingrese el nombre del candidato: ")
    votaciones.append({'nombre_estudiante': nombre_estudiante, 'candidato': candidato})
    guardar_csv('votaciones.csv', votaciones, ['nombre_estudiante', 'candidato'])

# Función para mostrar datos
def mostrar_datos(nombre_archivo):
    datos = leer_csv(nombre_archivo)
    for fila in datos:
        print(fila)

# Función principal del menú
def menu():
    estudiantes = leer_csv('estudiantes.csv')
    calificaciones = leer_csv('calificaciones.csv')
    asistencia = leer_csv('asistencia.csv')
    biblioteca = leer_csv('biblioteca.csv')
    votaciones = leer_csv('votaciones.csv')
    
    while True:
        print("\nMenú:")
        print("1. Registrar estudiante")
        print("2. Registrar calificaciones")
        print("3. Registrar asistencia")
        print("4. Gestionar biblioteca")
        print("5. Registrar votaciones")
        print("6. Mostrar estudiantes")
        print("7. Mostrar calificaciones")
        print("8. Mostrar asistencia")
        print("9. Mostrar biblioteca")
        print("10. Mostrar votaciones")
        print("11. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            registrar_calificaciones(calificaciones)
        elif opcion == "3":
            registrar_asistencia(asistencia)
        elif opcion == "4":
            gestionar_biblioteca(biblioteca)
        elif opcion == "5":
            registrar_votaciones(votaciones)
        elif opcion == "6":
            print("\nEstudiantes:")
            mostrar_datos('estudiantes.csv')
        elif opcion == "7":
            print("\nCalificaciones:")
            mostrar_datos('calificaciones.csv')
        elif opcion == "8":
            print("\nAsistencia:")
            mostrar_datos('asistencia.csv')
        elif opcion == "9":
            print("\nBiblioteca:")
            mostrar_datos('biblioteca.csv')
        elif opcion == "10":
            print("\nVotaciones:")
            mostrar_datos('votaciones.csv')
        elif opcion == "11":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()

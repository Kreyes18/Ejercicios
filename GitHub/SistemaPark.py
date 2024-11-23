import datetime

# Precios por fracción de 15 minutos
PRECIO_MOTO = 500
PRECIO_CARRO = 1000

# Datos del parqueadero
vehiculos = []

def registrar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo (moto/carro): ").lower()
    placa = input("Ingrese la placa del vehículo: ")
    hora_entrada = input("Ingrese la hora de entrada (HH:MM): ")
    vehiculos.append({
        "tipo": tipo,
        "placa": placa,
        "hora_entrada": hora_entrada,
        "hora_salida": None,
        "duracion": None,
        "precio": None
    })
    print(f"Vehículo {tipo} con placa {placa} registrado a las {hora_entrada}.")

def calcular_precio(duracion, tipo):
    fracciones = duracion // 15
    if duracion % 15 != 0:
        fracciones += 1
    if tipo == "moto":
        return fracciones * PRECIO_MOTO
    elif tipo == "carro":
        return fracciones * PRECIO_CARRO

def registrar_salida():
    placa = input("Ingrese la placa del vehículo que va a salir: ")
    hora_salida = input("Ingrese la hora de salida (HH:MM): ")
    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa and vehiculo["hora_salida"] is None:
            vehiculo["hora_salida"] = hora_salida
            hora_entrada = datetime.datetime.strptime(vehiculo["hora_entrada"], "%H:%M")
            hora_salida_dt = datetime.datetime.strptime(hora_salida, "%H:%M")
            duracion = int((hora_salida_dt - hora_entrada).total_seconds() // 60)
            vehiculo["duracion"] = duracion
            vehiculo["precio"] = calcular_precio(duracion, vehiculo["tipo"])
            print(f"Duración del parqueo: {duracion} minutos.")
            print(f"Precio a pagar: ${vehiculo['precio']}")
            return
    print("Vehículo no encontrado o ya registrado como salido.")

def mostrar_resumen():
    total_motos = sum(1 for v in vehiculos if v["tipo"] == "moto")
    total_carros = sum(1 for v in vehiculos if v["tipo"] == "carro")
    total_recaudado = sum(v["precio"] for v in vehiculos if v["precio"] is not None)
    print(f"Total de motos: {total_motos}")
    print(f"Total de carros: {total_carros}")
    print(f"Total recaudado: ${total_recaudado}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Registrar vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar resumen del día")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_vehiculo()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()

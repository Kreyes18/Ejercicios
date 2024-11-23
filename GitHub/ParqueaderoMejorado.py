import tkinter as tk
from tkinter import messagebox
import pandas as pd
import datetime
import os
PRECIO_MOTO = 1000
PRECIO_CARRO = 1500
if os.path.exists("vehiculos.csv"):
    vehiculos = pd.read_csv("vehiculos.csv")
else:
    vehiculos = pd.DataFrame(columns=["tipo", "placa", "hora_entrada", "hora_salida", "duracion", "precio"])
def guardar_datos():
    vehiculos.to_csv("vehiculos.csv", index=False)
def registrar_vehiculo():
    tipo = tipo_var.get().lower()
    placa = placa_entry.get()
    hora_entrada = hora_entry.get()
    if not tipo or not placa or not hora_entrada:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    global vehiculos
    nuevo_vehiculo = pd.DataFrame([[tipo, placa, hora_entrada, None, None, None]], columns=["tipo", "placa", "hora_entrada", "hora_salida", "duracion", "precio"])
    vehiculos = pd.concat([vehiculos, nuevo_vehiculo], ignore_index=True)
    guardar_datos()  # Guardar datos después de registrar un vehículo
    messagebox.showinfo("Registro", f"Vehículo {tipo} con placa {placa} registrado a las {hora_entrada}.")
    placa_entry.delete(0, tk.END)
    hora_entry.delete(0, tk.END)
def obtener_multiplo(n):
    if n < 1000:
        return 500
    elif n < 5000:
        return 1000
    else:
        return 5000
def aproximar_al_multiplo_superior(n):
    multiplo = obtener_multiplo(n)
    if n % multiplo == 0:
        return n  
    else:
        return (n // multiplo + 1) * multiplo
def calcular_precio(duracion, tipo):
    fracciones = duracion // 30
    if duracion % 30 != 0:
        fracciones += 1
    if tipo == "moto":
        return fracciones * PRECIO_MOTO
    elif tipo == "carro":
        numero = fracciones * PRECIO_CARRO
        return aproximar_al_multiplo_superior(numero)
def registrar_salida():
    placa = placa_salida_entry.get()
    hora_salida = hora_salida_entry.get()
    if not placa or not hora_salida:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    global vehiculos
    for index, vehiculo in vehiculos.iterrows():
        if vehiculo["placa"] == placa and vehiculo["hora_salida"] is None:
            vehiculos.at[index, "hora_salida"] = hora_salida
            hora_entrada = datetime.datetime.strptime(vehiculo["hora_entrada"], "%H:%M")
            hora_salida_dt = datetime.datetime.strptime(hora_salida, "%H:%M")
            duracion = int((hora_salida_dt - hora_entrada).total_seconds() // 60)
            vehiculos.at[index, "duracion"] = duracion
            vehiculos.at[index, "precio"] = calcular_precio(duracion, vehiculo["tipo"])
            guardar_datos()  # Guardar datos después de registrar una salida
            messagebox.showinfo("Salida", f"Duración del parqueo: {duracion} minutos.\nPrecio a pagar: ${vehiculos.at[index, 'precio']}")
            placa_salida_entry.delete(0, tk.END)
            hora_salida_entry.delete(0, tk.END)
            return
    messagebox.showerror("Error", "Vehículo no encontrado o ya registrado como salido.")
def mostrar_resumen():
    total_motos = vehiculos[vehiculos["tipo"] == "moto"].shape[0]
    total_carros = vehiculos[vehiculos["tipo"] == "carro"].shape[0]
    total_recaudado = vehiculos["precio"].sum()
    resumen = f"Total de motos: {total_motos}\nTotal de carros: {total_carros}\nTotal recaudado: ${total_recaudado}"
    messagebox.showinfo("Resumen del día", resumen)
def mostrar_vehiculos():
    if vehiculos.empty:
        messagebox.showinfo("Vehículos en el parqueadero", "No hay vehículos registrados.")
        return
    lista_vehiculos = "\n".join(f"{v['tipo'].capitalize()} - Placa: {v['placa']} - Hora de entrada: {v['hora_entrada']}" for index, v in vehiculos.iterrows() if v["hora_salida"] is None)
    messagebox.showinfo("Vehículos en el parqueadero", lista_vehiculos)
root = tk.Tk()
root.title("Parqueadero")
tk.Label(root, text="Registrar Vehículo").grid(row=0, columnspan=2)
tk.Label(root, text="Tipo (moto/carro):").grid(row=1, column=0)
tipo_var = tk.StringVar()
tk.Entry(root, textvariable=tipo_var).grid(row=1, column=1)
tk.Label(root, text="Placa:").grid(row=2, column=0)
placa_entry = tk.Entry(root)
placa_entry.grid(row=2, column=1)
tk.Label(root, text="Hora de entrada (HH:MM):").grid(row=3, column=0)
hora_entry = tk.Entry(root)
hora_entry.grid(row=3, column=1)
tk.Button(root, text="Registrar", command=registrar_vehiculo).grid(row=4, columnspan=2)
tk.Label(root, text="Registrar Salida").grid(row=5, columnspan=2)
tk.Label(root, text="Placa:").grid(row=6, column=0)
placa_salida_entry = tk.Entry(root)
placa_salida_entry.grid(row=6, column=1)
tk.Label(root, text="Hora de salida (HH:MM):").grid(row=7, column=0)
hora_salida_entry = tk.Entry(root)
hora_salida_entry.grid(row=7, column=1)
tk.Button(root, text="Registrar Salida", command=registrar_salida).grid(row=8, columnspan=2)
tk.Button(root, text="Mostrar Resumen", command=mostrar_resumen).grid(row=9, columnspan=2)
tk.Button(root, text="Mostrar Vehículos", command=mostrar_vehiculos).grid(row=10, columnspan=2)
root.mainloop()
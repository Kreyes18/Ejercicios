import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
from PIL import Image, ImageTk
def calcular(colores):
    valor = {"negro": 0,"marrón": 1,"rojo": 2,"naranja": 3,"amarillo": 4,"verde": 5,"azul": 6,"violeta": 7,"gris": 8,"blanco": 9,"oro": -1,"plata": -2}
    tole = {"marrón": "±1%","rojo": "±2%","verde": "±0.5%","azul": "±0.25%","violeta": "±0.1%","gris": "±0.05%","oro": "±5%","plata": "±10%"}
    if len(colores) < 4:
        return "Se necesitan al menos 4 colores."
    try:
        primer = valor[colores[0].lower()]
        segundo = valor[colores[1].lower()]
        tercer = valor[colores[2].lower()]
        cuarto_color = colores[3].lower()
        resi = (primer * 10 + segundo) * (10 ** tercer)
        toler = tole.get(cuarto_color, "Tolerancia no válida")
        return f"El valor de la resistencia es: {resi} ohmios, Tolerancia: {toler}"
    except KeyError as e:
        return f"Color no reconocido: {str(e)}. Asegúrate de ingresar colores válidos."
def detectar(imagen_path):
    imagen = cv2.imread(imagen_path)
    if imagen is None:
        return "No se pudo cargar la imagen."
    imagen = cv2.resize(imagen, (400, 200))
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    colores_detectados = []
    rangos_colores = {"rojo": ([0, 100, 100], [10, 255, 255]),"marrón": ([10, 100, 20], [20, 255, 200]),"amarillo": ([20, 100, 100], [30, 255, 255]),"verde": ([30, 100, 100], [90, 255, 255]),"azul": ([90, 100, 100], [130, 255, 255]),"violeta": ([130, 100, 100], [160, 255, 255]),"negro": ([0, 0, 0], [180, 255, 60]),"blanco": ([0, 0, 200], [180, 20, 255]),"oro": ([10, 100, 20], [30, 255, 255]), "plata": ([0, 0, 200], [180, 0, 255])}
    for color, (lower, upper) in rangos_colores.items():
        lower = np.array(lower)
        upper = np.array(upper)
        mascara = cv2.inRange(hsv, lower, upper)
        if np.any(mascara):
            colores_detectados.append(color)
    if len(colores_detectados) < 4:
        return "No se detectaron suficientes colores."
    contador = Counter(colores_detectados)
    colores_frecuentes = [color for color, _ in contador.most_common(4)]
    return colores_frecuentes
def cargar_imagen():
    imagen_path = filedialog.askopenfilename(title="Selecciona la imagen de la resistencia",filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png")])
    if imagen_path:
        colores = detectar(imagen_path)
        if isinstance(colores, str):
            messagebox.showerror("Error", colores)
        else:
            resultado = calcular(colores)
            messagebox.showinfo("Resultado", resultado)
def calcular_manual():
    colores_input = entry_colores.get()
    colores = [color.strip() for color in colores_input.split(',')]
    if len(colores) < 4:
        messagebox.showerror("Error", "Se requieren al menos 4 colores.")
        return
    resultado = calcular(colores)
    messagebox.showinfo("Resultado", resultado)
root = tk.Tk()
root.title("Calculadora de Resistencias")
frame_manual = tk.Frame(root)
frame_manual.pack(pady=10)
label_colores = tk.Label(frame_manual, text="Ingresa los colores (separados por comas):")
label_colores.pack()
entry_colores = tk.Entry(frame_manual, width=50)
entry_colores.pack()
btn_calcular = tk.Button(frame_manual, text="Calcular Resistencia", command=calcular_manual)
btn_calcular.pack(pady=10)
frame_imagen = tk.Frame(root)
frame_imagen.pack(pady=10)
root.mainloop()
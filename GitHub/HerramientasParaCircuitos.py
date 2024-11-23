import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
def ventana_terciaria():
    def calcular_voltaje():
        try:
            voltajes = list(map(float, entrada_voltajes.get().split(',')))
            resultado = sum(voltajes)
            resultado_label.config(text=f"Resultado: {resultado} V")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos separados por comas.")
    voltaje = tk.Toplevel()
    voltaje.title("Suma de voltajes")
    voltaje.geometry("400x300")
    tk.Label(voltaje, text="Ingresa los voltajes (separadas por comas):").pack(pady=10)
    entrada_voltajes = tk.Entry(voltaje, width=30)
    entrada_voltajes.pack(pady=5)
    tk.Button(voltaje, text="Calcular", command=calcular_voltaje).pack(pady=10)
    resultado_label = tk.Label(voltaje, text="Resultado: ")
    resultado_label.pack(pady=20)
def calcular_resistencia():
    colores = [color1.get(), color2.get(), color3.get(), color4.get()]
    valores = {'negro': 0, 'marrón': 1, 'rojo': 2, 'naranja': 3, 'amarillo': 4,
            'verde': 5, 'azul': 6, 'violeta': 7, 'gris': 8, 'blanco': 9}
    multiplicadores = {'negro': 1, 'marrón': 10, 'rojo': 100, 'naranja': 1000, 'amarillo': 10000,
                    'verde': 100000, 'azul': 1000000, 'violeta': 10000000, 'gris': 100000000, 'blanco': 1000000000}
    tolerancias = {'marrón': 1, 'rojo': 2, 'verde': 0.5, 'azul': 0.25, 'violeta': 0.1, 'gris': 0.05, 'oro': 5, 'plata': 10}
    try:
        valor = (valores[colores[0]] * 10 + valores[colores[1]]) * multiplicadores[colores[2]]
        tolerancia = tolerancias.get(colores[3], 20)
        resultado.set(f"{valor} Ω ± {tolerancia}%")
    except KeyError:
        messagebox.showerror("Error", "Color no válido")
def ventana_secundaria():
    def calcular_paralelo():
        try:
            resistencias =list(map(float, entrada_resistencias.get().split(',')))
            resultado = 1 / sum(1 / r for r in resistencias)
            resultado_label.config(text=f"Resultado en paralelo: {resultado:.2f} Ω")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos separados por comas.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se permite una resistencia de valor cero en paralelo.")
    def calcular_serie():
        try:
            resistencias = list(map(float, entrada_resistencias.get().split(',')))
            resultado = sum(resistencias)
            resultado_label.config(text=f"Resultado en serie: {resultado} Ω")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos separados por comas.")
    ventana = tk.Toplevel()
    ventana.title("Suma de resistencias")
    ventana.geometry("400x300")
    tk.Label(ventana, text="Ingresa las resistencias (separadas por comas):").pack(pady=10)
    entrada_resistencias = tk.Entry(ventana, width=30)
    entrada_resistencias.pack(pady=5)
    tk.Button(ventana, text="Calcular en Serie", command=calcular_serie).pack(pady=10)
    tk.Button(ventana, text="Calcular en Paralelo", command=calcular_paralelo).pack(pady=10)
    resultado_label = tk.Label(ventana, text="Resultado: ")
    resultado_label.pack(pady=20)
def ventana_divisor():
    resistencias_voltaje = []
    def agregar_resistencia_voltaje():
        try:
            valor = float(nueva_resistencia_voltaje.get())
            if valor <= 0:
                raise ValueError("La resistencia debe ser mayor que 0")
            resistencias_voltaje.append(valor)
            actualizar_lista_resistencias_voltaje()
            nueva_resistencia_voltaje.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido para la resistencia.")
    def eliminar_resistencia_voltaje():
        if resistencias_voltaje:
            resistencias_voltaje.pop()
            actualizar_lista_resistencias_voltaje()
        else:
            messagebox.showwarning("Advertencia", "No hay resistencias para eliminar.")
    def actualizar_lista_resistencias_voltaje():
        lista_resistencias_voltaje.set("\n".join([f"R{i+1} = {res} Ω" for i, res in enumerate(resistencias_voltaje)]))
        actualizar_opciones_resistencias_voltaje()
    def actualizar_opciones_resistencias_voltaje():
        menu_resistencia_opciones_voltaje['menu'].delete(0, 'end')
        for i in range(len(resistencias_voltaje)):
            menu_resistencia_opciones_voltaje['menu'].add_command(label=f"R{i+1}",command=tk._setit(resistencia_seleccionada_voltaje, i))
    def calcular_divisor_voltaje():
        try:
            V_in = float(entrada_voltaje.get())
            total_resistencia = sum(resistencias_voltaje)
            indice = resistencia_seleccionada_voltaje.get()
            if indice >= len(resistencias_voltaje) or indice < 0:
                raise ValueError("Selecciona una resistencia válida.")
            V_out = V_in * (resistencias_voltaje[indice] / total_resistencia)
            resultado_voltaje.set(f"Voltaje en R{indice+1}: {V_out:.2f} V")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos y selecciona una resistencia.")
    def calcular_divisor_corriente():
        try:
            I_in = float(entrada_corriente.get())
            R1 = float(resistencia1_corriente.get())
            R2 = float(resistencia2_corriente.get())
            I_R1 = I_in * (R2 / (R1 + R2))
            I_R2 = I_in * (R1 / (R1 + R2))
            resultado_corriente_R1.set(f"Corriente en R1: {I_R1:.2f} A")
            resultado_corriente_R2.set(f"Corriente en R2: {I_R2:.2f} A")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
    divisor = tk.Toplevel()
    divisor.title("Divisor de Voltaje y Corriente")
    frame_voltaje = tk.LabelFrame(divisor, text="Divisor de Voltaje", padx=10, pady=10)
    frame_voltaje.pack(padx=10, pady=10)
    tk.Label(frame_voltaje, text="Voltaje(V):").grid(row=0, column=0, sticky="e")
    entrada_voltaje = tk.Entry(frame_voltaje)
    entrada_voltaje.grid(row=0, column=1)
    tk.Label(frame_voltaje, text="Resistencia(Ω):").grid(row=1, column=0, sticky="e")
    nueva_resistencia_voltaje = tk.Entry(frame_voltaje)
    nueva_resistencia_voltaje.grid(row=1, column=1)
    tk.Button(frame_voltaje, text="Agregar", command=agregar_resistencia_voltaje).grid(row=1, column=2)
    tk.Button(frame_voltaje, text="Eliminar última resistencia", command=eliminar_resistencia_voltaje).grid(row=2, column=0, columnspan=3, pady=5)
    lista_resistencias_voltaje = tk.StringVar()
    tk.Label(frame_voltaje, text="Resistencias actuales:").grid(row=3, column=0, columnspan=3)
    tk.Label(frame_voltaje, textvariable=lista_resistencias_voltaje).grid(row=4, column=0, columnspan=3)
    resistencia_seleccionada_voltaje = tk.IntVar(value=0)
    tk.Label(frame_voltaje, text="Selecciona la resistencia:").grid(row=5, column=0, columnspan=3)
    menu_resistencia_opciones_voltaje = tk.OptionMenu(frame_voltaje, resistencia_seleccionada_voltaje, [])
    menu_resistencia_opciones_voltaje.grid(row=6, column=0, columnspan=3)
    resultado_voltaje = tk.StringVar()
    tk.Button(frame_voltaje, text="Calcular Voltaje en Resistencia", command=calcular_divisor_voltaje).grid(row=7, column=0, columnspan=3, pady=5)
    tk.Label(frame_voltaje, textvariable=resultado_voltaje).grid(row=8, column=0, columnspan=3)
    frame_corriente = tk.LabelFrame(divisor, text="Divisor de Corriente", padx=10, pady=10)
    frame_corriente.pack(padx=10, pady=10)
    tk.Label(frame_corriente, text="Corriente(I):").grid(row=0, column=0, sticky="e")
    entrada_corriente = tk.Entry(frame_corriente)
    entrada_corriente.grid(row=0, column=1)
    tk.Label(frame_corriente, text="Resistencia 1(Ω):").grid(row=1, column=0, sticky="e")
    resistencia1_corriente = tk.Entry(frame_corriente)
    resistencia1_corriente.grid(row=1, column=1)
    tk.Label(frame_corriente, text="Resistencia 2(Ω):").grid(row=2, column=0, sticky="e")
    resistencia2_corriente = tk.Entry(frame_corriente)
    resistencia2_corriente.grid(row=2, column=1)
    resultado_corriente_R1 = tk.StringVar()
    tk.Label(frame_corriente, textvariable=resultado_corriente_R1).grid(row=4, column=0, columnspan=2)
    resultado_corriente_R2 = tk.StringVar()
    tk.Label(frame_corriente, textvariable=resultado_corriente_R2).grid(row=5, column=0, columnspan=2)
    tk.Button(frame_corriente, text="Calcular Corriente en R1 y R2", command=calcular_divisor_corriente).grid(row=3, column=0, columnspan=2, pady=5)
def procesar_imagen():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    img = Image.open(filepath)
    img.thumbnail((250, 250))
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img
root = tk.Tk()
root.title("Herramientas para circuitos electrónicos")
frame = tk.Frame(root)
frame.pack(pady=20)
tk.Label(frame, text="Banda 1").grid(row=0, column=0)
tk.Label(frame, text="Banda 2").grid(row=1, column=0)
tk.Label(frame, text="Banda 3").grid(row=2, column=0)
tk.Label(frame, text="Tolerancia ").grid(row=3, column=0)
color1 = tk.StringVar()
color2 = tk.StringVar()
color3 = tk.StringVar()
color4 = tk.StringVar()
colores = ['negro', 'marrón', 'rojo', 'naranja', 'amarillo', 'verde', 'azul', 'violeta', 'gris', 'blanco', 'oro', 'plata']
tolerancias = ['marrón', 'rojo', 'verde', 'azul', 'violeta', 'gris', 'oro', 'plata']
tk.OptionMenu(frame, color1, *colores).grid(row=0, column=1)
tk.OptionMenu(frame, color2, *colores).grid(row=1, column=1)
tk.OptionMenu(frame, color3, *colores).grid(row=2, column=1)
tk.OptionMenu(frame, color4, *tolerancias).grid(row=3, column=1)
tk.Button(frame, text="Calcular", command=calcular_resistencia).grid(row=4, columnspan=2, pady=10)
resultado = tk.StringVar()
tk.Label(frame, textvariable=resultado).grid(row=5, columnspan=2)
tk.Button(root, text="Sumas resisitencias", command=ventana_secundaria).pack(pady=10)
tk.Button(root, text="Sumas de voltajes", command=ventana_terciaria).pack(pady=10)
tk.Button(root, text="Divisores", command=ventana_divisor).pack(pady=10)
panel = tk.Label(root)
panel.pack()
root.mainloop()
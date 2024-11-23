# Solicitar coeficientes a, b y c
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Calcular el discriminante
D = b**2 - 4*a*c

# Verificar la naturaleza de las raíces
if D > 0:
    # Dos raíces reales distintas
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print("Las raíces son reales y distintas: x1 =", x1, "x2 =", x2)
elif D == 0:
    # Dos raíces reales iguales
    x = -b / (2*a)
    print("Las raíces son reales e iguales: x =", x)
else:
    # Dos raíces complejas
    real_part = -b / (2*a)
    imag_part = abs(D)**0.5 / (2*a)
    print("Las raíces son complejas: x1 =", real_part, "+", imag_part, "i, x2 =", real_part, "-", imag_part, "i")

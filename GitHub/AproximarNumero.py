def obtener_multiplo(n):
    # Define el múltiplo según el rango del número
    if n < 1000:
        return 500
    elif n < 5000:
        return 1000
    else:
        return 5000

def aproximar_al_multiplo_superior(n):
    multiplo = obtener_multiplo(n)
    # Calcular el próximo múltiplo superior
    if n % multiplo == 0:
        return n  # Si ya es un múltiplo, se devuelve el mismo número
    else:
        return (n // multiplo + 1) * multiplo

# Ejemplo de uso
numero = float(input("Ingrese el número a aproximar: "))
resultado = aproximar_al_multiplo_superior(numero)
print(f"El número {numero} aproximado al siguiente múltiplo superior es {resultado}.")

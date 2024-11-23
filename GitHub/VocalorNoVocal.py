letra = input("Ingresa una letra: ")

if len(letra) != 1:
    print("No se puede procesar el dato. Debes ingresar solo un carácter.")
elif letra in 'aeiouAEIOU':
    print("Es vocal")
else:
    print("No es vocal")

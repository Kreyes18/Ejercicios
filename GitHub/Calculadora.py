import math
while True:
    print("Menú de Calculadora")
    print("1.sumar")
    print("2.restar")
    print("3.multiplicar")
    print("4.dividir")
    print("5.comparar números pares e impares")
    print("6.calcular porcentaje")
    print("7.calcular razones trigonométricas")
    print("8.salir")
    a=input("Elige una opción: \n")
    if a=='1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La suma es: {num1 + num2}")
    elif a=='2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La resta es: {num1 - num2}")
    elif a=='3':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La multiplicación es: {num1 * num2}")
    elif a=='4':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            print(f"La división es: {num1 / num2}")
        else:
            print("No se puede dividir por cero")
    elif a=='5':
        num = int(input("Ingrese un número: "))
        if num % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    elif a=='6':
        total = float(input("Ingrese el total: "))
        porcentaje = float(input("Ingrese el porcentaje: "))
        print(f"El {porcentaje}% de {total} es: {(total * porcentaje) / 100}")
    elif a=='7':
        angulo = float(input("Ingrese el ángulo en grados: "))
        radianes = math.radians(angulo)
        print(f"Seno: {math.sin(radianes)}")
        print(f"Coseno: {math.cos(radianes)}")
        print(f"Tangente: {math.tan(radianes)}")
    elif a=='8':
        break
    else:
        print("Por favor elige una opción del 1 al 8")

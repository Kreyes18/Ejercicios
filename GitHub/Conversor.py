print("Conversor de Unidades de Longitud")
KR1 = float(input("Ingrese el valor: "))
KR2 = input("Ingrese la unidad de origen (metros, kilometros, centimetros, millas, yardas, pies, pulgadas): ").lower()
KR3 = input("Ingrese la unidad de destino (metros, kilometros, centimetros, millas, yardas, pies, pulgadas): ").lower()
if KR2 == 'metros':
    KR4 = KR1
elif KR2 == 'kilometros':
    KR4 = KR1 * 1000
elif KR2 == 'centimetros':
    KR4 = KR1 / 100
elif KR2 == 'millas':
    KR4 = KR1 * 1609.34
elif KR2 == 'yardas':
    KR4 = KR1 * 0.9144
elif KR2 == 'pies':
    KR4 = KR1 * 0.3048
elif KR2 == 'pulgadas':
    KR4 = KR1 * 0.0254
else:
    print("Unidad de origen no válida")
    KR4 = 'a'
if KR4 is not 'a':
    if KR3 == 'metros':
        KR5 = KR4
    elif KR3 == 'kilometros':
        KR5 = KR4 / 1000
    elif KR3 == 'centimetros':
        KR5 = KR4 * 100
    elif KR3 == 'millas':
        KR5 = KR4 / 1609.34
    elif KR3 == 'yardas':
        KR5 = KR4 / 0.9144
    elif KR3 == 'pies':
        KR5 = KR4 / 0.3048
    elif KR3 == 'pulgadas':
        KR5 = KR4 / 0.0254
    else:
        print("Unidad de destino no válida")
        KR5 = 'a'
    if KR5 is not 'a':
        print(f"{KR1} {KR2} son {KR5} {KR3}")
else:
    print("No se pudo realizar la conversión debido a una unidad de origen no válida.")

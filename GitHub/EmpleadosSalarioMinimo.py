empleados = []
numero_empleados = int(input("Ingrese el número de empleados: "))
for i in range(numero_empleados):
    print("\nEmpleado", i + 1, ":")
    nombre_apellido = input("Ingrese el nombre y apellido del empleado: ")
    documento_identidad = input("Ingrese el número de documento de identidad: ")
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    empleados.append((nombre_apellido, sueldo))
salario_minimo = 5000000
for nombre_apellido,sueldo in empleados:
    if sueldo > salario_minimo:
        print(nombre_apellido, "gana más que el salario mínimo en Colombia.")
    else:
        print(nombre_apellido, "no gana más que el salario mínimo en Colombia.")

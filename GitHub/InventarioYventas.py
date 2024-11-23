import pandas as pd
import os
class Empresa():
    def __init__(self):
        self.kr_nombre = input('Ingrese el nombre del producto: ')
        self.kr_precio = int(input('Ingrese el precio del producto: '))
        self.kr_cantidad = input('Ingrese la cantidad del producto: ')
class Alimento(Empresa):
    def __init__(self):
        super().__init__()
        self.kr_tipo = "Alimento"
        self.kr__Garantia = None  # Encapsulo la garantia
        self.kr_fecha_vencimiento = input('Ingrese la fecha de vencimiento del producto: ')
        kr_producto = [{'nombre': self.kr_nombre, 'precio': self.kr_precio, 'cantidad': self.kr_cantidad,'fecha_vencimiento': self.kr_fecha_vencimiento, 'garantia': self.kr__Garantia, 'tipo': self.kr_tipo}]
        kr_df = pd.DataFrame(kr_producto)
        kr_productos_existentes = pd.read_csv("empresa.csv")
        if not kr_productos_existentes.empty:
            kr_df = pd.concat([kr_productos_existentes, kr_df])
            kr_df.to_csv('empresa.csv', index=False)
        else:
            kr_df.to_csv('empresa.csv', index=False)
        print("Producto guardado con exito")
class Electronica(Empresa):
    def __init__(self):
        super().__init__()
        self.kr_tipo = "Electronico"
        self.kr__fecha_vencimiento = None  # Encapsulo la fecha de vencimiento
        self.kr_garantia = input('Ingrese la garantia del producto: ')
        kr_producto = [{'kr_nombre': self.kr_nombre, 'kr_precio': self.kr_precio, 'kr_cantidad': self.kr_cantidad,'kr_fecha_vencimiento': self.kr__fecha_vencimiento, 'kr_garantia': self.kr_garantia, 'kr_tipo': self.kr_tipo}]
        kr_df = pd.DataFrame(kr_producto)
        kr_productos_existentes = pd.read_csv("empresa.csv")
        if not kr_productos_existentes.empty:
            kr_df = pd.concat([kr_productos_existentes, kr_df])
            kr_df.to_csv('empresa.csv', index=False)
        else:
            kr_df.to_csv('empresa.csv', index=False)
        print("Producto guardado con exito")
class Menu():
    def __init__(self):
        kr_op = input('¿Desea agregar un alimento o un producto electronico?\n1-Alimento\n2-Producto Electronico\n3-Mostrar todos los productos\n4-Venta\n5-Salir\n')
        if kr_op == '1':
            self.kr_empresa = Alimento()
        elif kr_op == '2':
            self.kr_empresa = Electronica()
        elif kr_op == "3":
            kr_df = pd.read_csv("empresa.csv")
            print(kr_df)
        elif kr_op == "4":
            self.kr_venta()
        elif kr_op == "5":
            exit()
    def kr_venta(self):
        if os.path.exists("empresa.csv"):
            kr_df = pd.read_csv("empresa.csv")
            if kr_df.empty:
                print("No hay productos disponibles para vender.")
                return
            print("Productos disponibles para la venta:")
            print(kr_df[['kr_nombre', 'kr_precio', 'kr_cantidad']])
            kr_producto_nombre = input('Ingrese el nombre del producto que desea comprar: ')
            if kr_producto_nombre in kr_df['kr_nombre'].values:
                kr_producto = kr_df[kr_df['kr_nombre'] == kr_producto_nombre].iloc[0]
                kr_cantidad_disponible = kr_producto['kr_cantidad']
                kr_precio = kr_producto['kr_precio']
                kr_cantidad_a_comprar = int(input(f'¿Cuántas unidades desea comprar de {kr_producto_nombre}? '))
                if kr_cantidad_a_comprar <= kr_cantidad_disponible:
                    kr_df.loc[kr_df['kr_nombre'] == kr_producto_nombre, 'kr_cantidad'] -= kr_cantidad_a_comprar
                    kr_total = kr_cantidad_a_comprar * float(kr_precio)
                    print(f"Venta realizada con éxito. Total: {kr_total} .")
                    kr_df.to_csv('empresa.csv', index=False)
                else:
                    print(f"No hay suficiente cantidad de {kr_producto_nombre}. Solo hay {kr_cantidad_disponible} unidades disponibles.")
            else:
                print("Producto no encontrado.")
        else:
            print("No existe el archivo empresa.csv")
while True:
    a = Menu()
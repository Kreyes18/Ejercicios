import pandas as pd
import os
class Zoo():
    def __init__(self):
        self.kr_fecha_ingreso = input("Ingrese la fecha de ingreso: ")
        self.kr_edad = input("Ingrese la edad: ")
        self.kr_enfermedades = input("Ingrese las enfermedades: ")
def contar_animales():
    kr_total_animales = 0
    kr_archivos = ["acuatico.csv", "terrestre.csv", "volador.csv"]
    for archivo in kr_archivos:
        if os.path.exists(archivo):
            kr_df = pd.read_csv(archivo)
            kr_total_animales += len(kr_df)
    return kr_total_animales
class Acuatico(Zoo):
    def __init__(self):
        super().__init__()
        self.kr_especie = "Acuatico"
        self.kr_genero = input("Ingrese el genero: ")
        self.kr_peso = input("Ingrese el peso: ")
        self.kr_altura = input("Ingrese la altura: ")
        self.kr_comida = input("Ingrese la comida que consume: ")
        if contar_animales() >= 15:
            print("No se pueden agregar más animales. El zoo ya tiene el máximo permitido de 15 animales.")
            return
        kr_animal = [{"kr_edad": self.kr_edad, 'kr_genero': self.kr_genero, 'kr_peso': self.kr_peso, 'kr_altura': self.kr_altura, 'kr_comida': self.kr_comida, "kr_tipo": self.kr_especie, "kr_fecha_ingreso": self.kr_fecha_ingreso, "kr_enfermedades": self.kr_enfermedades}]
        kr_df = pd.DataFrame(kr_animal)
        if os.path.exists("acuatico.csv"):
            kr_animales_existentes = pd.read_csv("acuatico.csv")
            kr_df = pd.concat([kr_animales_existentes, kr_df])
            kr_df.to_csv('acuatico.csv', index=False)
        else:
            kr_df.to_csv('acuatico.csv', index=False)
        print("Acuatico guardado con éxito")
class Terreste(Zoo):
    def __init__(self):
        super().__init__()
        self.kr_especie = "Terrestre"
        self.kr_genero = input("Ingrese el genero: ")
        self.kr_peso = input("Ingrese el peso: ")
        self.kr_altura = input("Ingrese la altura: ")
        self.kr_velocidad = input("Ingrese la velocidad del animal: ")
        if contar_animales() >= 15:
            print("No se pueden agregar más animales. El zoo ya tiene el máximo permitido de 15 animales.")
            return
        kr_animal = [{"edad": self.kr_edad, 'genero': self.kr_genero, 'peso': self.kr_peso, 'altura': self.kr_altura, 'velocidad': self.kr_velocidad, "tipo": self.kr_especie, "fecha_ingreso": self.kr_fecha_ingreso, "enfermedades": self.kr_enfermedades}]
        kr_df = pd.DataFrame(kr_animal)
        if os.path.exists("terrestre.csv"):
            kr_animales_existentes = pd.read_csv("terrestre.csv")
            kr_df = pd.concat([kr_animales_existentes, kr_df])
            kr_df.to_csv('terrestre.csv', index=False)
        else:
            kr_df.to_csv('terrestre.csv', index=False)
        print("Terrestre guardado con éxito")
class Volador(Zoo):
    def __init__(self):
        super().__init__()
        self.kr_especie = "Volador"
        self.kr_genero = input("Ingrese el genero: ")
        self.kr_peso = input("Ingrese el peso: ")
        self.kr_altura = input("Ingrese la altura: ")
        self.kr_envergadura = input("Ingrese la envergadura del animal: ")
        if contar_animales() >= 15:
            print("No se pueden agregar más animales. El zoo ya tiene el máximo permitido de 15 animales.")
            return
        kr_animal = [{"kr_edad": self.kr_edad, 'kr_genero': self.kr_genero, 'kr_peso': self.kr_peso, 'kr_altura': self.kr_altura, 'kr_envergadura': self.kr_envergadura, "kr_tipo": self.kr_especie, "kr_fecha_ingreso": self.kr_fecha_ingreso, "kr_enfermedades": self.kr_enfermedades}]
        kr_df = pd.DataFrame(kr_animal)
        if os.path.exists("volador.csv"):
            kr_animales_existentes = pd.read_csv("volador.csv")
            kr_df = pd.concat([kr_animales_existentes, kr_df])
            kr_df.to_csv('volador.csv', index=False)
        else:
            kr_df.to_csv('volador.csv', index=False)
        print("Volador guardado con éxito")
class Menu():
    def __init__(self):
        kr_op = input("¿Desea ingresar un animal al zoo?\n1-Ingresar\n2-Mostrar animales en el zoo\n3-Salir\n")
        if kr_op == "1":
            kr_tipo = input("¿Cuál es el tipo de animal?\n1-Acuático\n2-Terrestre\n3-Volador\n")
            if kr_tipo == "1":
                self.kr_zoo = Acuatico()
            elif kr_tipo == "2":
                self.kr_zoo = Terreste()
            elif kr_tipo == "3":
                self.kr_zoo = Volador()
            else:
                print("Tipo de animal incorrecto")
                Menu()
        elif kr_op == "2":
            print("Terrestres")
            kr_df = pd.read_csv("terrestre.csv")
            print(kr_df)
            print("Acuáticos")
            kr_df = pd.read_csv("acuatico.csv")
            print(kr_df)
            print("Voladores")
            kr_df = pd.read_csv("volador.csv")
            print(kr_df)
        elif kr_op == "3":
            exit()
while True:
    a = Menu()

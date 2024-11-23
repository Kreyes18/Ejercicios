import csv
inventario=[]

def mostrar():
    print('ingresa al modulo mostrar productos\n')
    a=len(inventario)
    if a==1:
        print('No se han registrado productos en el inventario hasta el momento\n')
    for i in (inventario):
        print(i)
        
def agregar():
    cod_produc=input('ingrese código del producto\n')
    nom_produc=input('ingrese nombre del producto\n')
    cantidad=input('ingrese cantidad disponible\n')
    inventario.append([cod_produc, nom_produc, cantidad])
    guardar()
    
def guardar(): 
    with open('C:/Users/inghe/Desktop/CSV07/prueba.csv', 'w',  newline='') as septiembre:
        escri=csv.writer(septiembre, delimiter=';')   
        escri.writerows(inventario)
    print('Datos almacenados con éxito\n')

op=int(input('marque 1: para agregar productos, 2: para ver productos\n'))

    
while op==1 or op==2:
    #Lectura de CSV. 
    with open('C:/Users/inghe/Desktop/CSV07/prueba.csv',  newline='') as septiembre:
        leer=csv.reader(septiembre, delimiter=';')
        inventario=list(leer)
    if op==1:
      print('###### AGREGAR PRODUCTO ######')
      print('\n')
      agregar()
    elif op==2:
      print('###### MOSTRAR PRODUCTOS ######')
      print('\n')
      mostrar()
    print('\n')
    op=int(input('marque 1: para agregar productos, 2: para ver productos\n'))

    

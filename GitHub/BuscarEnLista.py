#Diseñe un algoritmo que le permita crear una lista con nombres de estudiantes (N nombres), 
# su programa debe permitir buscar si los nombres están contenidos en la lista, 
# la consulta solicita nombres y verifica si están o no. Recomiendo uso for e if
a=int(input("ingrese la cantidad de estudiantes que va a registrar:  "))
lista=[]
for i in range (a):
    nombres=input("ingrese un nobre a la lista: ")
    lista.append(nombres)
r=1
while r != 2 :
    buscar=input("digite el nombre que desa buscar: ")
    xs=(buscar in lista)
    if  xs == True :
        print("el nombre consultado si esta en la lista")
        r=int(input("desea volver a buscar otro nombre \n 1-si \n 2- no \n"))
    else:
        print("el nombre consultado no esta en la lista")
        r=int(input("desea volver a buscar otro nombre \n 1-si \n 2- no \n"))
print("el programa ha terminado")

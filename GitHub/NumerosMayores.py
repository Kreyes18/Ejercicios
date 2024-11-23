#Escriba un programa que pida números enteros mientras sean cada vez más grandes, 
# al digitar un número menor que el anterior debe imprimir un mensaje diciendo que 
# ese número es menor y terminar el programa usando while.
l=[0]
entrada=int(input('Ingrese un numero positivo\n'))
i=0
while entrada>=l[i]:
   l.append(entrada)
   i=i+1
   entrada=int(input('Ingrese un numero positivo\n'))
   while entrada<=l[i]:
       entrada=int(input('Ingrese un numero mayor al anterior\n'))
   print('La suma de todos los valores es',sum(l))    
l.remove(0)
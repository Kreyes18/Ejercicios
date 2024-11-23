# Escribir un programa que permita al usuario ingresar por teclado 5 números enteros, que pueden ser positivos o negativos. 
# Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos. 
# Recuerde que no es posible dividir por cero, por lo que es necesario evitar que el programa 
# arroje un error si no se ingresaron números positivos.
div=0
sum=0
sum1=0
for i in range(5) :
    a=int(input(" diguite un numero entero: "))
    if a < 0 :
        sum1=sum1+a
    else:
        sum=sum+a
        div=div+1
        prom=sum/div
                                                            
print("la sumatoria de los numeros negativo es: ",sum1)
if div == 0 :
            print("no hay numeros positivos ")
else:
    print("el promedio de los numeros positivos es: ",prom)        
                                                                            

#Diseñe un programa empleando Python donde pueda realizar las operaciones básicas matemáticas 
# (suma, resta, multiplicación, división, raices, potencia y porcentajes). Su programa debe mostrar 
# todas las operaciones y a medida que va mostrando en pantalla los resultados debe solicitar los siguientes datos sucesivamente. 
import math
a= int(input("diguite un numero \n"))
b= int(input("diguite otro numero \n"))
print("la suma entre ",a," y ",b," es:")
print(a+b)
print("la resta entre ",a," y ",b," es:")
print(a-b)
print("la suma multiplicacion ",a," y ",b," es:")
print(a*b)
print("la divicion entre ",a," y ",b," es:")
print(float(a/b))
print("la divicion entre ",b," y ",a," es:")
print(float(b/a))
print("la potencia de base ",a," y exponente",b," es:")
print(pow(a,b))
print("la potencia de base ",b," y exponente",a," es:")
print(pow(b,a))
print("la  la rais cuadrada de ",a," es:")
print(round(pow(a,(1/2)),2))
print("la  la rais cuadrada de ",b," es:")
print(round(pow(b,(1/2)),2))

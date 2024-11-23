a='SI'
while a=='SI':
    cont=0
    cadena=input('Ingrese una cadena de texto\n')
    for letra in cadena:
        if (letra.isupper()==True):
            cont+=1
    print('La cantidad de mayusculas es: ',cont)
    a=input('Desea ingresar otra cadena\nSI o NO\n').upper()

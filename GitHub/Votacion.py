#Escriba un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: 
# candidato A, candidato B, candidato C y voto en blanco. Según el candidato elegido (A, B, C ó Voto blanco) 
# se le debe imprimir el mensaje “Usted ha votado por el candidato #”. Si el usuario ingresa una opción que no 
# corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
while True:
    op = (input("""Elija un candidato:
        1- Candidato A
        2- Candidato B
        3- Candidato C
        4- Candidato D \n"""  
    ))
  
    if op=='1':
        print ("Usted ha votado por el candidato A")
        break
    elif op=='2':
        print ("Usted ha votado por el candidato B")
        break
    elif op=='3':
        print ("Usted ha votado por el candidato C")
        break
    elif op=='4':
        print ("Usted ha votado por el candidato D")
        break
    else :
        print(str("haz seleccionado una opcion erronea"))
